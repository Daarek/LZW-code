import time

stime=time.time()

with open("finish.txt", "r") as f:
    txt = f.read().strip()


x = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя, "
dictionary = {str(i): x[i] for i in range(len(x))}

codes = txt.split()
decoded_output = ""
previous_code = ""

for code in codes:
    if code in dictionary:
        entry = dictionary[code]
    elif code == str(len(dictionary)):
        entry = previous_entry + previous_entry[0]
    else:
        raise ValueError(f"Encountered an invalid LZW code: {code}")

    decoded_output += entry

    if previous_code:
        dictionary[str(len(dictionary))] = previous_entry + entry[0]

    previous_code = code
    previous_entry = entry

with open("newfile.txt", "w") as f:
    f.write(decoded_output)

etime = time.time()

print(etime-stime)