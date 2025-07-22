# Given integer n between 1 and 7 inclusive . print name of day of week corresponding to number 
# eg monday = 1 input n = 5 outpit friday


MONDAY = 1 

TUESDAY = 2

WEDNESDAY = 3

THURSDAY = 4

FRIDAY = 5

SATURDAY = 6
SUNDAY = 7 

n = int( input ("Enter any number from one to SEVEN"));
print  ("your input integer is number", n )


if n == 1 :
    print("DAY: MONDAY")
elif   n == 2 :
    print("DAY: TUESDAY")
elif n == 3:
    print("DAY: WEDNESDAY")
elif n == 4:
    print("DAY: THURSDAY")
elif n == 5:
    print("DAY: FRIDAY")
elif n == 6:
    print("DAY: SATURDAY")
elif n == 7:
    print("DAY: SUNDAY")
else:
    print ("ERROR INPUT ONLY NOS FROM ONE TO 7 SEVEN")
















