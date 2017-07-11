inputArray = [3, 6, -2, -5, 7, 3]
def adjacentElementsProduct(inputArray):
    product = max([inputArray[item]*inputArray[item+1]
    for item in range(len(inputArray)-1)])
    print(product)
    return product

adjacentElementsProduct(inputArray)
#returns highest adjacent product of an array, lovely.
