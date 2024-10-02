import sys


def main():
    numbers = list(map(int, input().split()))
    numbers.sort()
    print(numbers[1])


if __name__ == '__main__':
    main()