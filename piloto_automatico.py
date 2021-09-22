traseira_a = int(input())
traseira_b = int(input())
traseira_c = int(input())

if (traseira_b - traseira_a) > (traseira_c - traseira_b):
  print("-1")
elif (traseira_b - traseira_a) < (traseira_c - traseira_b):
  print("1")
else:
  print("0")
