import random

from task1 import kwargsAcceptFun
from task2 import typeBasedTransformer
from task3 import decorator_1

# #1
# print(kwargsAcceptFun(name="Azamat", age=19, email="a.davronov@newuu.uz", major="AI"))
# print(kwargsAcceptFun(name = "Oxun", age = 20, email = "o.oxie@newuu.uz", major = "Medicine"))
#
# #2
# data = { "mapping": {"a": 1, "b": 2},}
# result = typeBasedTransformer(**data)
# print(result)

#3


@decorator_1
def func():
    print("I am ready to Start")
    result = 0
    n = random.randint(10, 751)
    for i in range(n):
        result += (i**2)

@decorator_1
def funx(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n = random.randint(10, 751)
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i

if __name__ == "__main__":
    func()
    funx()
    func()
    funx()
    func()
