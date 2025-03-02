#declare variables
List = input("Enter a list of numbers separated by commas: ")
index = 0
Numbers = []

#Seperating input into an array of numbers
for i in range(len(List)):
    if List[i] == ",":
        Numbers.append(List[index:i])
        index = i+1
    if i == len(List)-1:
        Numbers.append(List[index:i+1])

#using array to form an output of "*"s the length of the number
for i in range(len(Numbers)):
    placehold = ""
    for j in range(int(Numbers[i])):
        placehold += "*"
    print(placehold)
