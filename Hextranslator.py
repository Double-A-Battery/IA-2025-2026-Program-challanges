NumLetter = ["A","B","C","D","E","F"]
related = [10,11,12,13,14,15]
Phrase = input("Enter your number here: ")
choice = int(input("type 1 for TRANSLATE TO or type 2 for TRANSLATE FROM: "))
segment = []
HexTranslated = []
translated =[]
LetterFormat = ""
hexvalues = []
calcressult = []
finalresult = 0
valid = False
funny = 0
#funny math thing 16^0 is 1 so gets ignored
i = -1
#convert to hex
if choice == 1:
    Phrase = int(Phrase)
    # Calculate the place values
    while not valid:
        total = 0
        i += 1
        hexvalues.append(1 * (16 ** i))
        HexTranslated.append("")
        for k in range(len(hexvalues)):
            # Add total place values by max value to see if the place values are big enough
            total += hexvalues[k]
            if total > Phrase:
                valid = True
                break
    # Make the hexvalues array "aligned"
    hexvalues.reverse()
    print(hexvalues)

    # Once we have place values, we can start multiplying and adding
    total = 0
    # CROSSING ARRAY WITH FOR RANGE VALUES
    for k in range(len(hexvalues)):
        for j in range(16):
            if (Phrase - total) < hexvalues[k] * j:
                HexTranslated[k] = max(0, j - 1)
                total += hexvalues[k] * max(0, j - 1)
                print(HexTranslated)
                break
    # Convert numbers to letters
    for i in range(len(HexTranslated)):
        found = False
        for j in range(6):
            if related[j] == HexTranslated[i]:
                LetterFormat += NumLetter[j]
                found = True
                break
        if not found and HexTranslated[i] != 0:
            LetterFormat += str(HexTranslated[i])
    print(LetterFormat)


#Convert from hex
if choice == 2:
    #divide up phrase into its digits
    for i in range(len(Phrase)):
        segment.append(Phrase[i])
        #assign place values
    for i in range(len(Phrase)):
        hexvalues.append(1*16**(len(Phrase)-i-1))
    #convert letters into numbers ALSO MORE IJ SPAM
    for i in range(len(Phrase)):
        for j in range(6):
            if NumLetter[j-1] == segment[i-1]:
                translated = (j+9)
                segment[i-1] = translated
    #multiply each number by its multiplier and add together
    for i in range(len(Phrase)):
        finalresult += int(segment[i-1])*hexvalues[i-1]
    print(finalresult)