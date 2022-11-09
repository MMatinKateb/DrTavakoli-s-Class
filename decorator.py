def say_hello():
    print("Hello")

def do_twice(func):
    func()
    func()

do_twice(say_hello)