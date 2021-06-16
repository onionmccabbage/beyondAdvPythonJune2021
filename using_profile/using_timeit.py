import random
import time
import timeit

def timethis(func):
    def function_timer(*args, **kwargs):
        start_time = timeit.default_timer()
        value = func(*args, **kwargs)
        run_time = timeit.default_timer() - start_time
        print('The function {} took {} seconds to run'.format(func.__name__, run_time))
        return value
    return function_timer

@timethis # we can decorate ANY function to be timed
def long_runner():
    for x in range(9):
        sleep_time = random.choice(range(1,3))
        time.sleep(sleep_time)

@timethis
def count_up():
    for i in range(1,10):
        x = i

@timethis
def count_down():
    for i in range(10, 1, -1):
        x = i

if __name__ == '__main__':
    long_runner()
    count_up()
    count_down()