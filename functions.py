# def test():
#     print("A")
#     return
#     print("B")
# test()


# def add(a,b):
#     return a + b
# result=add(10, 20)
# print(result)



# def add(a, b):
#     print(a+b)
# result=add(10,20)
# print(result)




# def add(a, b):
#     print(a+b)
# add(10, 20)




# def test():
#     print("A")
#     return
#     print("B")
# test()




# def stats(a,b):
#     return a+b,a*b
# s,p=stats(2,4)
# print("Sum:",s)
# print("Product:",p)

# square = lambda x:x*x
# print(square(5))

# def greet(name,age):
#     print(name,age)
#     print("Name:",name)
#     print("Age:",age)
# greet(25,"Achu")


# def greet(name,age):
#     print("Name:",name)
#     print("Age:",age)
# greet(age=25,name="Shivaay")
# 
# def greet(name="Guest"):
#     print("Hello",name)
# greet("Rudra")

# def total(*numbers):
#     result = 0
#     for n in numbers:
#         result += n
#     return result
# print(total(10,20))
# print(total(10,20,30))

# def student_info(**data):
#     for key ,value in data.items():
#         print(key,":",value)
# student_info(name="Ravi",age=18,marks=85)

# def demo(*args,**kwargs):
#     print(args)
#     print(kwargs)
# demo(10,20,name="Achu",age=25)

# def show():
#     x=10
#     print(x)
# show()

# x= "global"
# def outer():
#     x = "enclosing"
#     def inner():
#         x= "local"
#         print("Inner x:",x)
#     inner()
#     print("Outer x:",x)
# outer()
# print("Global x:",x)

# def countdown(n):
#     print(n)
#     if n> 1:
#         countdown(n-1)
# countdown(5)

