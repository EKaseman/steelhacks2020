
"""This dictionary contains everything we need """
recipe_data = {
    "0": {
        "name":"chicken parmesan",
        "ingredients": {["2 large eggs","1 tablespoon garlic","2 tablespoons parsley","salt and pepper","3 large chicken breasts halved","1 cup Panko breadcrumbs","1/2 cup breadcrumbs","1/2 cup fresh grated parmesan cheese","1 teaspoon garlic","1/2 cup olive oil for frying","1 tablespoon olive oil","1 large onion chopped","2 teaspoons minced garlic","14 ounces (400 g) tomato puree","Salt and pepper to taste","1 teaspoon dried Italian herbs","8 ounces (250 g) mozzarella cheese sliced or shredded","1/3 cup fresh shredded parmesan cheese","2 tablespoons fresh chopped basil"]},
        "instructions": {"step1":"eheat oven 430°F | 220°C. Lightly grease an oven tray (or baking dish) with non stick cooking oil spray; set aside.","step2": "Whisk together eggs, garlic, parsley, salt and pepper in a shallow dish. Add chicken into the egg, rotating to evenly coat each fillet in the mixture. Cover with plastic wrap and allow to marinate for at least 15 minutes (or overnight night if time allows for a deeper flavour).","step3": "When chicken is ready for cooking, mix bread crumbs, Parmesan cheese and garlic powder together in a separate shallow bowl. Dip chicken into the breadcrumb mixture to evenly coat.","step4": "Heat oil in a large skillet over medium-high heat until hot and shimmering. Fry chicken until golden and crispy, (about 4-5 minutes each side).","step5":"Place chicken on prepared baking tray / dish and top each breast with about 1/3 cup of sauce (sauce recipe below). Top each chicken breast with 2-3 slices of mozzarella cheese and about 2 tablespoons parmesan cheese. Sprinkle with basil or parsley. ","step6":"Bake for 15-20 minutes, or until cheese is bubbling and melted, and the chicken is completely cooked through.","step7":"Heat oil in a medium-sized pot. Fry onion until transparent (about 3 minutes), then add the garlic until fragrant (about 30 seconds).","step8":"Add the tomato puree, salt and pepper to taste, Italian herbs and sugar (If using). Cover with lid to simmer for about 8 minutes, or until sauce has thickened slightly. Taste test and adjust salt and pepper, if needed."},
        "description": "Deliciousness in a bag",
        "time": "40 minutes",
        "related": ["None In The Universe"],
        "likes": 0,
        "picture": "https://hips.hearstapps.com/vidthumb/images/delish-chicken-parm-still006-1553287552.jpg",
        "tags": []
    },
}
    
}

my_id=0
"""prints every ingredient in recipe 0"""
for ingredient in recipe_data[my_id]["ingredients"]:
    print(ingredient)





