def linearsearchproducts(productslist,targetproducts):
    indices=[]
    for index,product in enumerate(productslist):
        if product==targetproducts:
            indices.append(index)
    return indices

products=["hp","samsung","dell","apple","lenono"]
target="dell"
final=linearsearchproducts(products,target)
print(final)