file1 = open(input (str("Please enter the name of the file you wish to open:" )),"r")
a = input()
print('The inputted number is:', a)
with open('', 'w') as inF:
        myString = a 
        for index, line in enumerate(inF):
            if myString in line:
                print ("Search Term Found!")
                inF.write("Line %d has string: %s" % (index, line))
filename = "outputfile.txt"
myfile = open(filename)
lines = len(myfile.readlines())