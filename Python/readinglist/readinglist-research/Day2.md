# Day 2

## Learn the terms: initialization, declaration and assignment of variables

### Initialization
Initialization is the first time the variable receives a value.

Example in Python:
```python
x = 10 # initialization (and declaration happens here too)
```

### Declaration
At a declaration, you assign a value to a variable.

For example in Python:
```python
x  # invalid in Python because declaration happens with assignment
```


### Assignment
An assignment means you set or change the value of the variable after it exists.

For example in Python:
```python
x = 10   # initialization
x = 20   # assignment (old value replaced)

```

Source: [Stackoverflow](https://stackoverflow.com/questions/2614072/java-define-terms-initialization-declaration-and-assignment)

## What is the difference between Dynamically typed and Statically typed variables?
The main difference is **when the type of variable is known** and **whether you need to explicitly declare it**.

### Statically typed variables
- The variable type is fixed at compile time.
- You must declare the type of the variable before using it.

Here's an example in Java:
```Java
int age = 25;
// age = "hello"; -> gives an error, because you can not assign a sting to an int. Age can only hold integers.
```

### Dynamically typed variables
- The variable type is declared at runtime.
- You don't need to declare the type specially, it can change.

Here's an example in Python:
```python
age = 25
age = "twenty-five" 
```

String was first an integer (25) and then it became a string without errors.


