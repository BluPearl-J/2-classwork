#WRITE A PYTHON FUNCTION THAT CONVERTS A LIST OF STRINGS TO THEIR CORRESPONDING LENGTHS USING MAP() FUNCTION


#words=["apple", "banana","cherry"]
#output:[5,6]

def get_length_array (arr):
 for element in arr:
  print(len(element))
#example
words=["apple", "banana","cherry"]
get_length_array(words)
