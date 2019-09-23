'''
Wayne O'Sullivan R00064536
In my main function i have nested while loops for requesting user input for a sentence, a word within that sentence and
a second word to replace the first word input from the user. The validation catches an empty input for the sentence and
both words. I use if (not in) sentence to catch a word that is not present from the original sentence and print an
error message. If it passes all these then my function switchinWords is invoked with the 3 inputs from the user.
For the switchingWords function i split the sentence into an array using .split() create an empty variable result. For
loop through the array and for each element i in the array, if i == to the first word parameter then make it equal to
the value of the second word.
'''


def switchingWords(sentence, word1, word2):
    sentence2 = sentence.split()
    result = ""
    for i in sentence2:
        if i == word1:
            i = word2
        result += i + " "

    return result.strip()


def main():
    loop = True
    while loop:
        sentence = input("Please enter a sentence >>> \t")
        if sentence == "":
            print("Please enter a valid sentence !!!")
        else:
            while loop:
                word1 = input("Please enter the word you'd like to replace >>>\t")
                if word1 == "":
                    print("Please enter a valid word !!!")
                elif word1.strip() not in sentence:
                    print("Sorry word not in sentence")
                elif word1 != "":
                    while loop:
                        word2 = input("Please enter your replacement word >>>\t")
                        if word2 == "":
                            print("Please enter a valid word !!!")
                        elif word2 != "":
                            newSentence = switchingWords(sentence, word1, word2)
                            print("Original sentence ", sentence)
                            print("New sentence ", newSentence)
                            loop = False


main()
