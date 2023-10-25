# Random code
print(4 // 2)
print(type("A"))
print(type("a"))

def mimic(my_words: str) -> str:
    """Given the string my_words, outputs the same string"""
    return my_words
print("hello!")
print(mimic("hello!"))

def mimic_letter(my_words: str, letter_idx: int) -> str:
    """Outputs the character of my_words at index letter_idx"""
    if letter_idx < len(my_words):
        return my_words[letter_idx]
    else:
        return "Index too high"

print(mimic_letter("Hello!", 4))

xs: str = "123"
ys: str = "45"

x_idx: int = 0
while x_idx < len(xs):
    y_idx: int = 0
    while y_idx < len(ys):
        print(f"{xs[x_idx]},{ys[y_idx]}")
        y_idx = y_idx + 1
    x_idx = x_idx + 1

def f(x: int) -> int:
    return x
    x *= 2
    print(x)

y: int = f(3)
print(y)

def f(x: int) -> int:
    print(x)
    x *= 2
    return x

y: int = f(3)
print(y)
