import mymodule

print("TOP LEVEL IN mymodule2.py")
mymodule.func()

if __name__ == "__main__":
    print("mymodule2.py is being run directly")
else:
    print("mymodule2.py is being imported")