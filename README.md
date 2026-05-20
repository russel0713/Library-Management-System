# Library Management System

A comprehensive Python-based library management system with interactive CLI for managing books, members, and loans.

## 📋 Features

### 1. **Add Book**
- Add new books to the library with ID, title, and author
- Books are initialized as available by default
- Flowchart: `_01_add_book.svg`

### 2. **Register Member**
- Register new library members with ID, name, and email
- Members can borrow and return books
- Flowchart: `_02_register_member.svg`

### 3. **Borrow Book**
- Members can borrow available books
- Validates both book and member existence
- Checks book availability before borrowing
- Creates a loan record with unique ID (L001, L002, etc.)
- Flowchart: `_03_borrow_book.svg`

### 4. **Return Book**
- Return borrowed books using the loan ID
- Updates book availability status
- Closes the loan record
- Flowchart: `_04_return_book.svg`

### 5. **View Books**
- Display all books in the library
- Shows book ID, title, author, and availability status
- Flowchart: `_05_view_book.svg`

### 6. **View Members**
- Display all registered members
- Shows member ID, name, and email
- Flowchart: `_06_view_member.svg`

### 7. **View Loans**
- Display all loan records (active and closed)
- Shows loan ID, member name, book title, and status
- Flowchart: `_07_view_loan.svg`

### 8. **Exit**
- Gracefully exit the application
- Flowchart: `_08_exit.svg`

## 📁 Project Structure

```
Library-Management-System/
├── models.py              # Data models (Book, Member, Loan)
├── exceptions.py          # Custom exception classes
├── library_service.py     # Core business logic (LibraryService)
├── main.py               # Interactive CLI application (LibraryApp)
└── README.md             # This file
```

## 🏗️ Architecture

### models.py
- **Book**: Represents a library book with availability tracking
  - `book_id`, `title`, `author`, `available`
  - Methods: `borrow()`, `return_book()`

- **Member**: Represents a library member
  - `member_id`, `name`, `email`

- **Loan**: Represents a book lending transaction
  - `loan_id`, `book`, `member`, `borrow_date`, `return_date`, `is_active`
  - Methods: `close_loan()`

### exceptions.py
Custom exceptions for error handling:
- `BookNotFoundError`: Book doesn't exist
- `MemberNotFoundError`: Member doesn't exist
- `BookUnavailableError`: Book is already borrowed
- `BookNotBorrowedError`: Loan not found or already closed

### library_service.py
**LibraryService** class - Core business logic:
- `add_book(book_id, title, author)`: Add a new book
- `register_member(member_id, name, email)`: Register a new member
- `borrow_book(book_id, member_id)`: Borrow a book with validation
- `return_book(loan_id)`: Return a borrowed book
- `view_books()`: Get all books
- `view_members()`: Get all members
- `view_loans()`: Get all loans

### main.py
**LibraryApp** class - Interactive CLI:
- Menu-driven interface with 8 options
- Input validation and error handling
- User-friendly prompts and feedback

## 🚀 Usage

### Running the Application
```bash
python main.py
```

### Example Workflow

```
1. Add books to the library
   - Add Book ID: B001, Title: "Python Programming", Author: "John Doe"

2. Register members
   - Register Member ID: M001, Name: "Alice Smith", Email: "alice@example.com"

3. Borrow a book
   - Borrow Book B001 for Member M001
   - System generates Loan ID: L001

4. View all records
   - View Books: Shows all books with availability status
   - View Members: Shows all registered members
   - View Loans: Shows all loan transactions

5. Return a book
   - Return using Loan ID: L001
   - Book becomes available again

6. Exit the system
   - Choose option 8 to close the program
```

## 🔍 Error Handling

The system includes comprehensive error handling for:
- Missing books or members
- Attempting to borrow unavailable books
- Invalid loan IDs
- User input validation

All errors are caught and displayed in a user-friendly manner with ✗ or ✓ indicators.

## 💾 Data Persistence

Currently, the system stores data in memory during the session. To add persistence:
- Implement JSON/SQLite storage in `library_service.py`
- Add load/save methods for books, members, and loans
- Call these methods in `LibraryApp.__init__()` and `__exit__()`

## 📊 Data Flow

```
User Input → LibraryApp (main.py)
     ↓
LibraryService (library_service.py)
     ↓
Models (models.py)
     ↓
Database / Storage
```

## 🛠️ Future Enhancements

- Add fine system for overdue books
- Implement book reservation system
- Add search/filter functionality
- Database integration (SQLite/PostgreSQL)
- Web interface (Flask/Django)
- User authentication and roles
- Book rating and review system

## 📝 License

This project is provided as an educational example.

---

**Created**: May 2026  
**Repository**: russel0713/Library-Management-System
