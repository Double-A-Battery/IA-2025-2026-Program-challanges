def menu():
    word = input("write the word/phrase you want to translate ")
    type = input("do you want to translate TO pig latin or FROM pig latin ")
    if type == "from" or type == "From" or type == "FROM" or type == "F" or type == "f":
        translate(False,word)
    elif type == "to" or type == "To" or type == "TO" or type == "T" or type == "t":
        translate(True,word)
    else:
        print("Invalid input")
        menu()

def wordcheck(word):
    split = []
    fullword = ""
    for i in range(len(word)):
        if word[i] == " ":
            split.append(fullword)
            fullword = ""
        else:
            fullword = fullword + word[i]
    split.append(fullword)
    return split

def translate(check,word):
    split = wordcheck(word)
    translation = ""
    if check == True:
        for i in range(len(split)):
            currentword = ""
            for j in range(len(split[i])+1):
                if j == 0:
                    hold = split[i][j]
                elif j == len(split[i]):
                    if hold == "a" or hold == "e" or hold == "i" or hold == "o" or hold == "u" or hold == "y":
                        translation = translation + currentword + hold + "yay "
                    else:
                        translation = translation + currentword + hold + "ay "
                else:
                    currentword = currentword + split[i][j]
        print(translation)

    if check == False:
        for i in range(len(split)):
            currentword = ""
            for j in range(len(split[i])-1):
                if split[i][j] == "a" and split[i][j+1] == "y" and j == len(split[i])-2:
                    if split[i][j-1] == "y":
                        hold = split[i][len(split[i])-4]
                        split[i] = split[i][0:len(split[i])-4]
                        split[i] = hold + split[i]
                    else:
                        hold = split[i][len(split[i])-3]
                        split[i] = split[i][0:len(split[i])-3]
                        split[i] = hold + split[i]
        final = ""
        for i in range(len(split)):
            final = final + split[i] + " "
        print(final)
menu()