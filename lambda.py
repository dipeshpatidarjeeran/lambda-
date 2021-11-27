#lambda function = anonymous function
#lambda arguments : expression
x = lambda t : t * 45 # lambda function input:output
 
print(x(2)) 

trd = lambda a , b : a + b     # more then argument and  return the value 

print(trd(25,25))

std = lambda a ,b , c , d : a * b - c / d #summarize argument a b c return the value

print(std(5,4,15,3))

def dip(n):
    return lambda a : a * n

mydip = dip(5)
print(mydip(15))
