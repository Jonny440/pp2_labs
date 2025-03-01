import os
path = "/Users/Z1/Desktop/pp2_labs"
#1
# def listDirs(path):
#     dirs = []
#     for dir in os.listdir(path):
#         if os.path.isdir(f"{path}/{dir}"):
#             dirs.append(dir)
#     return dirs
# def listFiles(path):
#     files = []
#     for dir in os.listdir(path):
#         if os.path.isfile(f"{path}/{dir}"):
#             files.append(dir)
#     return files
# def ls(path):
#     return [file for file in os.listdir(path)]
# print(listDirs(path))
# print(listFiles(path))
# print(ls(path))

#2
# def isReadeable(path):
#     return os.access(path, os.R_OK)
# def isWritable(path):
#     return os.access(path, os.W_OK)
# def isExecutable(path):
#     return os.access(path, os.EX_OK)
# def doesExist(path):
#     return os.path.exists(path)
# isReadeable(path)
# isExecutable(path)
# doesExist(path)
# isWritable(path)

#3
# if os.path.exists(path):
#     print(f"Directory name: {os.path.dirname(path)}")
#     print(f"File name: {os.path.basename(path)}")

#4
# path = f"{path}/_chat.txt"
# file = open(path, "r")
# lineCount = len(file.readlines())
# file.close()
# print(lineCount)

#5
# path = f"{path}/_chat.txt"
# array = ["Helo", "My", "name", "is Jontfds"]
# file = open(path, "a")
# file.write(" ".join(array))
# file.close()

# file = open(path, "r")
# print(file.read())
# file.close()

#6
# for letter in (chr(i) for i in range(65, 91)):  # ASCII 65-90 are 'A'-'Z'
#     file = open(f"{path}/{letter}.txt", "x")
#     file.close()
# for dir in os.listdir(path):
#     if os.path.isfile(f"{path}/{dir}"):
#         print(dir)

#7
# file = open(f"{path}/_chat.txt", "r")
# txt = file.read()
# secondFile = open(f"{path}/A.txt", "w")
# secondFile.write(txt)

#8
# for letter in (chr(i) for i in range(65, 91)):
#     new_path = f"{path}/{letter}.txt"
#     if os.path.exists(new_path):
#         os.remove(new_path)