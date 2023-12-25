N = int(input())
dishes = {}  
ingredients_set = set()  

for _ in range(N):
    dish_id, dish_name, ingredients, restrictions = input().split(", ")
    ingredients_list = ingredients.split(":")
    dishes[dish_id] = {"name": dish_name, "ingredients": ingredients_list, "restrictions": restrictions}
    ingredients_set.update(ingredients_list)
query_restriction = input()
max_ingredients = 0
max_ingredients_dish = ""
restricted_dishes = []
for dish_id, dish_info in dishes.items():
    if query_restriction in dish_info["restrictions"]:
        restricted_dishes.append(dish_info["name"])
for dish_id, dish_info in dishes.items():
    num_ingredients = len(dish_info["ingredients"])
    if num_ingredients > max_ingredients:
        max_ingredients = num_ingredients
        max_ingredients_dish = dish_info["name"]


print(f"Dishes for {query_restriction}: {', '.join(restricted_dishes)}")
print(f"All ingredients: {', '.join(sorted(ingredients_set))}")
print(f"Dish with most ingredients: {max_ingredients_dish}")
