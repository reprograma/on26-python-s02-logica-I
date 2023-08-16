
def do_sum(x,y,z):
    sum = (x+y+z)
    return sum

value1= int(input('to type the first value'))
value2= float(input('to type the second value'))
value3= int(input('to type the third value'))

final_solver = do_sum(value1, value2, value3)
print(f'the sum of the three values is {final_solver}')