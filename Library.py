class Book:
    '''Класс Book, хранит индекс, название, автора, описание и жанр.'''
    def __init__(self, index, title, author, description, genre):
        self.index = index
        self.title = title
        self.author = author
        self.description = description
        self.genre = genre

class Library:
    '''Класс Library, добавление, удаление, список и поиск книг.'''
    def __init__(self):
        self.books = []

    def add_book(self, book) -> None:
        '''Добавление книги.'''
        self.books.append(book)

    def print_genres(self) -> None:
        '''Вывод существующих жанров.'''
        print(f'Существующие жанры: {set(book.genre for book in self.books)}')

    def remove_book(self, keyword) -> None:
        '''Удаление книги по названию или индексу.'''
        for book in self.books:
            if str(book.title) == keyword or str(book.index) == keyword:
                self.books.remove(book)
        
    def search_books(self, keyword) -> list:
        '''Поиск книг по ключевому слову.'''
        return [book for book in self.books if keyword in book.title or keyword in book.author]
    
    def search_books_genre(self, keyword) -> list:
        '''Поиск книг по жанру.'''
        return [book for book in self.books if keyword in book.genre]

def main():
    library = Library()

    # Создаем 5 книг и добавляем их в базу данных
    book1 = Book(len(library.books), "Земляничная весна", "Стивен Кинг", "Стивен Кинг (в то время — 21-летний студент) точными мазками рисует жуткий в общем-то мир с его особыми цветами, звуками и даже запахами. ", "Ужасы")
    library.add_book(book1)
    book2 = Book(len(library.books), "Пожиратели тьмы: Токийский кошмар»", "Ричард Ллойд Перри", "Это невыдуманная история исчезновения молодой англичанки Люси Блэкман в Токио и журналистское расследование, написанное увлекательнее многих детективов.", "Детектив")
    library.add_book(book2)
    book3 = Book(len(library.books), "Темные тайны", "Гиллиан Флинн", "За расследование убийства семьи в Канзасе берется не полиция (она уже давно нашла виновного, а суд приговорил его к пожизненному заключению), а свидетель преступления — женщина по имени Либби.", "Детектив")
    library.add_book(book3)
    book4 = Book(len(library.books), "Дело сердца. 11 ключевых операций в истории кардиохирургии", "Томас Моррис", "Эта книга — отличный пример того, что называется пресловутым «сторителлингом»", "Фантастика")
    library.add_book(book4)
    book5 = Book(len(library.books), "Тысяча и одна ночь отделения скорой помощи", "Батист Болье", "Это бесконечная череда рассказов про людей, оказавшихся в больнице.", "Комедия")
    library.add_book(book5)

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Список книг")
        print("3. Поиск книги")
        print("4. Поиск книги по жанру")
        print("5. Подробная информация о книге")
        print("6. Удалить книгу")
        print("7. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            description = input("Введите описание книги: ")
            library.print_genres()
            genre = input("Введите жанр книги: ")
            book = Book(len(library.books), title, author, description, genre)
            library.add_book(book)
            print("Книга успешно добавлена!")

        elif choice == "2":
            print("\nСписок книг:")
            for book in library.books:
                print(f"{book.index}. {book.title} ({book.author})")

        elif choice == "3":
            keyword = input("Введите ключевое слово для поиска: ")
            search_results = library.search_books(keyword)
            if search_results:
                print("\nРезультаты поиска:")
                for book in search_results:
                    print(f"{book.title} ({book.author})")
            else:
                print("Книги не найдены.")
        
        elif choice == '4':
            library.print_genres()
            keyword = input("Введите жанр книги: ")
            search_results = library.search_books_genre(keyword)
            print("\nРезультаты поиска:")
            if search_results:
                for book in search_results:
                    print(f"{book.title} ({book.author})")
            else:
                print("Книги не найдены.")
                
        elif choice == "5":
            keyword = input("Введите название книги или ее индекс для просмотра подробной информации: ")
            for book in library.books:
                if str(book.title) == keyword or str(book.index) == keyword:
                    print(f"\nИндекс: {book.index}")
                    print(f"Название: {book.title}")
                    print(f"Автор: {book.author}")
                    print(f"Описание: {book.description}")
                    print(f"Жанр: {book.genre}")
                    break
            else:
                print("Книга не найдена.")
        
        elif choice == "6":
            keyword = input("Введите название книги или ее индекс для удаления: ")
            library.remove_book(keyword)
            print("Книга успешно удалена!")

        elif choice == "7":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()