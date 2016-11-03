# Method 1
def yanghui(n): # n_1_result means last line result
    global n_1_result
    if n == 1:
        n_result = [1]
        print(n_result)
    else:
        yanghui(n-1)
        for i in range(n-1):
            if i == 0:
                n_result = [1]
            else:
                n_result.append(n_1_result[i-1] + n_1_result[i])
        
        n_result.append(1)
        n_1_result = n_result
        print(n_result)
         
yanghui(10)

# Method 2
def yanghui(n): # n_1_result means last line result
    global n_1_result
    if n == 1:
        n_result = [1]
        n_1_result = n_result
        print(n_result)
    else:
        yanghui(n-1)
        n_result = [sum (i) for i in zip([0] + n_1_result, n_1_result + [0])]
        n_1_result = n_result
        print(n_result)
         
yanghui(10)

# Method 3: waste too much resource
def yanghui(n):
    if n == 1:
        return [1]
    else:
        for i in range(n-1):
            n_result = [sum (j) for j in (zip([0] + yanghui(n-1), yanghui(n-1) + [0]))]
            return n_result
         
print(yanghui(7))

# Just print the last line
def yanghui(n):
    global n_1_result
    if n == 1:
        n_result = [1]
        n_1_result = [1]
        return n_result
    else:
        yanghui(n - 1)
        n_result = [sum (j) for j in zip([0] + n_1_result, n_1_result + [0])]
        n_1_result = n_result
        return n_result

print(yanghui(10))
 
