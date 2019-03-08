def slow_fibonacci(n):
    if n in {0, 1}:
        return 1

    return slow_fibonacci(n-1) + slow_fibonacci(n-2)

def run_serial():
    for _ in range(10):
        print(slow_fibonacci(31))

if __name__ == '__main__':
    run_serial()
