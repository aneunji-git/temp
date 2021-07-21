def decorator(func):
    def decorated(input_text):
        print('함수 시작!')
        func(input_text)
        print('함수 끝!')
    return decorated

@decorator
def hello_world(input_text):
    print(input_text)


hello_world("Hello World")



def decorator_1(func):
    def decorated_1(base, height):
        if base<0 or height<0:
            print('Error')
        else:
            func(base, height)
    return decorated_1

@decorator_1
def triangle(base, height):
    print(base * height* 0.5)

@decorator_1
def rectangle(base, height):
    print(base * height)



tri1 = triangle(4,7)
print(tri1)