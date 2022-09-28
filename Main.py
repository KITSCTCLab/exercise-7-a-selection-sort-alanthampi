from typing import List

def selectionSort(array,size) ->List[int]:
  for i in range(size):
    min = i
    for j in range(i+1,size):
      if array[j]<array[min]:
        min = j
    array[i],array[min] = array[min],array[i]
  return array


input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
