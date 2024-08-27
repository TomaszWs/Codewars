# Create a function called _if which takes 3 arguments: a value bool and 2
# functions(which do not take any parameters): func1 and func2 When
# bool is truthy, func1 should be called, otherwise call the func2. Example:
#
#
# def truthy():
#     print("True")
#
#
# def falsey():
#     print("False")
#
#
# _if(True, truthy, falsey)
# # prints 'True' to the console


def truthy():
    print("True")


def falsey():
    print("False")


def _if(bool, func1, func2):
    if bool:
        func1()
    else:
        func2()

if __name__ == '__main__':
    _if(True, truthy, falsey)


# Best solutions:


def _if(bool, func1, func2):
  func1() if bool else func2()


def _if(bool, func1, func2):
    func1() if bool else func2()
