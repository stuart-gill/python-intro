print("How many times to I have to tell you to clean up your room? ")
times = input()
times = int(times)

for num in range(times):
  print("CLEAN UP YOUR ROOM!")
  if num > 10:
    print("geez this is just too much")
    break
