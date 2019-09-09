# Контекстный менеджер
import time

class Timer:
    def __init__(self, num_runs=10):
        self.num_runs = num_runs

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self,*args,**kwargs):
        end = time.time()
        print("Выполнение заняло %.5f секунд." % (end - self.start))


def fibonachi(len_feb):
    fibonachi = [1, 2]
    while len(fibonachi) < len_feb:
        fibonachi.append(fibonachi[-1] + fibonachi[-2])
    return fibonachi

with Timer():
    fibonachi(10000)
