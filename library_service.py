"""Core business logic for the Library Management System."""

from typing import List, Dict
from models import Book, Member, Loan
from exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookUnavailableError,
    BookNotBorrowedError
)


class LibraryService:
    """Manages all library operations: books, members, and loans."""
    
    def __init__(self):
        self._books: Dict[str, Book] = {}
        self._members: Dict[str, Member] = {}
        self._loans: List[Loan] = []
        self._loan_counter = 0
    
    def add_book(self, book_id: str, title: str, author: str) -> Book:
        """
        Add a new book to the library.
        
        Args:
            book_id: Unique identifier for the book
            title: Title of the book
            author: Author of the book
        
        Returns:
            The created Book object
        """
        book = Book(book_id, title, author)
        self._books[book_id] = book
        return book
    
    def register_member(self, member_id: str, name: str, email: str) -> Member:
        """
        Register a new member to the library.
        
        Args:
            member_id: Unique identifier for the member
            name: Name of the member
            email: Email address of the member
        
        Returns:
            The created Member object
        """
        member = Member(member_id, name, email)
        self._members[member_id] = member
        return member
    
    def borrow_book(self, book_id: str, member_id: str) -> Loan:
        """
        Borrow a book for a member.
        
        Args:
            book_id: ID of the book to borrow
            member_id: ID of the member borrowing the book
        
        Returns:
            The created Loan object
        
        Raises:
            BookNotFoundError: If book doesn't exist
            MemberNotFoundError: If member doesn't exist
            BookUnavailableError: If book is already borrowed
        """
        # Lookup book
        book = self._books.get(book_id)
        if book is None:
            raise BookNotFoundError(f"Book not found: {book_id}")
        
        # Lookup member
        member = self._members.get(member_id)
        if member is None:
            raise MemberNotFoundError(f"Member not found: {member_id}")
        
        # Check availability
        if not book.available:
            raise BookUnavailableError(f"Book is already borrowed: {book.title}")
        
        # Borrow the book
        book.borrow()
        
        # Create loan record
        self._loan_counter += 1
        loan_id = f"L{self._loan_counter:03d}"
        loan = Loan(loan_id, book, member)
        self._loans.append(loan)
        
        return loan
    
    def return_book(self, loan_id: str) -> Loan:
        """
        Return a borrowed book.
        
        Args:
            loan_id: ID of the loan to close
        
        Returns:
            The closed Loan object
        
        Raises:
            BookNotBorrowedError: If loan doesn't exist or is already closed
        """
        # Find the loan
        loan = None
        for l in self._loans:
            if l.loan_id == loan_id:
                loan = l
                break
        
        if loan is None or not loan.is_active:
            raise BookNotBorrowedError(f"Loan not found or already closed: {loan_id}")
        
        # Return the book
        loan.book.return_book()
        loan.close_loan()
        
        return loan
    
    def view_books(self) -> List[Book]:
        """
        Get all books in the library.
        
        Returns:
            List of all Book objects
        """
        return list(self._books.values())
    
    def view_members(self) -> List[Member]:
        """
        Get all registered members.
        
        Returns:
            List of all Member objects
        """
        return list(self._members.values())
    
    def view_loans(self) -> List[Loan]:
        """
        Get all loan records.
        
        Returns:
            List of all Loan objects
        """
        return list(self._loans)
