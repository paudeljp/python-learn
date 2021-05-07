a = int(input("Enter a number"))
b = int(input("Enter a number"))
c = int(input("Enter a number"))

if (a == b == c):
  print ("all are equale")
elif (a == b) | (a == c) | (b == c):
  print ("Two are equale")
  if (a == b) :
    print ("a and b are equal")
  elif (a == c) :
    print ("a and c are equal")
  else:
    print ("b and c are equal")
else:
  print ("not equal")