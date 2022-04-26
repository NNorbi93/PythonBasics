import datetime


def hello_xy(name: str = "hthdhrehd") -> str:
    print("#"*50)
    if name == "hthdhrehd":
        name = input("What is your name?")
    else:
        print("I know you")
    return f"{datetime.datetime.now()} - Hello {name}!"


print(hello_xy())
print(hello_xy("gdfgfd"))
print(hello_xy(name="fghdgfd"))