food={"name":["haha"],"password":["123"]}

for key in food.keys():
    food[key] = food[key][0]
print(food)