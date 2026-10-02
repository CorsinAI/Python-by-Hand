# List Comprehensions — Rulebook

A list comprehension builds a new list in one expression. It replaces the pattern of "create empty list, loop, append."

---

## Basic syntax

```python
# Old way
result = []
for x in iterable:
    result.append(expression)

# Comprehension
result = [expression for x in iterable]
```

```python
squares = [x**2 for x in range(1, 6)]
# [1, 4, 9, 16, 25]
```

## With a filter (if clause)

```python
# Old way
result = []
for x in iterable:
    if condition:
        result.append(expression)

# Comprehension
result = [expression for x in iterable if condition]
```

```python
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

even_squares = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]
```

## With if/else (ternary — expression changes, not filter)

```python
# Note: the if/else goes BEFORE the for, not after
result = [a if condition else b for x in iterable]

labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
# ["even", "odd", "even", "odd", "even"]
```

## Nested (loop inside loop)

```python
pairs = [(x, y) for x in [1, 2] for y in ["a", "b"]]
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
```

## Flattening a list of lists

```python
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [n for row in matrix for n in row]
# [1, 2, 3, 4, 5, 6]
```

## Related: dict and set comprehensions

```python
{k: v for k, v in pairs}          # dict comprehension
{x**2 for x in range(5)}          # set comprehension (no duplicates)
(x**2 for x in range(5))          # generator expression (lazy, not a list)
```

---

## When NOT to use a comprehension

- When the logic is complex enough to need multiple lines — use a regular loop.
- When you have side effects (printing, writing files) — use a regular loop.
- Rule of thumb: if it fits on one readable line, comprehension is fine.

---

## Common mistakes

| Mistake | Fix |
|---|---|
| Ternary `if/else` placed after `for` | put ternary before `for`: `[a if c else b for x in ...]` |
| Comprehension that mutates items in the original list | comprehensions create a **new** list; original is unchanged |
