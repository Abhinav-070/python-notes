#1
# text = "banana"
# frequency={}

# for char in text:
#     if char in frequency:
#         frequency[char] += 1
#     else:
#         frequency[char] = 1

# for key,value in frequency.items():
#     print(key,":",value)



#2
# text = "Banana"
# frequency = {}

# for char in text:
#     if char in frequency:
#         frequency[char] += 1
#     else:
#         frequency[char] = 1

# min = 100
# freq =""

# for key,value in frequency.items():
#     if value < min:
#         min = value
#         freq = key

# print("Least frequent character :",freq)
# print("frequency:",min)

#3

# text = "banana"
# frequency={}

# for char in text:
#     if char in frequency:
#         frequency[char] += 1
#     else:
#         frequency[char] = 1

# for key,value in frequency.items():
#     if value >1:
#         print(key,":",value)

# 4
# text = "Banana"
# frequency = {}

# for char in text:
#     if char in frequency:
#         frequency[char] +=1
#     else:
#         frequency[char] = 1

# for key,value in frequency.items():
#     if value == 1:
#         print("Character appearing once:",key)

#5
# text="Banana"
# frequency = {}

# for char in text:
#     if char in frequency:
#         print("First repeated character:",char)
#         break
#     else:
#         frequency[char] = 1



#8
# text = "banana"
# frequency = {}


# for char in text:
#     if char in frequency:
#         frequency[char] += 1 
#     else:
#         frequency[char] = 1

# cnt = 0
# for key,value in frequency.items():
#     if value == 1:
#         cnt += 1

# print("Number of Unique Characters:",cnt)

#9
# text = str(1236545)
# frequency = {}

# for char in text:
#     if char in frequency:
#         frequency[char]+=1
#     else:
#         frequency[char]=1

# maxy = 0
# freq=""

# for key,value in frequency.items():
#     if maxy < value:
#         maxy = value
#         freq=key

# print("Most Frequent Number:",freq)

#10 
# text = str(142256874)
# frequency ={}

# for char in text:
#     if char in frequency:
#         frequency[char] += 1 
#     else:
#         frequency[char] = 1

# mini=100
# freq =""

# for key,value in frequency.items():
#     if mini > value:
#         mini = value
#         freq = key
# print("Least Frequent Number:",freq)

#11
# orders = ["Laptop", "Mouse", "Laptop", "Keyboard","Mouse", "Laptop"]
# frequency = {}

# for char in orders:
#     if char in frequency:
#         frequency[char] += 1
#     else:
#         frequency[char] = 1

# maxi = 0
# freq = ""

# for key,value in frequency.items():
#     if maxi < value:
#         maxi = value
#         freq = key 
# print("Most Purchased Product:",freq)

#12
# votes = ["A", "B", "A", "C", "B", "A", "B"]
# frequency={}

# for char in votes:
#     if char in frequency:
#         frequency[char] +=1
#     else:
#         frequency[char] = 1

# maxi = 0
# freq = ""

# for key,value in frequency.items():
#     if maxi< value:
#         maxi = value
#         freq = key
# print("Most Common Vote:",freq)

#13
# word = ["apple", "mango","apple","orange","mango","apple"]
# frequency={}

# for char in word:
#     if char in frequency:
#         frequency[char] += 1
#     else:
#         frequency[char] = 1

# maxi = 0
# freq=""

# for key,value in frequency.items():
#     if maxi < value:
#         maxi = value
#         freq = key
# print("Most Common Word:",freq)

#14
# names = ["Anu", "Rahul", "Anu", "Meera", "Rahul", "Anu"]
# frequency = {}

# for char in names:
#     if char in frequency:
#         frequency[char] += 1
#     else:
#         frequency[char] = 1

# maxi=0
# freq=""

# for key,value in frequency.items():
#     if maxi < value:
#         maxi = value
#         freq = key
# print("Most Common Student Name:",freq)

#15
# errors = ["404","500","404","403","404","500"]
# frequency={}

# for char in errors:
#     if char in frequency:
#         frequency[char]+=1
#     else:
#         frequency[char] = 1

# maxi =0
# freq = ""

# for key,value in frequency.items():
#     if maxi < value:
#         maxi = value
#         freq = key
# print("Most Common Error Code:",freq)

#13-1

# text = "Welcome,to python-programming"
# word=""
# words=[]
# for ch in text:
#     if ch != " " and ch != " " and ch != "-":
#         word += ch
#     else:
#         words.append(word)
#         word = ""
# words.append(word)
# print(words)

# text = "Welcome to python programming"
# print(text.split())

