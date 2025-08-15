#3
#WRITE A PYTHON FUNCTION using FILTER() THAT RETURNS A LIST OF ALL THE EVEN NUMBERS FROM A GIVEN LIST OF INTEGERE
# numbers =[1,2,3,4,5,6,]

def filtering_array_list (arr):
 for number in arr:
  if(number % 2==0):
   number+1
   return arr[number];
  
numbers_array =[1,2,3,4,5,6,]
result=[filter(filtering_array_list, numbers_array)]
print(filtering_array_list(numbers_array))
