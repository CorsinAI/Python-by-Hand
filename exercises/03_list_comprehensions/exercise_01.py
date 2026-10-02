# Exercise 01 — List Comprehensions
# Topic: basic comprehension, filter (if), ternary (if/else), flattening
#
# Rule: every task must be solved with a single list comprehension — no loops.

numbers = [3, 7, 2, 9, 4, 1, 8, 6, 5, 10]

words = ["hello", "world", "python", "is", "fun", "list", "comprehension"]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]


# Task 1 — squares
# Return a list of the square of every number in `numbers`.
# Expected: [9, 49, 4, 81, 16, 1, 64, 36, 25, 100]

squares = ...  # your comprehension here


# Task 2 — big_numbers
# Return only the numbers from `numbers` that are greater than 5.
# Expected: [7, 9, 8, 6, 10]

big_numbers = ...


# Task 3 — even_squares
# Return the squares of only the even numbers in `numbers`.
# Expected: [4, 16, 64, 36, 100]

even_squares = ...


# Task 4 — labels
# For every number in `numbers`, produce "big" if > 5, otherwise "small".
# Expected: ['small', 'big', 'small', 'big', 'small', 'small', 'big', 'big', 'small', 'big']

labels = ...


# Task 5 — long_words
# Return the words from `words` that have more than 4 characters, in UPPER CASE.
# Expected: ['HELLO', 'WORLD', 'PYTHON', 'COMPREHENSION']

long_words = ...


# Task 6 — flat
# Flatten `matrix` into a single list.
# Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]

flat = ...


# Task 7 — word_lengths
# Build a dict mapping each word in `words` to its length.
# Expected: {'hello': 5, 'world': 5, 'python': 6, 'is': 2, 'fun': 3, 'list': 4, 'comprehension': 13}
# Hint: this is a dict comprehension, not a list comprehension — same idea, different brackets.

word_lengths = ...


# ----- MAIN ----------------------------------------------------------------

if __name__ == "__main__":
    print("squares      :", squares)
    print("big_numbers  :", big_numbers)
    print("even_squares :", even_squares)
    print("labels       :", labels)
    print("long_words   :", long_words)
    print("flat         :", flat)
    print("word_lengths :", word_lengths)
