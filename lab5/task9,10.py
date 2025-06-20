import re


# ex 9
test = "SplitStringOooGood"
resub = re.sub(r"(\w)([A-Z])", r"\1 \2", test)
print(resub)

# ex 10
test = "helloWorld_world"
snake_case = re.sub(r'([a-z])([A-Z])', r'\1_\2', test).lower()
print(snake_case)
