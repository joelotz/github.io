Title: Playing around with FizzBuzz
Date: 2021-01-18
Tags: Python
Keywords: python, fizzbuzz
Version: Python, 3.7.4



I was bored and reading a Python article on Medium where it challenged the reader to write a python one-liner to solve the [FizzBuzz](https://en.wikipedia.org/wiki/Fizz_buzz) question. This is a long-time famous programming interview question that everyone most likely knows, so I won’t explain it. Like I said, I was bored so I wrote it out. 

Here is my long-form solution using loops:
```python
def loop_fizzbuzz(num=100):
    for i in range(1, num+1):
        if (i%3==0 and i%5==0): print("FizzBuzz")
        elif i%3==0: print("Fizz")
        elif i%5==0: print("Buzz")
        else: print(i)
    return True
    
loop_fizzbuzz()    
```
I did the one-liner using list comprehension, but then thought it would be interesting to create a generator and spit it out in a list comprehension. Since this is such a trivial example, I don't see any memory benefit, or any benefit it all except being silly.

```python 
def listcomp_fizzbuzz(num=100):
    # create a generator
    return ( 'FizzBuzz' if (i%3==0 and i%5==0) else 'Fizz' if i%3==0 else 'Buzz' if i%5==0 else i for i in range(1, num+1) )

[ print(i) for i in listcomp_fizzbuzz() ]
```



Completely by coincidence - honestly - I just saw on Twitter that [Joel Grus](https://joelgrus.com/) [@joelgrus](https://twitter.com/joelgrus) (a data science nerd that I <s>stalk</s> follow) just published a humorous and interesting book titled “[Ten Essays on Fizz Buzz](https://leanpub.com/fizzbuzz/)”. It’s a collection of stories with unusual Fizz Buzz solutions, for example, he imagines creating and training a neural network to predict the first 100 answers. Totally outrageous, but the interview story he imagines along with the solution is pretty funny! Anyways - support your fellow nerds!