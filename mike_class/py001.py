# # print("\tlogin")
# # uname = input("username:")
# # password = input("password:")

# # if uname.lower()=="jerry" and password=="1234":
# #     print("Login Successful")
# # else:
# #     print("Invalid Username or Password")
# # temprature conversion from cel to fah
# # name = input("Enter your name:")
# # cel =float(input("Enter your temperature{c*}: "))
# # fah=cel* 8/5 + 32 #formular for conversion
# # temperature =(f"{name}, Your Temperature in fah {fah}f.")
# # print(temperature)

# # name= input("Enter you name: ")
# # # print(f" Hello {name}")


# # write a program thats accepts the name, number of hours worked a day and display the wages of the person.

# # write a program that takes in the sides of a rectangle and display its area and perimeter. 

# # name=input("Enter your name: ")
# # hrs= float(input("Enter hours worked: "))
# # rate=20*hrs
# # wage=(f"You've earned {rate}$. ") 
# # print(wage)

# # lenght=float(input("Enter the lenght of the rectangle{cm}: "))
# # breadth=float(input("Enter the breadth of the rectangle{cm}: "))
# # area=lenght*breadth
# # perimeter=2*lenght + 2*breadth
# # solution=(f"The Area is {area}cm and the Perimeter is {perimeter}cm.")
# # print(solution)

# # sex = input("Enter Your Gender: ")
# # Maritalstatus = input("Single or Married?: ")
# # Age = int(input("Enter Your Age: "))

# # if sex.lower() == "female" or sex.upper() == "female" and Maritalstatus.lower() == Maritalstatus.upper() :
# #     print("She is allowed to work in the urban area. \n")

# # if sex.lower() == "male" or sex.upper() == "male" and Maritalstatus.lower() == Maritalstatus.upper() :
# #     if Age >= 20 and Age <= 40:
# #         print("He will work in the urban area")
# #     elif Age>= 40 and Age <=60:
# #         print ("He will work in the urban area and others ")
# #     else:
# #         print("error!!")

# # sex = input("Enter Your Gender: ")
# # Maritalstatus = input("Single or Married?: ")
# # Age = int(input("Enter Your Age: "))

# # num = int(input("Enter a number: "))
# # num2 = int(input("Enter another number: "))
# # if num > num2:
# #     print(f" {num}, is the larger number.")
# # else:
# #     print(f" {num2}, is the larger number")

# # user = input("Enter Your Company ID: ")
# # Salary= int(input("Enter your monthly wage: "))
# # totalprofit = int((Salary * 0.05))
# # service = int(input("Enter Your total years of service: "))
# # if service >= 5:
# #     print(f"The Company has decided to give you {totalprofit} bonus in addition to your salary.")
# # else:
# #     print("You have not reached the target.")

# # num1 = int(input("Enter a number: "))
# # num2 = int(input("Enter a second number: "))
# # num3 = int(input("Enter a third number: "))
# # print(max(num1, num2, num3))

# # print('Enter to the X-mall')
# # custormer = input("Enter Your name Sir/Ma:")
# # print(f'Welcome {custormer}')
# # print(f'Select a category;\n(1)Phone\n(2)Cars\n(3)Clothes')
# # Select = input("Where would you shop from?: ")
# # if Select.lower()=="phone" or Select.lower()=="1":
# #     print(f"select brand;\nSamsung\nIphone")
# #     select_phone = input("Which Brand would you Purchase from?: ")
# #     if select_phone.lower() =="samsung":
# #         print(f'what series would you purchase from?;\n Sseries\n Jseries:')
# #         select_phone_series = input("Select a series.: ")
# #         if select_phone_series.lower()=="sseries":
# #             print('How many would you like to purchase? ')
# #             qty = int(input("How many will you Like to purchase?:"))
# #             price = qty * 120000
# #             print(f'Mr/Mrs{custormer} your purchase of {select_phone}{select_phone_series} is sucessful and your bill is {price}. Thank for shopping with us.')



# # print('Hello user')
# # user= input("Enter Your Name: ")
# # time = float(input('Enter the Time: '))

# # if time >= 0 and time <=12:
# #     print (f'Good morning {user}')
# # elif time >= 13 and time <=16:
# #     print (f'Good Afternoon {user}')
# # elif time >=17 and time <=20:
# #     print (f'Good Evening {user}')
# # elif time >=21 and time <=24:
# #     print (f'Good Night {user}')
# # else:
# #     print('Wrong input')

# # num = int(input("Guess a number above Zero:"))
# # score = 0
# # if num > 0:
# #     print("number is positive")
# #     score += 1
# #     sign = input("Guess a sign: ")
# #     if sign == '+' or sign =='-' or sign == '/':
# #         print("You Passed the second level")
# #         score += 1 
# #         y = int(input("Enter another number: "))
# #         if y == 5:
# #             print ("You passed the final level")
# #             score += 1
# # print(f"Your total score is {score}")
# # d_student = {
# #     'name': 'Role Smith',
# #     'grades': [70, 80, 90, 99]
# # }

