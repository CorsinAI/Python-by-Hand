# Python-by-Hand

Deliberate practice exercises for Python. All code written by hand, no AI assistance.

---

## Structure

```
exercises/
  01_dictionaries/
    RULEBOOK.md       <- syntax reference for the topic
    exercise_01.py    <- skeleton with TODOs
    solution_01.py    <- reference solution (check after you're done)
    exercise_02.py    <- more of the same topic (added over time)
    solution_02.py
  02_string_methods/
    ...
  03_list_comprehensions/
    ...
```

New exercises on the same topic get the next number (`exercise_02`, `exercise_03`, ...).
New topics get the next folder (`04_topic_name`).

---

## How to use

1. Read the `RULEBOOK.md` for the topic.
2. Open `exercise_XX.py` and fill in the `TODO` / `...` spots.
3. Run it: `python exercise_XX.py`
4. Once it works, compare to `solution_XX.py`.

---

## Topics

| # | Topic | Concepts covered |
|---|-------|-----------------|
| 01 | Dictionaries | create, read, iterate `.items()`, sort by value, pop |
| 02 | String methods | strip, split, join, title, f-strings |
| 03 | List comprehensions | filter, ternary, flatten, dict comprehension |

---

## Loose scripts (root)

| File | Description |
|------|-------------|
| `FizzFuzz.py` | FizzBuzz variant with a Bazz rule |
| `Grade.py` | Student grade tracker using lists |
