def countWord():
    fileName = input("Enter File Name: ")
    count = 0
    line = 0
    file = open(fileName,"r")
    for i in file:
        word = i.split()
        print(word)
        count = count+len(word)
        line+=1
    print("Number of Words ",count)
    print ("Number of Line ",line)
countWord()