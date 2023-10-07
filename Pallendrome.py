num = 1234321

string = str(num)

NewString = string[2]+string[1]+string[0]

NewNum = int(NewString)

if NewNum == num:   
    print("The number is a pallendrome!")
else:
    print("The number is not a pallendrome")
