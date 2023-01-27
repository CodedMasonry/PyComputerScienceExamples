def Example():
    """
    This function demonstrates the use of arrays in Python. It creates an array called SomeArray, 
    prints the array to the console, prints the length of the array, and then adds and removes elements 
    from the array.
    """
    print("Array:")
    SomeArray = [1,2,3]
    print(SomeArray)

    length = len(SomeArray)
    print(length)

    SomeArray.append(4)
    SomeArray.append(5)
    print(SomeArray)

    SomeArray.remove(2)
    print(SomeArray)
    print("\n")
