
#4. Given prices = [100, 200, 300], use 
#map() to add 10% tax to each price

# list(map(lambda x: x+10%,argument2)))

#map must have at least two arguments

prices = [100, 200, 300]
DISCOUNT=0.1

tax = list(map(lambda element:element+0.1 , prices))
print("10% tax or 0.1tax added is:", tax)
