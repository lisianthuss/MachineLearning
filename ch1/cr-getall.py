from bs4 import BeautifulSoup
from urllib.request import *
from urllib.parse import *
from os import makedirs
import os.path, time, re

# 이미 처리한 파일인지 확인용
proc_files = {}

# HTML 내부에 있는 링크 추출
def enum_links(html, base):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.select("link[rel='stylesheet']") # css
    links += soup.select("a[href]") # link
    result = []

    # href 속성 추출, link를 절대 경로로 변환
    for a in links:
        href = a.attrs['href']
        url = urljoin(base, href)
        result.append(url)

    return result

# 파일을 다운로드, 저장
def download_file(url):
    o = urlparse(url)
    savepath = "./" + o.netloc + o.path

    print("*" * 20)
    print("o: ", o)
    print("url: ", url)
    print("o.netloc: ", o.netloc)
    print("o.path: ", o.path)

    if re.search(r"/$", savepath): # 플더라면 index.html
        savepath += "index.html"

    print("savepath: ", savepath)

    savedir = os.path.dirname(savepath)
    print("savedir: ", savedir)

    # 모두 다운됐는지 확인
    if os.path.exists(savepath): return savepath

    # 다운 받을 폴더 생성
    if not os.path.exists(savedir):
        print("mkdir=", savedir)
        makedirs(savedir)

    # 파일 다운 받기
    try:
        print("- download=", url)
        urlretrieve(url, savepath)
        
        time.sleep(1)
        return savepath
    except:
        print("failed to download: ", url)
        return None

# HTML 분석, 다운로드
def analyze_html(url, root_url):
    savepath = download_file(url)

    if savepath is None: return
    if savepath in proc_files: return # 이미 처리됨

    proc_files[savepath] = True
    print("analyze_html=", url)

    # extract link
    html = open(savepath, "r", encoding="utf-8").read()
    links = enum_links(html, url)

    for link_url in links:
        # link가 root이외의 경로면 무시
        if link_url.find(root_url) != 0:
            if not re.search(r".css$", link_url): continue

        # HTML이면
        if re.search(r".(html|htm)$", link_url):
        # 재귀적으로 HTML 파일 분석
            analyze_html(link_url, root_url)
            continue

        # 기타 파일
        download_file(link_url)

if __name__ == "__main__":
    url = "https://docs.python.org/3.5/library/"
    analyze_html(url, url)
