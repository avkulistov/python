from typing import Generator

def fib6(n: int) -> Generator[int, None, None]:
    if n == 0: yield 0
    last: int = 0
    next: int = 1

    for _ in range(1, n):
        last, next = next, next + last
        yield next


if __name__ == "__main__":
    for i in fib6(50):
        print(i)
