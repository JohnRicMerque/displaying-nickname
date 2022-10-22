# Assignment 1:
# Create a program that will print your nickname using only asterisk character (*)
# Example:

def makeLetterAsteriskList (letter):
    charList = []
    for row in range(5):    
        innerList = []
        for col in range(5):

            # condition reference
            J = (col == 4 or row == 4  or (row == 3 and col == 0))
            O = ((row == 0 or row==4) and (col != 0 and col != 4)) or ((col == 0 or col==4) and (row != 0 and row != 4))
            H = col == 0 or col == 4 or row == 2
            N = col == 0 or col == 4 or (row == col)

            if letter == "J":
                condition = J
            elif letter == "O":
                condition = O
            elif letter == "H":
                condition = H
            elif letter == "N":
                condition = N

            if condition:
                innerList.append("*")
            else:
                innerList.append(" ")
        charList.append(innerList)
    return charList

# make asterisk lists for each character
charJ = makeLetterAsteriskList("J")
charO = makeLetterAsteriskList("O")
charH = makeLetterAsteriskList("H")
charN = makeLetterAsteriskList("N")

# print loop for each characters list
for row in range(5):
    for col in range(5):
        print(charJ[row][col], end=" ")
    for col in range(5):
        print(charO[row][col], end=" ")
    for col in range(5):
        print(charH[row][col], end=" ")
    for col in range(5):
        print(charN[row][col], end=" ")
    print("")

