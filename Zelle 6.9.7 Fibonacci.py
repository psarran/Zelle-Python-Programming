#Zelle 6.9.7 fibonacci

def fibonacci(n):
    out = [1,1]
    for i in range(1,n):
            out += [out[i-1] + out[i]]
    return out[n-1]

print(fibonacci(2))

