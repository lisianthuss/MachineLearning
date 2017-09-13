import struct

def to_csv(name, maxdata):
    # open label file, image file
    lbl_f = open("./mnist/"+name+"-labels-idx1-ubyte", "rb")
    img_f = open("./mnist/"+name+"-images-idx3-ubyte", "rb")
    csv_f = open("./mnist/"+name+".csv", "w", encoding='utf-8')

    # read header
    # >: big-endian
    # I: unsigned int
    mag, lbl_count = struct.unpack(">II", lbl_f.read(8))
    mag, img_count = struct.unpack(">II", img_f.read(8))
    rows, cols = struct.unpack(">II", img_f.read(8))
    pixels = rows * cols

    # images -> csv
    res = []
    for idx in range(lbl_count):
        if idx > maxdata: break
        # B: unsigned char
        label = struct.unpack("B", lbl_f.read(1))[0] # 이미지 숫자
        bdata = img_f.read(pixels)
        sdata = list(map(lambda n: str(n), bdata))
        csv_f.write(",".join(sdata)+"\r\n")

        # save to images for test
        if idx < 10:
            s = "P2 28 28 255\n"
            s += " ".join(sdata)
# pgm 포맷은 글자 파일로 이미지를 나타낼 수 있다
            iname = "./mnist/{0}-{1}-{2}.pgm".format(name, idx, label)

            with open(iname, "w", encoding="utf-8") as f:
                f.write(s)

    csv_f.close()
    lbl_f.close()
    img_f.close()

to_csv("train", 10)
to_csv("t10k", 5)