# # def average_grade(student):
# #    return sum(student['grades'])/len(student['grades'])
# # print (average_grade(d_student))



# def check_status(grade):
#     if grade >= 50:
#         print('Your are above avarage')
#     else:
#         print('You failed you Dumb Bitch!')
# check_status(int(input('Enter Your Grade:')))

# # i = 1 
# # while i <= 5:
# #     print (f'1')
# # i += 1

# # n = 2
# # while n <= 10:
# #     if n % 2 == 0:
# #         print({n})
# #         n = n + 10

# # num= int(input('Enter a number:'))
# # if num % 3 == 0 and num % 5 == 0:
# #     print('fizzbuzz')
# # elif num % 3 == 0:
# #     print('Fizz')
# # elif num % 5 == 0:
# #     print('buzz')

# # 5
# # #lenght= int(input('Enter the lenght:'))
# # # breadth = int(input('Enter the Breath'))
# # # parameter = breadth * lenght
# # # print(parameter)
# # # if breadth % 2== 0: 
# # #     print('The number is even')
# # # elif breadth % 2 != 0: 
# # #     print  ('The number is odd')

# # range(1,2,3,4,5,6,7)
# # print (range)

# a = [1,2,3,4,5,6,7,8,9]
# def even_numbers(num):
#     sum_num = 0
#     for t in num:
#         sum_num = sum_num + t
#     even_numbers = (num) % 2 == 0:

# even_numbers(a)

# # 6
# def nums():
#     nums=0
# if nums <= 20:
#     for n in nums:
#         number = number + nums
#     if nums % 2==0:
#         print(nums, "is an even number.")
#     elif nums % 3 >= 1:
#         print (nums, "is an odd number.")
#     nums = nums + 1
# else:
#     print("invalid number")



# 1
def count_letter(word, letter):
    count = 0
    for alpha in word:
        if alpha == letter:
            count +=1
    return count
count = count_letter('banana', 'a')
print (count)

# # 2
# # slicer = 'banana'
# # print (slicer[0:2])

# # def slicer (word, start, stop):
# #     x = (word[start:stop])
# #     print (x)

# # slicer ("banana",0,2)



# # # # 3
# # def started(word, letter):
# #         if word[0] == letter:
# #             return("it started with b")

# # check = started("banana","b")
# # print(check)

# # # 4
# # def avg():
# #     count = 1
# #     ask = eval(input("how many numbers: "))
# #     sum_num = 0
# #     while count <= ask:
# #         num = eval(input("enter a number: "))
# #         sum_num = sum_num + num
# #         count +=1

# 6
# # notquit = True
# # while notquit == True:
# #     text = str(input("Enter a text: "))
# #     if text.lower().__eq__ ("quit"):
# #         notquit = False
# #     else:
# #         print(text, end=",")


# # i = 1
# # a = 100
# # while 1 <= 100:
# #     if 1 % 2 == 0:
# #         print (i, "is even.")
# #     elif i % 2 == 1:
# #         print (i , "is odd.")
# #     elif i % 3 >= 1:
# #         print (n, "is a prime number.")
# #     i = i +1

 
# # user_name = input("Enter Name: ")
# # num_test = int(input("Hom man test?\n: "))
# # if num_test <= 2:
# #     print ('Too Small')
# # else :
# #     sum = 0
# #     count = 1
# #     while count <= num_test:
# #         score = int(input('Enter Score: '))
# #         sum += score
# #         choose= (input('Type STOP to stop'))
# #         if choose.lower() = 'stop':
# #             break
# #     avg = sum/count
# #     print(f'{avg} is the average') 


# # while True:
# #     line = input("Enter name:")
# #     if line == 'done':
# #         break
# #     else:
# #         print ("Done!")


# # while True:
# #     line = input("Enter a name: ")
# #     if line.lower() == "Done":
# #         break
# #     else:
# #         print (line.lower())

# # while True:
# #     text = input(">")
# #     if text.lower == 'Quit':
# #         break
# #     elif text.lower == 'Tired':
# #         continue
# #     else:
# #         print (text)
# # else:
# #     print("This loop is Done!!!")


# # word = "P-y-t-h-o-n -p-r-o"
# # i = 0
# # c = 20
# # while i < c:
# #     i += 1
# #     if i % 2 == 0:
# #         continue
# #     else:
# #         print(i)


# word = "P-y-t-h-o-n -p-r-o"
# for i in word:
#     if i == "-":
#         continue
#     print (i)



# friends = 'a','b', 'c','d', 'e'

# for friend in friends:

#     print (f"Hello MF {friends}") 



# friends = ['a','b', 'c','d', 'e']
# for friend in friends:

#     if friends.index (friend) % 2 != 0:
#         continue
#     else:
#         print (f'Hello {friend}') 

























