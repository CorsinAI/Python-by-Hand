# String Methods — Rulebook

Strings are immutable. Every method returns a **new** string; the original never changes.

---

## Cleaning

```python
"  hello  ".strip()       # "hello"   — removes leading/trailing whitespace
"  hello  ".lstrip()      # "hello  " — left side only
"  hello  ".rstrip()      # "  hello" — right side only
"hello".strip("lo")       # "he"      — strips any of these chars
```

## Case

```python
"hello".upper()           # "HELLO"
"HELLO".lower()           # "hello"
"hello world".title()     # "Hello World"  — first letter of each word
"hello world".capitalize()# "Hello world"  — first letter of string only
```

## Searching

```python
"hello".startswith("he")  # True
"hello".endswith("lo")    # True
"hello".find("ll")        # 2  — index of first match, -1 if not found
"hello".count("l")        # 2  — how many times substring appears
"hello" in "say hello"    # True
```

## Replacing & splitting

```python
"hello".replace("l", "r")        # "herro"
"a,b,c".split(",")               # ["a", "b", "c"]
"a,b,c".split(",", maxsplit=1)   # ["a", "b,c"]
"hello world".split()            # ["hello", "world"]  (splits on any whitespace)
",".join(["a", "b", "c"])        # "a,b,c"  — inverse of split
```

## f-strings (most useful for formatting)

```python
name = "Alice"
score = 4.5
f"{name} scored {score}"          # "Alice scored 4.5"
f"{score:.2f}"                    # "4.50"  — 2 decimal places
f"{name:<10}"                     # "Alice     "  — left-aligned in 10 chars
f"{name:>10}"                     # "     Alice"  — right-aligned
f"{42:05d}"                       # "00042"  — zero-padded integer
```

## Multiline / raw strings

```python
text = """line one
line two"""          # triple quotes for multiline

path = r"C:\Users\name"  # raw string — backslashes are literal
```

---

## Common mistakes

| Mistake | Fix |
|---|---|
| `s.split(",")` leaves spaces: `" ben "` | chain: `s.split(",")` then `.strip()` each part |
| Forgetting strings are immutable | always reassign: `s = s.strip()` |
| `"hello"[1] = "a"` crashes | build a new string instead |
