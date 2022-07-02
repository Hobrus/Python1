def log(dir='', file_name='log.txt'):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            import os
            return_value = func(*args, **kwargs)
            with open(os.path.join(dir, file_name), "a") as f:
                f.write(f'function {func.__name__}{args}-->{return_value}\n')
            return return_value

        return wrapper

    return actual_decorator


# DEMO
if __name__ == "__main__":
    @log(file_name="log.txt")
    def summ(*args):
        s = 0
        for el in args:
            s += el

        return s


    print(summ(2, 4, 5))
    print(summ(2, 5))
