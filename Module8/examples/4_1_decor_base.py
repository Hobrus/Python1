# Это и есть функцяи декоратор
def new_decorator(function_to_decorate):
    def wrapper():
        print("Я - код, который отработает до вызова функции")
        function_to_decorate()  # Сама функция
        print("А я - код, срабатывающий после")

    return wrapper


# Вот так просто мы можем декорировать любую функцию
@new_decorator
def simple_function():
    print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?")
#
#
# # Вызываем декорируемую функцию:
simple_function()

# new_decorator(simple_function)()