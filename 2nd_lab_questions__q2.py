from array import array
sentence="This is an Umbrella"
array=sentence.split(" ")
array.sort(key=len)
print(array)
print("Smallest Element: "+array[0])
print("Largest Element: "+array[-1])