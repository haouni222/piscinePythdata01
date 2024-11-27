def slice_me(family: list, start: int, end: int) -> list:
    """ Slice a 2D array and return the new one"""
    i = 0
    cmp = 2
    while i < len(family):
        if len(family[i]) != cmp:
            print("Whole list not the same shape !")
        if len(family[i]) > 2:
            print("Not a 2D array !")
            exit(1)
        i += 1
    ouga = (i, cmp)
    print("My shape is : (" + str(ouga[0]) + ", " + str(ouga[1]) + ")")
    sliced = family[start:end]
    gougak = (len(sliced), len(sliced[0]))
    print("My new shape is : (" + str(gougak[0]) + ", " + str(gougak[1]) + ")")
    return sliced
