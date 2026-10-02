# Solution 01 — List Comprehensions

numbers = [3, 7, 2, 9, 4, 1, 8, 6, 5, 10]

words = ["hello", "world", "python", "is", "fun", "list", "comprehension"]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# Task 1 — squares
squares = [x**2 for x in numbers]

# Task 2 — big_numbers
big_numbers = [x for x in numbers if x > 5]

# Task 3 — even_squares
even_squares = [x**2 for x in numbers if x % 2 == 0]

# Task 4 — labels (ternary: expression before for)
labels = ["big" if x > 5 else "small" for x in numbers]

# Task 5 — long_words
long_words = [w.upper() for w in words if len(w) > 4]

# Task 6 — flat (nested: outer loop over rows, inner loop over items)
flat = [n for row in matrix for n in row]

# Task 7 — dict comprehension
word_lengths = {w: len(w) for w in words}


if __name__ == "__main__":
    print("squares      :", squares)
    print("big_numbers  :", big_numbers)
    print("even_squares :", even_squares)
    print("labels       :", labels)
    print("long_words   :", long_words)
    print("flat         :", flat)
    print("word_lengths :", word_lengths)
