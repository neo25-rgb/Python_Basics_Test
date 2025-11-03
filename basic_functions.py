

def add(num1, num2):
    sum=num1 + num2
    return sum

def subtract(num1, num2):
    result=num1 - num2
    return result

def multiply(num1, num2):
    product=num1 * num2
    return product

def divide(num1, num2):
    # result=num1/num2
    if num2==0:
        raise ValueError
    result=num1/num2
    return result

    # if num2==0:
    #     raise ValueError
    # else:
        # return result


def fizz_buzz(number):
    if number%5==0 and number%3==0:
        return "FizzBuzz"
    if number%3==0:
        return "Fizz"
    if number%5==0:
        return "Buzz"
    # if number%5==0 and number%3==0:
    #     return "FizzBuzz"
    else:
        return number


def fibonacci(n):
    n=(n+1)
    return n
        
def triangle(n):
    n=[]
    pass  # Implement triangle generation logic