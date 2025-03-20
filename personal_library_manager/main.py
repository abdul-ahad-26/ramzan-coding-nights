# library Manager
# Features
"""
Add new book
delete book
update book
show all books
show book progress
search for a book
"""
# Imports
import json


class BookCollection:
    """A class to collection of books, allowing users to store and organize their reading material"""

    # constructor to initialize empty list and set up file storage
    def __init__(self):
        """Initialize a new book collection with an empty list set up file storage"""
        self.book_list = []
        self.storage_file = "books_data.json"
        self.read_from_file()

    # function to read books data from file
    def read_from_file(self):
        """Load saved books into a json file into memory,
        If file does not exits or is corrupted, start with an empty collection."""
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []

    # function to save books data to file
    def save_to_file(self):
        """Store the current book collection to a JSON file for permanent storage."""
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)

    # function to add new book
    def create_new_book(self):
        """Add a new book to the collection by gathering information from the user."""
        book_title = input("Enter book title: ")
        book_author = input("Enter author: ")
        publication_year = input("Enter publication year: ")
        book_genre = input("Enter genre: ")
        is_book_read = (
            input("have you read this book: (yes/no): \n").strip().lower() == "yes"
        )

        new_book = {
            "title": book_title,
            "author": book_author,
            "year": publication_year,
            "genre": book_genre,
            "read": is_book_read,
        }

        self.book_list.append(new_book)
        self.save_to_file()

    # function to delete book
    def delete_book(self):
        """Remove a book from the collection using its title."""
        book_title = input("Enter the title of the book to remove: ")

        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_to_file()
                print("Book removed successfully!\n")
                return
        print("Book not found!\n")

    # function to find the book
    def find_book(self):
        """Search for books in the collection by title or or author name."""
        search_type = input("Search by:\n 1.Title\n2. Author\nEnter your choice: ")
        search_text = input("Enter search term: ").lower()
        found_books = [
            book
            for book in self.book_list
            if search_text in book["title"] or search_text in book["author"]
        ]

        if found_books:
            print("Matching Books")
            for index, book in enumerate(found_books, 1):
                reading_status = "Read" if book["read"] else "Unread"
                print(
                    f"{index}. {book['title']} by {book['author']} - {book['genre']} -{reading_status} "
                )
        else:
            print("No matching book found")

    # function to update existing book
    def update_book(self):
        """Modify the details of an existing book in the collection."""
        book_title = input("Enter the title of the book you want to edit: ")
        for book in self.book_list:
            if book['title'].lower()==book_title.lower():
                print("Leave blank to keep existing value.")
                book["title"] = input(f"New title ({book['title']}): ") or book["title"]
                book["author"] = input(f"New author ({book['author']}): ") or book["author"]
                book["year"] = input(f"New year ({book['year']}): ") or book["year"]
                book["genre"] = input(f"New genre ({book['genre']}): ") or book["genre"]
                book["read"] = (input(f"Have you read this book? (yes/no): ").strip().lower() == "yes") 
                self.save_to_file()
                print("Book updated successfully!\n")
                return
        print("Book not found!\n")

    # function to show all books
    def show_all_books(self):
        """Display all book from the collection with their details"""
        if not self.book_list:
            print("Your collection is empty.\n")
            return
        
        print("Your book collection:")
        for index, book in enumerate(self.book_list, 1):
                reading_status = "Read" if book["read"] else "Unread"
                print(
                    f"{index}. {book['title']} by {book['author']} - {book['genre']} -{reading_status} "
                )

    # show book progress
    def show_reading_progress(self):
        """Calculate and display statistics about your reading progress."""
        total_books = len(self.book_list)
        completed_books = sum(1 for book in self.book_list if book["read"])
        completion_rate = (
            (completed_books / total_books *100) if total_books > 0 else 0
        )
        print(f"Total books in collection: {total_books}")
        print(f"Reading progress: {completion_rate:.2f}%\n")

    # function for menu
    def application_start(self):
        """Run the main application loop with a user-freindly menu interface."""
        while True:
            print("📚 Welcome to book collection Manager! 📚")
            print("1. Add a new book")
            print("2. Remove a book")
            print("3. Search for books")
            print("4. Update book details")
            print("5. Veiw all books")
            print("6. View reading progress")
            print("7. Exit")
            user_choice  = input("Please choose an option from (1-7): \n")

            if user_choice == "1":
                self.create_new_book()
            elif user_choice == "2":
                self.delete_book()
            elif user_choice == "3":
                self.find_book()
            elif user_choice == "4":
                self.update_book()
            elif user_choice == "5":
                self.show_all_books()
            elif user_choice == "6":
                self.show_reading_progress()
            elif user_choice == "7":
                self.save_to_file()
                print("Thank you for using Book Collection manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    book_manager = BookCollection()
    book_manager.application_start()
