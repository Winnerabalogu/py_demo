# import sys
import pickle

Atm = input("Do you Wish to withdraw or deposit? ")
if Atm == 'withdraw':
    
    with open('wallet.txt') as inputs:
       Balance = inputs.read()
    amount=int(input("How much do you wish to withdraw?"))
    Current_balance = int(Balance) - amount
    print(f'{Current_balance} is your avalable balance')
    if amount > int(Balance):
        print('insuffient balance')
elif Atm == 'deposit':
    with open('wallet.txt','r') as inputs:
        balance = inputs.read()        
    amount =input("How much do you wish to Deposit: ")
    Current_balance = balance + amount
    print('%s is your avalable balance'%Current_balance)
# eldeposit

# with open('wallet.txt','w')as inputs:
#     inputs.write(str(Current_balance))