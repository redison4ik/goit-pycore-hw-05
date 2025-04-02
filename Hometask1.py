def caching_fibonacci(n):
    cache = {}
    def fibonacci(n): # функція для рекурсії
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache: #переврку кешу
            return cache[n]
        else:
            cache[n] = fibonacci(n-1) + fibonacci(n-2) # виклик рекурсії
        return cache[n]
    
    return fibonacci(n)
print(caching_fibonacci(8))