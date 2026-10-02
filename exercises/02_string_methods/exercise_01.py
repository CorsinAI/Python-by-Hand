# Exercise 01 — String Methods
# Topic: strip, split, join, replace, f-strings, upper/lower/title
#
# Scenario: you receive raw data lines from a messy CSV export.
# Each line describes a book. Your job is to parse and reformat them.

RAW_DATA = [
    "  the great gatsby , F. Scott Fitzgerald , 1925  ",
    "1984,george orwell,1949",
    "  To Kill a Mockingbird,Harper Lee ,  1960",
    "brave NEW world , Aldous Huxley,1932  ",
    "  THE HOBBIT,  J.R.R. Tolkien ,1937",
]

# Each line has the format: "title , author , year"
# Values may have extra whitespace. Case is inconsistent.


# Task 1 — parse_line
# Given a raw line string, return a tuple: (title, author, year)
# Rules:
#   - strip each field of whitespace
#   - title should be Title Case
#   - author should be Title Case
#   - year should be an int
#
# Example:
#   parse_line("  the great gatsby , F. Scott Fitzgerald , 1925  ")
#   -> ("The Great Gatsby", "F. Scott Fitzgerald", 1925)

def parse_line(line):
    # TODO: split on "," then clean each part
    pass


# Task 2 — format_book
# Given the (title, author, year) tuple, return a neatly formatted string.
# Format exactly:  "[year] Title — Author"
# Example:  "[1925] The Great Gatsby — F. Scott Fitzgerald"

def format_book(book):
    # TODO: use an f-string
    pass


# Task 3 — books_by_author
# Given a list of parsed book tuples, return a dict mapping author -> list of titles.
# (One author might have multiple books.)

def books_by_author(books):
    # TODO: build the dict; don't overwrite existing entries — append instead
    pass


# Task 4 — search_title
# Given a list of parsed book tuples and a search term (str),
# return a list of matching titles where the search term appears
# (case-insensitive).

def search_title(books, term):
    # TODO: use .lower() on both sides when comparing
    pass


# ----- MAIN ----------------------------------------------------------------

if __name__ == "__main__":
    books = [parse_line(line) for line in RAW_DATA]

    print("=== Formatted books ===")
    for book in books:
        print(format_book(book))

    print("\n=== Books by author ===")
    by_author = books_by_author(books)
    for author, titles in by_author.items():
        print(f"  {author}: {titles}")

    print("\n=== Search: 'the' ===")
    results = search_title(books, "the")
    for title in results:
        print(f"  {title}")
