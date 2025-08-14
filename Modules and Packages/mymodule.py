def func():
    print("FUNC() in mymodule.py")

def func2():
    pass

def func3():
    pass

#print("TOP LEVEL IN mymodule.py")

if __name__ == "__main__":
    print("mymodule.py is being run directly")
    func2()
    func()
    func3()
    # ...
else:
    print("mymodule.py is being imported")