from time import time


def speed_test_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Time Elapsed : {end_time - start_time}")
        return result

    return wrapper


@speed_test_decorator
def sum_nums_list():
    return sum([x for x in range(60000000)])


@speed_test_decorator
def sum_nums_gen():
    return sum(x for x in range(60000000))


# sum_nums_list()
sum_nums_gen()

# startTime = time()
# sum([num for num in range(200000)])
# endTime = time()
#
# print(endTime - startTime)
