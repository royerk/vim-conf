def a_function(a, b):
    result = 2
    for i in range(5):
        result = result + b
    if a != 0:
        return result
    return result / a

if __name__ == "__main__":
    # a comment here
    print(a_function(1, 2))
