# def add(a, b):
#     result = a + b
#     return result
   
# result = add(1,4)
# print(result)


# def add2():
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter a number: "))
#     print(num1 + num2)
# add2()

# def guess():
#     word = input("Enter a word: ")
#     return word
# word=guess()
# if word == 'sign':
#     print("Entered the correct word")

user_dic = {}
username = input('enter a name: ')
password = int(input('enter your password in number: '))
def user_details(username, password):
    user_dic [username] = password
    return user_dic
print(user_details(username,password))
login = input('Would Like to login? yes/no: ')
if login == 'yes':
    print('Enter Your Details Below')
    name = input('Username: ')
    code = int(input('Password:'))
    if name in user_dic:
        if code in user_dic: 
            print('Welcome back')
        else:
            print('Wrong Password')
    else:
       print('wrong username')

    
    # try:
    #     if user_dic[name]:
    #         print('Welcome Back')

    # except Exception:
    #     print('incorrect username or password')
    
        
else:
    print ('Okay see you next time')


