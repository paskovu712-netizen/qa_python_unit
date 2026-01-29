import pytest
from main import BooksCollector
    
class TestBooksCollector:
    
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Оно')

        assert len(collector.books_genre) == 2

    def test_set_book_genre_positive(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')

        assert 'Фантастика' == collector.books_genre['Дюна']

    def test_get_book_genre_positive(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        
        assert 'Фантастика' == collector.get_book_genre('Дюна')

    def test_get_books_with_specific_genre_one_book_positive(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')

        assert ['Дюна'] ==  collector.get_books_with_specific_genre('Фантастика')

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        
        assert {'Дюна': 'Фантастика'} == collector.get_books_genre()

    def test_get_books_for_children_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')

        assert ['Дюна'] ==  collector.get_books_for_children()

    def test_add_book_in_favorites_positive(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')

        assert ['Дюна'] == collector.favorites

    def test_delete_book_from_favorites_positive(self):
        collector = BooksCollector()
        collector.favorites.append('Дюна')

        assert None == collector.delete_book_from_favorites('Дюна')

    def test_get_list_of_favorites_books_one_book(self):
        collector = BooksCollector()
        collector.favorites.append('Дюна')

        assert ['Дюна'] == collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('book,genre', 
    [
        ('Дюна', 'Фантастика'),
        ('Оно', 'Ужасы'),
        ('Шерлок Холмс: Этюд в багровых тонах', 'Детективы'),
        ('Винни-Пух и все-все-все', 'Мультфильмы'),
        ('Двенадцать стульев', 'Комедии')
    ])
    def test_add_new_book_and_set_genre(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert genre == collector.books_genre[book]
