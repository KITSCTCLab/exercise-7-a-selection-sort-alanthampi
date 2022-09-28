from typing import List

def selectionSort(array, size) -> List[int]:
    for i in range(0,size-2):
        minim = i
        for j in range(1,size-1):
            if array[minim]>array[j]:
                minim = j
        temp = array[i]
        array[i] = array[j]
        array[j]=temp
                
                
    return array
    

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
