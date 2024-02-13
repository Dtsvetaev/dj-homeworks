from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def recipe(request, dish):

    servings = request.GET.get('servings', 1)
    try:
        servings = int(servings)
    except ValueError:
        servings = 1


    ingredients = DATA.get(dish, {})

    scaled_ingredients = {ingredient: amount * servings for ingredient, amount in ingredients.items()}


    context = {'recipe': scaled_ingredients}

    return render(request, 'calculator/index.html', context)
