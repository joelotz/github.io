---
Title: Python One-Liners
Date: 2021-01-20
Tags: Python
Keywords: python,
Version: Python, 3.7.4
---



As a bonus, here are two of my favorite python one-liners:

**<u>Swapping Variables</u>** - no need to use temp variables. In some other languages, like C, you would need a temporary variable to hold a value while you swap them around. Something like this:

```c
double a, b, temp;

// Assign values to variables
a = 5;
b = 7;

// Value of first variable is assigned to temp
temp = a;

// Value of second variable is assigned to the first
a = b;

// Value of temp (initial first) is assigned back to the second variable
b = temp;
```

But in Python it’s a lot more… elegant. 

```python
# Assign values to variables
a, b = 5, 7

# Swap values
a, b = b, a
```



**<u>Multiple Variable Assignment</u>** - the above example shows another of my favorites. We can assign values to multiple variables with a single line. Even cooler is we can use an asterix and assign multiple values to a variable.

```python
a, *b = [1, 2, 3, 4, 5]
print(a, b)
```

```reStructuredText
> 1 [2, 3, 4, 5]
```

In the above code, `a` is assigned the first element in the list while `b` is assigned all the remaining.

```python
*a, b = [1, 2, 3, 4, 5]
print(a, b)
```

```reStructuredText
> [1, 2, 3, 4] 5
```

In the above code, `a` is assigned all the elements except the last, and `b` is assigned the last element in the list.

```python
a, *b, c = [1, 2, 3, 4, 5]
print(a, b, c)
```

```reStructuredText
> 1 [2, 3, 4] 5
```

Finally, in the above code, `a` is assigned the first element, `c` is assigned the last element, and `b` is assigned all the elements in between.



**<u>List Comprehension</u>** - this is a really cool way to build a list without using loops. I’ve seen people go overboard on it where I couldn’t even understand what was going on. Here is the basic example:

```python
# Silly loop example
my_list = []
for i in range(5):
    my_list.append(i)
    
# List comprehension
my_list = [i for i in range(5)]
```

Here is the syntax:

```python
[expression for item in iterable if condition == True]
```

so in the previous example,

```python
my_list = [i<expression> for i<item> in range(5)<iterable>]
```

You can also get complex with the expression, 

```python
some_array = [True, False, True]
my_list = ["Hello" if i else "Goodbye" for i in some_array]
print(my_list)
```

```reStructuredText
> ['Hello', 'Goodbye', 'Hello']
```

In a [previous post](playing-around-with-fizzbuzz.html) I did a multi-line if/elif/else replacement:

```python
# Loop
for i in range(1, 101):
    if (i%3==0 and i%5==0): print("FizzBuzz")
    elif i%3==0: print("Fizz")
    elif i%5==0: print("Buzz")
    else: print(i)
        
# List Comprehension
[ 'FizzBuzz' if (i%3==0 and i%5==0) else 'Fizz' if i%3==0 else 'Buzz' if i%5==0 else i for i in range(1, 101) ]
```

Cool, huh?