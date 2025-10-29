# There are three numeric types in Python:

# int
# float
# complex
# Variables of numeric types are created when you assign a value to them:


x = 50;
y = 5.03;
z = 1j;

print(type(x));
print(type(y));
print(type(z));

gg = 1E65;
print(type(gg))


# Number converstion

x = 2;
y = 3.2;
z = 3j ;
print(x);
print(y);
print(z);

a = float(x);
b = complex(y);

print(a);
print(b);


import random

print(random.randrange(-273,10000));