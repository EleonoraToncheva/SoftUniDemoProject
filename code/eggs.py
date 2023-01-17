number_of_eggs = int(input())

orange = 0
red = 0
blue = 0
green = 0
color_egg = ""

for i in range(number_of_eggs):
    color = input()

    if color == 'red':
        red += 1
    elif color == 'orange':
        orange += 1
    elif color == 'blue':
        blue += 1
    elif color == 'green':
        green += 1
    max_eggs = max(red, orange, blue, green)

    if red == max_eggs:
        color_egg = "red"
    elif orange == max_eggs:
        color_egg = "orange"
    elif blue == max_eggs:
        color_egg = "blue"
    elif green == max_eggs:
        color_egg = "green"
print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {max_eggs} -> {color_egg}")
