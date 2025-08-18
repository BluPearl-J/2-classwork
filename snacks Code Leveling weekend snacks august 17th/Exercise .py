#Using reduce() and map(), find the product 
#of the squares of numbers [1, 2, 3, 4].

SOLVE2 2 2 COMPLETE TESTSS


product=1;

list(map(lambda element: element*product, reduce(lambda x: x **2 , numbers)))
#pg xx textbook
#In [9]: list(map(lambda x: x ** 2,filter(lambda x: x % 2 != 0, numbers)))

#