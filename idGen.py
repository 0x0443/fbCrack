import random, sys

original_stdout = sys.stdout
noz = int(input("\nEnter the number of zeros: "))
ids = int(input("Enter the number of IDs: "))
r1  = int("1"*(14-noz))
r2  = int("9"*(14-noz))
print("\n")
def result():
  [print(str("1"+"0"*noz)+str(random.randrange(r1, r2))) for _ in range(ids)]
with open('ids.txt', 'w+') as i:
  sys.stdout = i
  result()
  sys.stdout = original_stdout
  i.seek(0)
  print(i.read())
  print("Saved IDs in ids.txt.")
