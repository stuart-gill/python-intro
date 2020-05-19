
age = input("how old are you? ")

if age:
  age = int(age)
  if age >=21:
    print("ok normal entry")
  elif age < 18:
    print("too young, sorry!")
  else:
    print("you can come in but no drinks!")
else:
  print('invalid input')

# doesn't handle improper input... comes in as str, convert to int-- how to determine if str is a str representation of an int without trying to conver to int, which causes an error if str doesn't represent an int?
