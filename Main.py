from typing import List

def selectionSort(array,size) ->List[int]:
  for i in range(size):
    minim = i
    for j in range(i+1,size):
      if array[j]<array[minim]:
        minim = j
    array[i],array[minim] = array[minim],array[i]
  return array


input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
