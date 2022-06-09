cube = lambda x: x*x*x# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    a = [0,1]
    for i in range(2,n):
        a.append(a[i-2] + a[i-1])
    return(a[0:n])


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))