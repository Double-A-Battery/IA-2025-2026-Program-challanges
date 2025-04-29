user_input = int(input("Enter a number to convert to binary or denary: "))
choice = int(input("Type 1 for TRANSLATE TO or type 2 for TRANSLATE FROM: "))
BinPlaces = []
BinaryNum = []
Finished = ""
total = 0

if choice == 1:
    #DENARY TO BINARY
    result = 1
    i = 0
    maxvalue = 0
    while 2 ** i <= user_input:
        BinPlaces.append(2 ** i)
        i += 1
    BinPlaces.reverse()
    #finding the binary places
    for i in range(len(BinPlaces)):
        if user_input >= BinPlaces[i]:
            BinaryNum.append(1)
            user_input -= BinPlaces[i]
        else:
            BinaryNum.append(0)
    for i in range (len(BinaryNum)):
        Finished += str(BinaryNum[i])
    #converting the binary list to a string
    print("The binary value is: ", Finished)


if choice == 2:
    #BINARY TO DENARY
    NumString = str(user_input)
    PlaceLength = len(str(user_input))
    for i in range(PlaceLength):
        BinPlaces.append(2 ** i)
        #setting the binary place values
    BinPlaces.reverse()
    for i in range(PlaceLength):
        total += int(NumString[i]) * BinPlaces[i]
    print("The denary value is: " + str(total))
