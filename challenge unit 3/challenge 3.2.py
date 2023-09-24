Write a function called linear_search_product that takes the list of products and a target product name as input. The function should perform a linear search to find the target product in the list and return a list of indices of all occurrences of the product if found, or an empty list if the product is not found.


def linearsearchproduct(productList, target_product):
    indices = []
    for index, product in enumerate(productList):
        if product == target_product:
            indices.append(index)
    return indices

#example of usage:

# Sample list of products
products = ["apple", "banana", "orange", "apple", "grape", "apple"]

# Target product to search for
target_product = "apple"

# Call the function
result = linearsearchproduct(products, target_product)

# Print the result
print(result)