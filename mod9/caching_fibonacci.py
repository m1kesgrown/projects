def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n in cache:
            return cache[n]
        elif n <= 1:
            return n
        else:
            fib = fibonacci(n - 1) + fibonacci(n - 2)
            cache[n] = fib
            return fib

    return fibonacci


# Создайте функцию caching_fibonacci(), которая будет обладать кешем с предыдуще вычисленными
# значениями чисел Фибоначчи. Внутри она содержит функцию fibonacci(n), которая непосредственно
# и будет вычислять само число Фибоначчи. Функция caching_fibonacci() возвращает функцию fibonacci

# Если число Фибоначчи храниться в словаре cache, то функция fibonacci возвращает число из кеша.
# Если его нет в кеше, то мы вычисляем число и помещаем его в кеш, и возвращаем
# из функции fibonacci.