import os

print("test")

for day in range(3,4*5+1):
    if day < 10:
        day = f"0{day}"
    path_string = f"day{day}"
    with open(f"{path_string}/{path_string}a.py", 'w') as file:
        file.write('Morning Session')
    with open(f"{path_string}/{path_string}b.py", 'w') as file:
        file.write('Mid-Morning Session')
    with open(f"{path_string}/{path_string}c.py", 'w') as file:
        file.write('Afternoon Session')
    with open(f"{path_string}/{path_string}d-CYOA.py", 'w') as file:
        file.write('Choose Your Own Adventure')
