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