def benchmark(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))

    return wrapper


# DEMO
if __name__ == "__main__":
    @benchmark
    def fetch_webpage():
        import requests
        requests.get('https://google.com')


    fetch_webpage()
