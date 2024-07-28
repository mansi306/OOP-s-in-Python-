# operator overloading part-2
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __add__(self, other):
        # Create a new Book object with a placeholder title and combined page count
        return Book("Combined Book", self.pages + other.pages)

b1 = Book("The power of subconscious mind", 300)
b2 = Book("The 7 habits of highly effective people", 375)
b3 = Book("One Indian girl", 300)

# Adding books together
combined_book = b1 + b2 + b3
print("Total number of pages:", combined_book.pages)
