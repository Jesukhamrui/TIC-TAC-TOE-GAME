# Program 1
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

result = str1 + str2
print("Concatenated String:", result)
# Program 2
text = input("Enter a string: ")
new_text = text.replace("  ", " ")
print("After removing double spaces:", new_text)
# Program 3
sentence = "Welcome to Python Programming"
substring = sentence[11:17]
print("Extracted substring:", substring)
# Program 4
s = input("Enter a string: ")
cleaned = s.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
    print("It is a palindrome!")
else:
    new_palindrome = cleaned + cleaned[::-1]
    print("Not a palindrome. Transformed:", new_palindrome)
# Program 5
value = input("Enter something: ")
print("Data type is:", type(value))
# Program 6
print("Python\nIs\nawesome!")
# Program 7
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for ch in s if ch in vowels)
print("Number of vowels:", count)
# Program 8
s = input("Enter a string: ")
new_s = s.replace("a", "@")
print("Modified string:", new_s)
# Program 9
s = input("Enter a string: ")
print("Reversed string:", s[::-1])
# Program 10
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b if b != 0 else "Undefined (division by zero)")
print("Modulus:", a % b if b != 0 else "Undefined (mod by zero)")
# Program 11
s = input("Enter a string: ")
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print("Character frequencies:", freq)
# Program 12
s = input("Enter a string: ")
print("Converted string:", s.swapcase())
# Program 13
s = input("Enter a string: ")

if s.isalnum():
    print("The string is alphanumeric.")
else:
    print("The string is NOT alphanumeric.")
