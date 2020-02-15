
"""This dictionary contains everything we need """
recipe_data = {
    int(): {
        "name":str(),
        "ingredients":{"name":"amount"},
        "description":str(),
    }
}

my_id=0
"""prints every ingredient in recipe 0"""
for ingredient in recipe_data[my_id]["ingredients"]:
    print(ingredient)
