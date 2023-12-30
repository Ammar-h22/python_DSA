def funcThree():
    print("funcThree")


def funcTwo():
    funcThree()
    print("funcTwo")


def funcOne():
    funcTwo()
    print("funcOne")


funcOne()
