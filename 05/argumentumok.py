



class Arguments:

    @staticmethod
    def my_sum(*args, extra: int = 0):  # pass the variable length arguments
        result = 0
        print(args)
        # Iterating over the Python args tuple
        for x in args:
            result += x
        return result

    @staticmethod
    def concatenate(**kwargs):  # pass a variable number of keyword arguments
        result = ""
        # Iterating over the Python kwargs dictionary
        print(kwargs)
        for arg in kwargs.values():
            result += arg
        return result


if __name__ == "__main__":
    print(Arguments.my_sum(5, 5, 5))
    print(Arguments.concatenate(a="The", b="Python", c="Is", d="Great"))