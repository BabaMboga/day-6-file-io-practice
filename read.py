# import os

# print(os.getcwd())
file_path = "/home/babamboga/Development/code/phase3/day-6-file-io-practice/output.txt"

with open(file_path, 'r') as data_file:
    content = data_file.read()

print(content)