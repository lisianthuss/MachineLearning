import urllib.request

#url = "http://image.sm.co.r/uniContent/banner/G1XU7UVCIQUUAH3J43MY/title2.jpg"
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

mem = urllib.request.urlopen(url).read()

with open(savename, "wb") as f:
    f.write(mem)
    print("image saved")
