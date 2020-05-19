
# 4 and 13 are unlucky
# for all others, print odd or even 1-20

for num in range(1,21):
  status = None
  
  if num == 4 or num == 13:
    state = "UNLUCKY!"
  elif num % 2 == 0:
    state = "even"
  else:
    state = "odd"
    
  print(f"{num} is {state}")
