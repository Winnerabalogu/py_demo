# import sys
#find the index of a value
# print(name.find("weda"))
# print(name.replace("weda", "weather"))
#create / open a file

# text_file = open("test.txt", "wb")
# text_file.write(bytes("ill get ther soon\n" 'UTF-8'))
# text_in_file = text_file.read()
# print(text_in_file)

name = ('david coldshot\n''ayo ogunbiyi\n''celestine sniper\n')

names = input(':')

with open('names.txt', 'r') as students:
    val = students.readlines()
    for i in val:
        if names in i:
            full_name = i
        
print(full_name.strip('\n'))


    

      