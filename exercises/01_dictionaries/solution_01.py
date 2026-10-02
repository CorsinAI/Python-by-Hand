# Solution 01 — Dictionaries

students = {
    "Alice":    [4, 2, 4, 5, 6, 6],
    "Ben":      [5, 1, 2, 4, 4, 3],
    "Caroline": [4, 5, 5, 2, 3, 4],
    "Dave":     [1, 2, 3, 4, 5, 6],
    "Esther":   [6, 5, 6, 4, 3, 5],
}


def average(scores):
    return round(sum(scores) / len(scores), 2)


def print_averages(students):
    for name, scores in students.items():
        print(f"{name} | avg: {average(scores)}")


def top_scorer(students):
    # max() with a key function: evaluate each name by its average
    return max(students, key=lambda name: average(students[name]))


def add_student(students, name, scores):
    students[name] = scores


def remove_student(students, name):
    students.pop(name, None)  # None default means no crash if missing


def ranked(students):
    return sorted(students.items(), key=lambda kv: average(kv[1]), reverse=True)


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
