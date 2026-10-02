# Dictionaries — Rulebook

A dictionary maps **keys** to **values**. Keys must be unique and immutable (strings, numbers, tuples). Values can be anything.

---

## Creating

```python
d = {}                          # empty dict
d = {"alice": 90, "ben": 75}    # with initial values
d = dict(alice=90, ben=75)      # alternative constructor
```

## Reading

```python
d["alice"]          # 90 — raises KeyError if key missing
d.get("alice")      # 90 — returns None if missing (safe)
d.get("zoe", 0)     # 0  — returns default if missing
```

## Writing

```python
d["carol"] = 88     # add or overwrite
del d["ben"]        # remove a key (KeyError if missing)
d.pop("ben")        # remove and return value (KeyError if missing)
d.pop("ben", None)  # remove and return, or None if missing (safe)
```

## Checking

```python
"alice" in d        # True
"zoe" not in d      # True
len(d)              # number of key-value pairs
```

## Iterating

```python
for key in d:               # iterate over keys
for key in d.keys():        # same, explicit
for value in d.values():    # iterate over values
for key, value in d.items():  # iterate over both — use this most often
```

## Useful patterns

```python
# Build a dict from two lists
names  = ["alice", "ben"]
scores = [90, 75]
d = dict(zip(names, scores))

# Sort by value (returns list of tuples)
sorted(d.items(), key=lambda kv: kv[1])            # ascending
sorted(d.items(), key=lambda kv: kv[1], reverse=True)  # descending

# Dict comprehension
squares = {n: n**2 for n in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

## Common mistakes

| Mistake | Fix |
|---|---|
| `d["missing"]` crashes | use `d.get("missing")` or check `"missing" in d` first |
| Iterating and deleting at the same time | iterate over `list(d.keys())` instead |
| Using a list as a key | lists are mutable — use a tuple instead |
