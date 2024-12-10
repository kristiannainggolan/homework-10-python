class school_library:
    def __init__(self) -> None:
        self.books = {}
        self.students = {}

    def add_book(self, title, author, available_copies):
        if title not in self.books:
            self.books[title] = {
                "autor" : author,
                "available_copies" : available_copies
            }
        else:
            raise Exception("Book already exist")
        

    def register_student(self, id, name):
        if id not in self.students:
            self.students[id] = {
                "name" : name,
                "borrowed_book" : []
            }
        else:
            raise Exception("Student already exist")
        
    def borrow_book(self, student_id, book_title):
        if student_id not in self.students:
            return Exception(f"Student ID {student_id} not exist")
        
        if book_title not in self.books or self.books[book_title]["available_copies"] <= 0:
            return Exception(f"Book {book_title} not exist")
        
        self.books[book_title]["available_copies"] -=1
        self.students[student_id]["borrowed_book"].append(book_title)
        print(f"{book_title} borrowed by {self.students[student_id]['name']}")

    def return_book(self, student_id, book_title):
        if student_id not in self.students:
            return Exception(f"Student ID {student_id} not exist")
        
        if book_title not in self.students[student_id]["borrowed_book"]:
            return Exception(f"Book {book_title} does not borrowed by {self.students[student_id]['name']}")
        
        self.books[book_title]["available_copies"] +=1
        self.students[student_id]["borrowed_book"].remove(book_title)
        print(f"{book_title} returend by {self.students[student_id]['name']}")

    def display_book(self):
        for title, details in self.books.items():
            print(f"Book : {title}, Author : {details['autor']}, available copies : {details['available_copies']}")

    def display_student(self):
        for id, details in self.students.items():
            print(f"Student ID : {id}, Name : {details['name']}, Borrowed book : {details['borrowed_book']},")

    def display_by_author(self, author):
        list_book = []
        for title, details in self.books.items():
            if details['autor'] == author:
                list_book.append(title)

        return list_book


sl = school_library()
sl.books = {}
sl.students = {}

sl.add_book("judul1", "tian",10)
sl.add_book("judul2", "jacob",10)
sl.add_book("harry potter", "JK Rowling",10)
sl.add_book("LOR", "JK Rowling",10)

sl.register_student(1, "student1")
sl.register_student(2, "student2")


sl.borrow_book(1,"judul1")
sl.borrow_book(2,"judul2")
sl.return_book(1,"judul1")

sl.display_book()
sl.display_student()

print(sl.display_by_author("JK Rowling"))
# print(sl.books)
# print(sl.students)


'''
Modif register student, terdapat list buat buku yg dipinjam, 1 title buku
dictionary buku available_copies 

def borrowed books
def returened books
'''