"""Book store."""


class Book:
    """Represent book model."""

    def __init__(self, title: str, author: str, price: float, rating: float):
        """
        Class constructor. Each book has title, author, price and rating.

        :param title: book's title
        :param author: book's author
        :param price: book's price
        :param rating: book's rating
        """
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating


class Store:
    """Represent book store model."""

    def __init__(self, name: str, min_rating: float):
        """
        Class constructor.

        Each book store has name and a minimum rating requirement for books.
        There also should be an overview of all books present in store.

        :param name: book store name
        :param min_rating: minimum rating for books to be kept in this store
        """
        self.name = name
        self.min_rating = min_rating
        self._books = []

    def can_add_book(self, book: Book) -> bool:
        """
        Check if book can be added.

        It is possible to add book to book store if:
        1. The book with the same author and title is not yet present in this book store
        2. book's own rating is >= than store's rating
        :return: bool
        """
        if book.rating < self.min_rating:
            return False

        for existing_book in self._books:
            if existing_book.title == book.title and existing_book.author == book.author:
                return False

        return True

    def add_book(self, book: Book):
        """
        Add new book to book store if possible.

        :param book: Book
        Function does not return anything
        """
        if self.can_add_book(book):
            self._books.append(book)

    def can_remove_book(self, book: Book) -> bool:
        """
        Check if book can be removed from store.

        Book can be successfully removed if it is actually present in store

        :return: bool
        """
        return book in self._books

    def remove_book(self, book: Book):
        """
        Remove book from store if possible.

        Function does not return anything
        """
        if self.can_remove_book(book):
            self._books.remove(book)

    def get_all_books(self) -> list:
        """
        Return a list of all books in current store.

        :return: list of Book objects
        """
        return self._books

    def get_books_by_price(self) -> list:
        """
        Return a list of books ordered by price (from cheapest).

        :return: list of Book objects
        """
        return sorted(self._books, key=lambda b: b.price)

    def get_most_popular_book(self) -> list:
        """
        Return a list of book (books) with the highest rating.

        :return: list of Book objects
        """
        if not self._books:
            return []

        max_rating = max(book.rating for book in self._books)

        return [book for book in self._books if book.rating == max_rating]