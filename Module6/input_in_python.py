#string input

"""my_name = input("Enter your name: ")
print(my_name)

random_number_inp = int(input("Enter a number: "))
print(random_number_inp)
print(type(my_name), type(random_number_inp))
"""
#multiple inputs
a, b, c = map(int, input("Enter 3 numbers: ").split())
#print(a,c,b)

#L = list(map(int, input("enter numbers: ").split()))
#print(L)

print(a,b,c, sep='|', end=' ')
print("hello")