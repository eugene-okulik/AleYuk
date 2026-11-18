class Book:
    material = "Бумага"
    is_text = True

    def __init__(self, book_name, author, num_pages, isbn, is_reserved):
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.is_reserved = is_reserved


class SchoolTextbooks(Book):

    def __init__(self, school_subject, school_class, housing, book_name, author, num_pages, isbn, is_reserved):
        super().__init__(book_name, author, num_pages, isbn, is_reserved)
        self.school_subject = school_subject
        self.school_class = school_class
        self.housing = housing


alfabet = Book("Alfabet", "Folk", 33, "978-2-266-11156-0", False)
mowgli = Book("Mowgli", "Kipling", 100, "978-5-17-155736-2", False)
hobbit = Book("Hobbit", "Tolkien", 355, "978-5-17-114531-6", False)
odyssey = Book("Odyssey", "Homer", 233, "978-5-17-11156-6", False)
fairy_tales = Book("Fairy_tales", "Folk", 139, "978-5-17-12159-6", False)
hobbit.is_reserved = True
math_9 = SchoolTextbooks("Алгебра", "9", True, "Алгебра для 9 классов",
                         "Макарычев Ю.Н.", 200, "978-5-09-071722-9", False)
geometry_9 = SchoolTextbooks("Геометрия", "9", False,
                             "Геометрия для 9 классов", "Атанесян Л.С.",
                             244, "978-5-09-073883-5", False)
chemistry_9 = SchoolTextbooks("Химия", "9", False,
                              "Химия для 9 классов", "Шиманович Е.Е.",
                              176, "978-985-34-0189-9", False)
physics_9 = SchoolTextbooks("Физика", "9", False,
                            "Физика для 9 классов", "Дорофейчик В.В.",
                            255, "978-985-19-6827-1", False)
geography_9 = SchoolTextbooks("География", "9", False,
                              "География для 9 классов", "Щепилова А.В.",
                              149, "978-5-09-071854-7", False)
geography_9.is_reserved = True


def print_book(book):
    result = (f"Название: {book.book_name}, Автор: {book.author}, "
              f"страниц: {book.num_pages}, материал: {book.material}")
    if book.is_reserved:
        result += ", зарезервирована"
    print(result)


def print_school_textbooks(book):
    result = (f"Название: {book.book_name}, Автор: {book.author}, "
              f"страниц: {book.num_pages}, предмет: {book.school_subject}, класс: {book.school_class}")
    if book.is_reserved:
        result += ", зарезервирована"
    print(result)


print_book(alfabet)
print_book(mowgli)
print_book(hobbit)
print_book(odyssey)
print_book(fairy_tales)
print_school_textbooks(math_9)
print_school_textbooks(geometry_9)
print_school_textbooks(chemistry_9)
print_school_textbooks(physics_9)
print_school_textbooks(geography_9)
