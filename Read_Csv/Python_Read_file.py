##TO_BE_EDITED_Some_errors



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






numbers = set() # create a set for storing numbers that were already written
out = open('output', 'w') # open 'output' file for writing
for line in open('input'): # loop through each line of 'input' file
    try:
        i = int(line) # try to convert line to integer
    except ValueError:  # if conversion to integer fails display a warning
        print ("Warning: cannot convert to number string '%s'" % line.strip() )
        continue # skip to next line on error
    if i not in numbers: # check if the number wasn't already added to the set
        out.write('%d\n' % i) # write the number to the 'output' file followed by EOL
        numbers.add(i) # add number to the
