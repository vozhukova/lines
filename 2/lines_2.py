from pprint import pprint
import glob, os

file_list = []
file_dict = {}

os.chdir(os.getcwd())
for file in glob.glob("*.txt"):
    file_list.append(file)

for file in file_list:
    file_dict[file] = []
    with open (file, encoding="utf-8") as f:
        count = 0
        for line in f:
            count += 1
    with open(file, encoding="utf-8") as f:
        text = f.read()
    file_dict[file].append(count)
    file_dict[file].append(text)

# print(file_dict)

sorted_dict = {}
sorted_keys = sorted(file_dict, key=file_dict.get)
for w in sorted_keys:
    sorted_dict[w] = file_dict[w]

# print(sorted_dict)

with open("all.txt", "w", encoding="utf-8") as file_all:
    for file in sorted_dict.keys():
        file_all.write(file + "\n")
        for el in sorted_dict[file]:
            file_all.write(str(el) + "\n")

file_path = os.path.join(os.getcwd(), "all.txt")
res = open(file_path, encoding="utf-8")
data = res.read()
pprint(data)
