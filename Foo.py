from random import sample

letters = ("A", "B", "C", "D","E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
           "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

generated_password = sample(letters, 5) + sample(numbers, 4)

for i in generated_password:
    print(i, end = "")