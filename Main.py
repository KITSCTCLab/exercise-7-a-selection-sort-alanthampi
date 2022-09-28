from typing import List

def selectionSort(array, size) -> List[int]:
 i=0
  for x in range(i,size):
    for z in range(i+1,size):
      if array[i]>array[i+1]:
        temp = array[i]
        array[i] = array[i+1]
        array[i+1] = temp
    

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
