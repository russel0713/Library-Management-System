"""Interactive CLI application for the Library Management System."""

from library_service import LibraryService
from exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookUnavailableError,
    BookNotBorrowedError
)


class LibraryApp:
    """Interactive command-line interface for library management."""
    
    def __init__(self):
        self.service = LibraryService()
    
    def display_menu(self):
        """Display the main menu."""
        print("\n" + "="*50)
        print("       LIBRARY MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Books")
        print("6. View Members")
        print("7. View Loans")
        print("8. Exit")
        print("="*50)
    
    def add_book(self):
        """Add a new book to the library."""
        print("\n--- Add Book ---")
        try:
            book_id = input("Enter Book ID: ").strip()
            title = input("Enter Title: ").strip()
            author = input("Enter Author: ").strip()
            
            if not book_id or not title or not author:
                print("✗ All fields are required.")
                return
            
            self.service.add_book(book_id, title, author)
            print(f"✓ Book added: {title}")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def register_member(self):
        """Register a new member."""
        print("\n--- Register Member ---")
        try:
            member_id = input("Enter Member ID: ").strip()
            name = input("Enter Name: ").strip()
            email = input("Enter Email: ").strip()
            
            if not member_id or not name or not email:
                print("✗ All fields are required.")
                return
            
            self.service.register_member(member_id, name, email)
            print(f"✓ Member registered: {name}")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def borrow_book(self):
        """Borrow a book for a member."""
        print("\n--- Borrow Book ---")
        try:
            book_id = input("Enter Book ID: ").strip()
            member_id = input("Enter Member ID: ").strip()
            
            if not book_id or not member_id:
                print("✗ Both fields are required.")
                return
            
            loan = self.service.borrow_book(book_id, member_id)
            print(f"✓ {loan.member.name} borrowed {loan.book.title}")
            print(f"  Loan ID: {loan.loan_id}")
        except BookNotFoundError as e:
            print(f"✗ Book not found.")
        except MemberNotFoundError as e:
            print(f"✗ Member not found.")
        except BookUnavailableError as e:
            print(f"✗ Book is already borrowed.")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def return_book(self):
        """Return a borrowed book."""
        print("\n--- Return Book ---")
        try:
            loan_id = input("Enter Loan ID: ").strip()
            
            if not loan_id:
                print("✗ Loan ID is required.")
                return
            
            loan = self.service.return_book(loan_id)
            print(f"✓ {loan.book.title} returned by {loan.member.name}")
        except BookNotBorrowedError as e:
            print(f"✗ Loan not found or already closed.")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def view_books(self):
        """Display all books."""
        print("\n--- View Books ---")
        books = self.service.view_books()
        
        if not books:
            print("No books found.")
            return
        
        print(f"\n{len(books)} book(s) in library:")
        for book in books:
            print(f"  {book}")
    
    def view_members(self):
        """Display all members."""
        print("\n--- View Members ---")
        members = self.service.view_members()
        
        if not members:
            print("No members found.")
            return
        
        print(f"\n{len(members)} member(s) registered:")
        for member in members:
            print(f"  {member}")
    
    def view_loans(self):
        """Display all loans."""
        print("\n--- View Loans ---")
        loans = self.service.view_loans()
        
        if not loans:
            print("No loans found.")
            return
        
        print(f"\n{len(loans)} loan(s):")
        for loan in loans:
            print(f"  {loan}")
    
    def run(self):
        """Run the main application loop."""
        print("\nWelcome to Library Management System!")
        
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-8): ").strip()
            
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.register_member()
            elif choice == "3":
                self.borrow_book()
            elif choice == "4":
                self.return_book()
            elif choice == "5":
                self.view_books()
            elif choice == "6":
                self.view_members()
            elif choice == "7":
                self.view_loans()
            elif choice == "8":
                print("\nProgram closed.")
                break
            else:
                print("✗ Invalid choice. Please enter 1-8.")


if __name__ == "__main__":
    app = LibraryApp()
    app.run()
