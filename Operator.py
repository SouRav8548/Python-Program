#  Boolean Operations — and, or, not

#  Comparison Operators — ==, !=, >, <, >=, <=
#  Assignment Operators — =, +=, -=, *=, /=, //=, **=, %=
#  Arithmetic Operators — +, -, *, /, //, **, %
#  Bitwise Operators — &, |, ^, ~, <<, >>
#  Identity Operators — is, is not
#  Membership Operators — in, not in
#  Logical Operators — and, or, not
#  Operator Precedence
#  Operator Associativity
#  Operator Overloading
#  Operator Precedence
#  Operator precedence determines the order in which operators are evaluated in an expression.

x = 10
y = 5

print(x==5 or y==5)
print(x==10 and y==5)
print(not x==5)
print("-------------------------------")
print(x > 5)
print(x < 5)
print(x >= 10)
print(x <= 10)



# Numeric Types — int, float, complex

x = 10
y = 3.14
z = 2 + 3j

print(type(x))
print(type(y))
print(type(z))

x = 5 * abs(y)
print(abs(y))