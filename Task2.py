'''
Wayne O'Sullivan R00064536
For the randomremove function i create a copy of the list passed into the function using copy.copy(). I set my new list
equal to the list argument to be appended. I used a for loop in the range of the num argument passed into the function.
I then create a variable v using random.randint() between 2 and 5, pop that variable v from the list i then set the
contents of the new list equal to the tuple(myList). Use a print statement then to display the new edited list as a
tuple and the original list.
For the user input i want 12 input strings so i created an empty array and run a while loop until at least 12 inputs
have been added to the array that array is then returned for the randomremove function.
My numpicker function requests the user to choose a number between 2 and 6 and if the value is greater than 6 or less
than 2 it prints an error message. If a non integer is input the except ValueError catches that
'''

import random
import copy


def userinput():
    mylist = []
    while True:
        print("Please enter input number " + str(len(mylist) + 1) + " or enter to quit adding after twelve inputs")
        word = input()
        if word == "" and len(mylist) + 1 <= 12:
            print("Please enter something to add to list !!")
        elif word == "" and len(mylist) + 1 >= 12:
            break
        else:
            mylist = mylist + [word]
            # myList.append(word)
    return mylist


def numpicker():
    while True:
        num = input("Please choose a number between 2 and 6 >>")
        try:
            val = int(num)
            if val < 2 or val > 6:
                print("Please select a number between 2 and 6!! ")
            else:
                break
        except ValueError:
            print("Please enter an integer!! ")
    return val


def randomremove(mylist, num):
    oldlist = copy.copy(mylist)
    newlist = mylist
    for i in range(num):
        v = random.randint(2, 5)
        mylist.pop(v)
        newlist = tuple(mylist)
        type(newlist)
    print(str(num) + " items were deleted from the list: ")
    print("New Tuple >>>", newlist)
    print("Original List >>> ", oldlist)


def main():
    mylist = userinput()
    num = numpicker()
    randomremove(mylist, num)


main()
