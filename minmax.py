# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below. 
# From U Michigan python course

largest = None
smallest = None
while True:
  num = input("Enter a number: ")
  try:
    n = int(num)
  except:
    if num == "done" : break
    else: 
      print("Invalid input")
      continue
  if largest is None: 
    largest = n
    smallest = n
  else:
    if n > largest: largest = n
    elif n < smallest: smallest = n

print("Maximum is", largest)
print("Minimum is", smallest)
