

def decorator(func):
    def decorated(a, b):
        print('함수 시작!')

        func(a, b)
        print('함수 끝!\n')

    def decorated(input_text):
        func(input_text)

    return decorated

@decorator
def rec(a, b):
    print('사각형의 넓이 = ', a * b)

@decorator
def tri(a, b):
    print('삼각형의 넓이 = ', a * b / 2)

@decorator
def hello_world(input_text):
    print(input_text)


# hello_world('Hello World!')

rec(4, 4)
tri(4, 4)