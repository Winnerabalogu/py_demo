# try: open('not.txt')

# except: 
#     print("The file dosen't exist")
# try:
#     a = int(input('enter a number: '))

# except:
#     print('E dey Okay')

# try: 
#     list = []
#     count = 0
#     while count < 10:
#         number = int(input('Enter the number: '))
#         list.append(number)
#         count += 1
#     avg = sum(list)/ len(list)
#     print(avg)
# except:
#     print("I can't kill my self")


# try:
#     open('new_file.txt')
    
# except:
#     new_file = open('new_file.txt', 'w')
#     new_file.write('This is a new file')

try:
    new_user = input("Do you want to open a new file y/n?: ")
    if new_user == "y":
        new_user = open('new_user.txt', 'w')
        new_user.write('')
        new_user.close()
    else:
        old_user = input('Enter your already existing file name: ')
        open(old_user)
