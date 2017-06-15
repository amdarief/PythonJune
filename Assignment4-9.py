
inputword = input("Input a word to reverse: ")

for char in range(len(inputword) - 1, -1, -1):
  print(inputword[char], end="")
print("\n")