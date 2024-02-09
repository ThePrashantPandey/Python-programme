# write a program to swap  two variable  using third variable
# solution 1

a = 10
b = 20

temp = a
print ("the value of temp is ",temp)

a = b
print ("the value of a is ",a)

b = temp
print ("the value of b is ",b)


#solution 2( without using third variable)

a = 10
b = 20

a, b = b, a 

print("The value of a is ",a)   
print("The value of b is ",b) 
