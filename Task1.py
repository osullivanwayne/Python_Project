'''
Wayne O'Sullivan R00064536
For the biggest and smallest functions i created two variables an integer to track the size of an element and an
empty string as a placeholder. I then used a for loop to traverse the array check the size of the element. If that
was the biggest/smallest element then that became the item to be returned.
For tripleMyList i multiplied the array by 3 and then used a nested for loop to access any item that was greater than
four characters long within the 3 arrays.
The printMenu() just prints the menu to the console!!
The userInput() has an empty array to add strings to. It requests the user to input a string, it cannot be empty
and if the amount of strings entered is less than 8 it prints a message to the console. When the array is >= 8 then it
breaks from the while loop.
For the main function its a simple while loop that asks for user input for certain criteria to execute the above
functions B or b for biggest function, S or s for smallest function, Any positive integer for tripleMyList, E or e to
exit from loop and any other input displays an error message
'''


def biggest(myList):
    p = 0
    t = ""
    for item in myList:
        if len(item) > p:
            t = item
            p = len(item)
    return t


def smallest(myList):
    p = 1000
    t = ""
    for item in myList:
        if len(item) < p:
            t = item
            p = len(item)
    return t


def tripleMyList(myList):
    newList = [myList] * 3
    p = 0
    num = 0

    for myList in newList:
        for item in myList:
            if len(item) > 4:
                t = item
                p = p+1
                print(p, "\t", t)
                num = p
    return num


def printMenu():
    print("Menu".center(48, "="))
    print("B or b for bigger function")
    print("S or s for smaller function")
    print("Press any number for replication function")
    print("E or e to exit")
    print("================================================")


def userInput():
    myList = []
    while True:
        print("Please enter word number " + str(len(myList) + 1) + " or nothing to quit adding once 8 strings "
                                                                 "are added >>>\t")
        word = input()
        if word == "" and len(myList) + 1 >= 8:
            break
        elif word == "" and len(myList) + 1 < 8:
            print("Please enter something to add to the list >>>")
        else:
            myList = myList + [word]
    return myList


def main():
    myList2 = userInput()
    loop = True
    while loop:
        printMenu()
        choice = str(input("Enter your choice please >>> \t"))
        if choice == "B" or choice == "b":
            b = biggest(myList2)
            print("Biggest String In The List >>>", b, "\n")
        elif choice == "S" or choice == "s":
            s = smallest(myList2)
            print("Smallest String In The List >>>", s, "\n")
        elif choice.isdecimal():
            print("Replication Of Strings Greater Than Four Characters")
            num = tripleMyList(myList2)
            print("<<<", num, " items greater than four characters long>>>\n")
        elif choice == "E" or choice == "e":
            print("<<<< Goodbye Vincent >>>>")
            loop = False
        else:
            print("You know nothing John Snow follow the menu guide")


main()
