# 1
# ch = input("Enter a Character:")
# print(ord(ch))

# 2
# ch = input("Enter a Character:")
# print(ord(ch))

# 3
# num = int(input("Enter a number:"))
# print(chr(num))

#4
# word = "text"
# for ch in word:
#     print(ch,":",ord(ch))

#5
# num = int(input("Enter a number:"))
# print(chr(num))

#6
# ch = input("Enter a character:")
# if ord(ch)>= 65 and ord(ch)<=90:
#     print("Uppercase")
# else:
#     print("Not Uppercase")

#7
# ch = input("Enter a character:")
# if ord(ch) >=91 and ord(ch) <=122:
#     print("Lowercase")
# else:
#     print("Not Lowercase")

#8
# ch = input("Enter a character:")
# if ord(ch) >= 48 and ord(ch) <= 57:
#     print("The character is a digit")
# else:
#     print("The character is not a digit")

#9
# word ="teXt"
# cnt= 0
# for ch in word:
#     if ord(ch)>= 65 and ord(ch)<=90:
#         cnt = cnt+1
# print(cnt)

#10
# word="l1iab2"
# cnt = 0
# for ch in word:
#     if ord(ch) >= 48 and ord(ch) <= 57:
#         cnt = cnt+1
# print(cnt)

#11
# text = input("Enter the character:")
# sep=["-",";",":"]
# for ch in text:
#     if ch in sep:
#         print("Seperator")
#     else:
#         print("No Seperator")

#12
# text = input("Enter the character:")
# sep=["-",";",":"]
# cnt = 0
# for ch in text:
#     if ch in sep:
#         cnt = cnt+1
# print(cnt)

#13
# text = "hello-world"
# sep=["-",";",":"]
# word=""
# for ch in text:
#     if ch in sep:
#         continue
#     else:
#         word += ch
# print(word)

#14
# text = "hello-world"
# word=""
# sep = ["-",";",":"]
# for ch in text:
#     if ch in sep:
#         word += " "
#     else:
#         word += ch
# print(word)

#15
# text = "Welcome to python programming"
# word=""
# words=[]
# for ch in text:
#     if ch != " " :
#         word += ch
#     else:
#         words.append(word)
#         word = ""
# words.append(word)
# print(words)

#16
# text = "Python is a programming language"

# word = ""
# longest = ""

# for ch in text:
#     if ch != " ":
#         word += ch
#     else:
#         if len(word) > len(longest):
#             longest = word
#         word = ""

# if len(word) > len(longest):
#     longest = word

# print("Longest word:", longest)

#17
# text = "Python is a programming language"

# word = ""
# shortest = ""

# for ch in text:
#     if ch != " ":
#         word += ch
#     else:
#         if shortest =="" or len(word) < len(shortest):
#             shortest = word
#         word = ""

# if shortest == "" or len(word) < len(shortest):
#     shortest = word

# print("Shortest word:", shortest)

#19
# text="vda165dwf7856"
# number = ""

# for ch in text:
#     if ord(ch) >= 48 and ord(ch) <= 57:
#         number = number + ch

# print(number)

#20
# text="vda165dwf78GH56"
# alphabets = ""

# for ch in text:
#     if ord(ch) >= 65 and ord(ch) <= 122:
#         alphabets = alphabets + ch

# print(alphabets)

#21
# text = "Hello123!"
# Uppercase = 0
# Lowercase = 0
# Digits = 0
# Special = 0

# for ch in text:
    
#     if ord(ch) >= 65 and ord(ch) <= 90:
#         Uppercase += 1

#     elif ord(ch) >= 97 and ord(ch) <= 122:
#         Lowercase += 1

#     elif ord(ch) >= 48 and ord(ch) <= 57:
#         Digits += 1

#     else:
#         Special += 1

# print("Uppercase:", Uppercase)
# print("Lowercase:", Lowercase)
# print("Digits:", Digits)
# print("Special:", Special)