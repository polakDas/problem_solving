from time import sleep, perf_counter
from functools import wraps

def get_time(func):
    '''Doc string for get_time function'''

    @wraps(func)    # wraps the function with the given func mask
    def wrapper(*args, **kwargs):
        start_time = perf_counter()

        func(*args, **kwargs)

        end_time = perf_counter()
        total_time = round(end_time - start_time, 2)

        print(f'This function ({func.__name__}) takes {total_time} seconds')    # {func.__name__} hold the given function name
    return wrapper

@get_time
def something(name: str):
    '''Doc string for something function'''

    sleep(1)
    print(name)

if __name__ == "__main__":
    something('My Name')
    # print(something.__doc__) -> this line is working fine for something function because of the wraps function.
