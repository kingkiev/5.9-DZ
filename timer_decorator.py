# Декоратор через обьект-класса.


import time

class Timer:
    def __init__(self, num_runs=10):
        self.num_runs = num_runs

    def __call__(self, func):
        def wrapper(*args):
            avg_time = 0
            for _ in range(self.num_runs):
                start = time.time()
                func(*args)
                end = time.time()
                avg_time += (end - start)
            avg_time /= self.num_runs
            print("Выполнение заняло %.5f секунд" % avg_time)
            return func
        return wrapper


@Timer()
def fibonachi(len_feb):
    fibonachi = [1, 2]
    while len(fibonachi) < len_feb:
        fibonachi.append(fibonachi[-1] + fibonachi[-2])
    return fibonachi
fibonachi(10000)