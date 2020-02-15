
"""This dictionary contains everything we need """
recipe_data = {
    "0": {
        "name":"chicken parmesan",
        "ingredients": {["2 large eggs","1 tablespoon garlic","2 tablespoons parsley","salt and pepper","3 large chicken breasts halved","1 cup Panko breadcrumbs",""]},
        "instructions": {"step1":"Add one cup of olives to the ice cream"},
        "description": str(),
        "time":0,
        "related": [],
        "likes": 0,
        "picture": "cat.gif",
        "tags": []
    },
}
    
}

my_id=0
"""prints every ingredient in recipe 0"""
for ingredient in recipe_data[my_id]["ingredients"]:
    print(ingredient)





