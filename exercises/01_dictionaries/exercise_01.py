# Exercise 01 — Dictionaries
# Topic: creating, reading, iterating, sorting dicts
#
# Background: you had a Grade.py that used separate lists for students and grades.
# That was fragile. Rewrite the core logic using a dictionary instead.
#
# The data: map each student name to a list of their scores (1–6 scale).

# ----- DATA ----------------------------------------------------------------


students = {
    "Alice" :       [4, 2, 4, 5, 6, 6], 
    "Ben" :         [5, 1, 2, 4, 4, 3], 
    "Caroline" :    [4, 5, 5, 2, 3, 4], 
    "Dave":         [1, 2, 3, 4, 5, 6], 
    "Esther" :      [6, 5, 6, 4, 3, 5]
}  


# ----- HELPER --------------------------------------------------------------

def average(scores):
    return round(sum(scores) / len(scores), 2)


# ----- TASKS ---------------------------------------------------------------

# Task 1 — Print every student's average score.
# Expected format:  Alice | avg: 4.5
def print_averages(students):
    for student, grades in students.items():
        print(f"{student} | avg: {average(grades)}")


# Task 2 — Find and return the name of the student with the highest average.
def top_scorer(students):
    return max(students, key=lambda name: average(students[name]))



# Task 3 — Add a new student "Frank" with scores [5, 4, 5, 3, 6, 4].
def add_student(students, name, scores):
    students[name] = scores


# Task 4 — Remove "Dave" from the dict safely (don't crash if he's missing).
def remove_student(students, name):
    students.pop(name, None)


# Task 5 — Return a list of (name, average) tuples sorted best → worst.
def ranked(students):
    return sorted(students.items(), key=lambda kv: average(kv[1]), reverse=True)


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
