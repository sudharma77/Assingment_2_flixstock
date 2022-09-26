import numpy as np

arr = np.array([[0,0,0,0,0],
				[0,3,0,5,0],
                [0,0,0,0,0],
                [0,8,0,3,0],
                [0,0,0,0,0]])

first_non_zero_row = 0
last_non_zero_row = 0
first_non_zero_col = 0
last_non_zero_col = 0

i = 0
for x in arr:
  s = np.sum(x)
  if(s > 0 and first_non_zero_row == 0):
  	first_non_zero_row = i
  if(s > 0):
  	last_non_zero_row = i
  i=i+1	
  
trans = arr.transpose()
  
i = 0
for x in trans:
  s = np.sum(x)
  if(s > 0 and first_non_zero_col == 0):
  	first_non_zero_col = i
  if(s > 0):
  	last_non_zero_col = i
  i=i+1	
x = first_non_zero_row 
y = first_non_zero_col
height = last_non_zero_row - first_non_zero_row + 1
width = last_non_zero_col - first_non_zero_col + 1
print(x," ",y," ",height," ",width)
#sudharma kumar