# Exercise 01 — Dictionaries
# Topic: creating, reading, iterating, sorting dicts
#
# Background: you had a Grade.py that used separate lists for students and grades.
# That was fragile. Rewrite the core logic using a dictionary instead.
#
# The data: map each student name to a list of their scores (1–6 scale).

# ----- DATA ----------------------------------------------------------------

# TODO: create a dict called `students` where each key is a name (str)
# and each value is a list of scores (list of ints).
# Students and scores:
#   Alice:    [4, 2, 4, 5, 6, 6]
#   Ben:      [5, 1, 2, 4, 4, 3]
#   Caroline: [4, 5, 5, 2, 3, 4]
#   Dave:     [1, 2, 3, 4, 5, 6]
#   Esther:   [6, 5, 6, 4, 3, 5]

students = ...  # replace with your dict


# ----- HELPER --------------------------------------------------------------

def average(scores):
    # TODO: return the average of a list of numbers, rounded to 2 decimal places
    pass


# ----- TASKS ---------------------------------------------------------------

# Task 1 — Print every student's average score.
# Expected format:  Alice | avg: 4.5
def print_averages(students):
    # TODO: iterate over the dict and print name + average
    pass


# Task 2 — Find and return the name of the student with the highest average.
def top_scorer(students):
    # TODO: find the key whose value-list has the highest average
    pass


# Task 3 — Add a new student "Frank" with scores [5, 4, 5, 3, 6, 4].
def add_student(students, name, scores):
    # TODO: add the entry to the dict (modify in place)
    pass


# Task 4 — Remove "Dave" from the dict safely (don't crash if he's missing).
def remove_student(students, name):
    # TODO: remove the key; use .pop() with a default so it won't raise
    pass


# Task 5 — Return a list of (name, average) tuples sorted best → worst.
def ranked(students):
    # TODO: sort students by average descending, return as list of tuples
    pass


# ----- MAIN ----------------------------------------------------------------

if __name__ == "__main__":
    print("=== Averages ===")
    print_averages(students)

    print("\n=== Top scorer ===")
    print(top_scorer(students))

    print("\n=== After adding Frank ===")
    add_student(students, "Frank", [5, 4, 5, 3, 6, 4])
    print_averages(students)

    print("\n=== After removing Dave ===")
    remove_student(students, "Dave")
    print_averages(students)

    print("\n=== Ranked ===")
    for name, avg in ranked(students):
        print(f"  {name}: {avg}")
