
def multiply(list):
    prodlist = list[0]
    for x in list:
        prodlist *= x
    return prodlist
print(multiply([1,2,-8]))