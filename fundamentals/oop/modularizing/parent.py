local_val = "magic unicorns"
def square(x):
    return x*x

class User:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return "hello"

print(square(5))
user = User("Anna")
print(user.name)
print(user.say_hello())
print(__name__)

if __name__ == "__main__":
    print("the firle is being executed directlyl")
else:
    print("the file is being executed because it is imported by another file. the file is called: ", __name__)