# Solution 01 — String Methods

RAW_DATA = [
    "  the great gatsby , F. Scott Fitzgerald , 1925  ",
    "1984,george orwell,1949",
    "  To Kill a Mockingbird,Harper Lee ,  1960",
    "brave NEW world , Aldous Huxley,1932  ",
    "  THE HOBBIT,  J.R.R. Tolkien ,1937",
]


def parse_line(line):
    parts = line.split(",")           # ["  the great gatsby ", " F. Scott Fitzgerald ", " 1925  "]
    title  = parts[0].strip().title() # strip whitespace, then Title Case
    author = parts[1].strip().title()
    year   = int(parts[2].strip())    # strip then convert to int
    return (title, author, year)


def format_book(book):
    title, author, year = book        # unpack the tuple
    return f"[{year}] {title} — {author}"


def books_by_author(books):
    result = {}
    for title, author, year in books:
        if author not in result:
            result[author] = []       # create list on first encounter
        result[author].append(title)
    return result


def search_title(books, term):
    term_lower = term.lower()
    return [title for title, author, year in books if term_lower in title.lower()]


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
