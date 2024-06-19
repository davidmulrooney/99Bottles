bottles = 99
for i in range(bottles, 0, -1):
  print(f"{i} bottles of milk on the wall, {i} bottles of milk.")
  print("Take one down, pass it around,")
  if i == 1:
    print(f"{i} bottle of milk on the wall.")
  else:
    print(f"{i-1} bottles of milk on the wall.")

print("There are no more bottles of milk on the wall.")