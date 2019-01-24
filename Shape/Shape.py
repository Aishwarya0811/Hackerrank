
## The input to the script is separated by space. 
##The split function will use space as a delimiter and get all the inputs separately as a list.
##Then you end up with characters which you must convert to integers. 
##You do that by mapping the function int.
##Input Function lets you ask a user for some text input.
##Then you just convert it to a list.
import numpy as np
array = np.array(list(map(int, input().split())))
print(array.reshape(3, 3))
