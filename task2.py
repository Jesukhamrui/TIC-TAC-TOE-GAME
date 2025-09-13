# Program 1
sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word occurrences:", word_count)

# Program 2
s = input("Enter a string: ")
compressed = ""
count = 1

for i in range(len(s)):
    if i < len(s) - 1 and s[i] == s[i+1]:
        count += 1
    else:
        compressed += s[i] + str(count)
        count = 1

print("Compressed string:", compressed)

# Program 3
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) == len(s2) and s2 in (s1+s1):
    print("Yes, it's a rotation")
else:
    print("No, it's not a rotation")

# Program 4
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", a+b)
elif op == "-":
    print("Result:", a-b)
elif op == "*":
    print("Result:", a*b)
elif op == "/":
    print("Result:", a/b if b != 0 else "Division by zero error")
else:
    print("Invalid operator")

    # Program 5
questions = [
    {"q": "What is the capital of India?", "options": ["Delhi", "Mumbai", "Kolkata"], "ans": "Delhi"},
    {"q": "Who developed Python?", "options": ["Guido", "James", "Dennis"], "ans": "Guido"},
]

prize = 0
for q in questions:
    print(q["q"])
    print("Options:", q["options"])
    ans = input("Your answer: ")
    if ans == q["ans"]:
        prize += 1000
        print("Correct! Prize:", prize)
    else:
        print("Wrong! Game Over.")
        break

# Program 6
import random

moves = ["rock", "paper", "scissors"]

for _ in range(3):
    user = input("Enter rock/paper/scissors: ").lower()
    comp = random.choice(moves)
    print("Computer chose:", comp)

    if user == comp:
        print("It's a draw")
    elif (user == "rock" and comp == "scissors") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissors" and comp == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

# Program 7
students = ["Alice", "Bob", "Charlie", "David", "Eva"]

for _ in range(3):
    name = input("Enter student name: ")
    if name in students:
        print(f"Student {name} is enrolled")
    else:
        print(f"Student {name} is not found")
# Program 8
nums = [12, 7, 9, 20, 15, 8]
even, odd = [], []

for n in nums:
    (even if n%2==0 else odd).append(n)

print("Even numbers:", even)
print("Odd numbers:", odd)
# Program 9
words = ["Python", "is", "an", "amazing", "language"]
n = int(input("Enter a number: "))

print("Words longer than", n, ":")
for w in words:
    if len(w) > n:
        print(w)
# Program 10
lst = [1, 2, 2, 3, 4, 3, 5, 1]
unique = list(set(lst))
print("Unique elements:", unique)
# Program 11
scores = [95, 82, 67, 45, 77]
s = int(input("Enter a score: "))

if s in scores:
    if s >= 90:
        grade = "A"
    elif s >= 75:
        grade = "B"
    elif s >= 60:
        grade = "C"
    else:
        grade = "F"
    print("Grade:", grade)
else:
    print("Score not found")
# Program 12
total = 0
while True:
    n = int(input("Enter a number (0 to stop): "))
    if n == 0:
        break
    if n > 0:
        total += n
print("Total sum:", total)
# Program 13
dept1_guests = ["Alice", "Bob", "Charlie"]
dept2_guests = ["Bob", "David", "Eva"]

merged = list(set(dept1_guests + dept2_guests))
merged.sort()
print("Final guest list:", merged)

# Program 14
ages = [16, 18, 20, 15, 21, 17]

for age in ages:
    if age == 21:
        print("VIP check → Stopping further checks")
        break
    if age >= 18:
        print(f"Age {age}: Access granted")
        

