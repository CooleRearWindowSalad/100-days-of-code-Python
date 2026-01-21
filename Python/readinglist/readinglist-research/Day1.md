# Day 1

## How does Python compile and run the code?
Python will be compiled from source code to bytecode and then the bytecode will be executed.

## What is the difference between Python and Java?

| Feature        | Python                             | Java                              |
|----------------|------------------------------------|-----------------------------------|
| Typing         | Dynamically typed                  | Statically typed                  |
| Speed          | Slower (interpreted)               | Faster (compiled to JVM bytecode) |
| Syntax         | Beginner-friendly                  | More verbose                      |
| Compilation    | Bytecode -> Python Virtual Machine | Bytecode -> Java Virtual Machine  |
| Learning Curve | Easier                             | Harder                            |
| Paradigm       | Multi-paradigm                     | Primarily OOP                     |

**Python** is easier to learn and is often used for fast development, scripting and automation.

On the other hand, **Java** generally offers better performance because the code is compiled to bytecode before execution.  
It is commonly used for large-scale applications such as enterprise systems and Android apps.

## What is the difference between Compiler and Interpreter?

| Feature        | Compiler          | Interpreter          |
|----------------|-------------------|----------------------|
| Translation    | Entire program    | Line-by-line         |
| Output         | Executable file   | Direct execution     |
| Runtime Speed  | Fast              | Slower               |
| Error Handling | After compilation | Stops at first error |
| Examples       | C, C++            | Python, JavaScript   |

### Compiler
- Translates **entire program** into machine code **before** execution.  
- Produces an executable file.  
- Fast execution after compilation.  
- All errors must be fixed before running.

**Examples:** C, C++, Java

### Interpreter
- Translates and executes the program **line by line**.  
- No separate executable generated.  
- Slower runtime.  
- Stops at the first encountered error.

**Examples:** Python (PVM), JavaScript, PHP