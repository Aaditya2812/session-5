class Book:
    """
    A class representing a book in a library.
    
    Attributes:
        title (str): The title of the book
        author (str): The author of the book
        pages (int): The number of pages in the book
        is_available (bool): Whether the book is available for checkout
    """

    def __init__(self, title, author, pages):
        """
        Initialize a new Book object.
        """
        self.title = title
        self.author = author
        self.pages = pages
        self.is_available = True  # Book starts as available

    def checkout(self):
        """
        Mark the book as checked out (not available).
        """
        if self.is_available:
            self.is_available = False
            return True
        else:
            return False

    def return_book(self):
        """
        Mark the book as returned (available).
        """
        self.is_available = True
        return True

    def get_info(self):
        """
        Return a string with the book's information.
        """
        availability = "Available" if self.is_available else "Not Available"
        return f"{self.title} by {self.author} ({self.pages} pages) - {availability}"


# Test your implementation
def test_book_class():
    """
    Test the Book class implementation.
    """
    # Create a new book
    book = Book("The Hobbit", "J.R.R. Tolkien", 295)

    # Test initial state
    print("Initial book info:", book.get_info())

    # Test checkout
    success = book.checkout()
    print("Checkout successful?", success)
    print("After checkout:", book.get_info())

    # Try to checkout again (should fail)
    success = book.checkout()
    print("Second checkout successful?", success)

    # Return the book
    success = book.return_book()
    print("Return successful?", success)
    print("After return:", book.get_info())


if __name__ == "__main__":
    test_book_class()


# Expected Output:
# Initial book info: The Hobbit by J.R.R. Tolkien (295 pages) - Available
# Checkout successful? True
# After checkout: The Hobbit by J.R.R. Tolkien (295 pages) - Not Available
# Second checkout successful? False
# Return successful? True
# After return: The Hobbit by J.R.R. Tolkien (295 pages) - Available
