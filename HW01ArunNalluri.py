""" this is a program that lets you play Rock Paper Scissors with the computer With Dictionaries! """

from random import choice
def winner(human):
    """ this function decides and prints the winner and returns the fuction to main"""
    PC = choice(['R', 'P', 'S'])
    FullName = {'R':'Rock','P':'Paper','S':'Scissors'}
    dic = {'R':'S','P':'R','S':'P'}
    if(PC==human):
        print("Tie: we both chose "+FullName[human])        
    elif(dic[PC]==human):
          print(FullName[PC]+" beats "+FullName[human]+ " : I Win!!")
    elif(dic[human]==PC):
          print(FullName[human]+" beats "+FullName[PC]+" : You Win!!")
    return


print("Hello welcome to first assignment Rock Paper scissors")
val = input("Enter your choice R for Rock P for Paper S for scissors Q if you want to quit")
val = val.upper()

while val != 'Q':
    if val in ['R','S','P']:
        winner(val)
       
    else:
        print('You have selected a invalid choice please try again')
        
    val = input("Enter your choice R for Rock P for Paper S for scissors Q if you want to quit")
    val = val.upper()
    

print("Thanks for playing! have a good day")
