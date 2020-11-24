# fh=open("mike awfr.txt", "w")
# fh.write("hello friend")
# fh.close()
# fh.write("wiwnner")


# file = open('C:/Users/stonner/Desktop/folder/folder1/folder2/folder3/nn.txt.txt', 'r')
# file.readlines()


# with open('new_file.txt', 'w') as new_file:
#     new_file.write("hey there")

# new_file = open("new_file.txt")
# # line = new_file.read()
# # print(line[0:10])

# #lines starting with G
# # for line in new_file:
# #     if line.startswith("g"):
# #         print(line)

# #find function
# for line in new_file:
#     line = line.rstrip()
#     if line.find("g")==-1:
#         continue
#     print(line)

Open = input("Enter the file name: ")
new_file = open("new_file.txt")
count = 0
for line in new_file:
    if line.startswith("du"):
        count + 1
print(f"there were {count} subject lines in {new_file}")
