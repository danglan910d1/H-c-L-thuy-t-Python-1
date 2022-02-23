def greet(n) :
    i = 0
    while i < n:
        i = i + 1
        print("Hello my friend")

def sumNums (*args) :
    sum = 0
    for item in args :
        sum += item
    return sum

def myRange (start, end, step) :
    i = start
    while i <= end :
        yield i
        i += step