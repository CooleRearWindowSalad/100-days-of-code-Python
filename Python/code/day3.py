name = input("Enter your name: ")
print("hello,", name, ".")

age = int(input("enter your age: "))
height = float(input("enter your height: "))

print(f"""
Hello, {name},
You are {age} years old,
and your height is {height}
""")

print(f"""
Data types:
name = {type(name)}
age = {type(age)}
height = {type(height)}
""")
