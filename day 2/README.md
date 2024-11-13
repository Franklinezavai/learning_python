# Arithmeticall operations
  The arithmeticall operations are basic mathematics perfomed in the order of parenthisis,exponentiation, multiplication and division, addition and subtraction.

## parenthisis - ( )  usually first priority
  a = (2 + 3) * 4
  print(a)
  output: 20

## exponentiation - ** usually second priority
  c = 2 ** 3
  print(c)
  output: 8

## multiplication  - *  usually third priority
  d = 2 * 3
  print(d)
  output: 6

## division - /  usually third priority
   e = 6 / 3
   print(e)
   output: 2.0

## addition - +  usually fourth priority
  f = 2 + 3
  print(f)
  output: 5

## subtraction - -  usually fifth priority
  g = 5 - 3
  print(g)
  output: 2

# Comparison operators
  They are used to compare two values and return a preffered output

## equal to - == used to check if two values are equal
  a = 2
  b = 2
  if a == b:
  print("a is equal to b")
  output: a is equal to b

## not equal to - != used to check if two values are not equal
  a = 2
  b = 3
  if a != b:
  print("a is not equal to b")
  output: a is not equal to b

## greater than - > used to check if one value is greater than another
  a = 5
  b = 3
  if a > b:
  print("a is greater than b")
  output: a is not greater than b

## less than - < used to check if one value is less than another
  a = 7
  b = 11
  if a < b:
  print("a is less than b")
  output: a is less than b

# conditional statements
  they give a preffered output based on a set of conditions

## if statement
  if a > b:
  print("a is greater than b")
  output: a is greater than b

   ## else statement
   else a < b:
    print("a is less than b")
    output: a is less than b
   
   ## elif - if the above conditions are not meet
      print("a and b are incompatible")

# logical operators
 They are used to combine conditional statements

 ## and - used to check if both conditions are true
    a = 5
    b = 3
    fabian_age = 34
    if a > b and fabian_age == 34:
      print("a is greater than b and fabian is 34 years old")
      output: a is greater than b and fabian is 34 years old

## or - used to check if any of the condition is true
    a = 5
    b = 3
    fabian_age = 34
    if a > b or fabian_age == 34:
      print("a is greater than b or fabian is 34 years old")
      output: a is greater than b or fabian is 34 years old

## not - if one of the combined conditions is false the entire statement is False
    a = 1
    b = 3
    fabian_age = 34
    if not a > b and fabian_age == 34:
      print("access denied")
      output: access denied
    







