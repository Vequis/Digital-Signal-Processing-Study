import time

def calculate_time(function, *args):
    start = time.time()
    function(*args)
    end = time.time()
    print(f"Execution time: {end - start} seconds")