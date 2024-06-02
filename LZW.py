import time
stime = time.time()
def initialize_dict():
    x = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя, "
    return {x[i]: i for i in range(len(x))}

def lzw_compress(txt):
    dict = initialize_dict()
    next_code = len(dict)
    pos = 0
    code_output = []

    while pos < len(txt):
        leng = 1
        while pos + leng <= len(txt) and txt[pos:pos + leng] in dict:
            leng += 1

        leng -= 1
        w = txt[pos:pos + leng]
        code_output.append(dict[w])

        if pos + leng < len(txt):
            dict[txt[pos:pos + leng + 1]] = next_code
            next_code += 1

        pos += leng

    return code_output

def main():
    with open("file.txt", "r", encoding='utf-8') as f:
        txt = f.read()
    
    code = lzw_compress(txt)
    
    with open("finish.txt", "w", encoding='utf-8') as f:
        f.write(" ".join(map(str, code)))

if __name__ == "__main__":
    main()

etime = time.time()

print(etime-stime)