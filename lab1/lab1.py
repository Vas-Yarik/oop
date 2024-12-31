class Book:
    books = []
    century = 19

    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.books.append(self)


book1 = Book('Граф Монте‑Кристо', 'Александр Дюма')

book2 = Book('Война и мир', 'Лев Толстой')

book3 = Book('Маленькие женщины', 'Луиза Мэй Олкотт')

book4 = Book('Гамлет', 'Уильям Шекспир')
book4.century = 17

book5 = Book('Мастер и Маргарита', 'Михаил Булгаков')
book5.century = 20

book6 = Book('Отверженные', 'Виктор Гюго')

book7 = Book('Приключения Тома Сойера', 'Марк Твен')

book8 = Book('Котлован', 'Андрей Платонов')
book8.century = 20

book9 = Book('Крёстный отец', 'Марио Пьюзо')
book9.century = 20

book10 = Book('Вишнёвый сад', 'Антон Чехов')
book10.century = 20

book11 = Book('Божественная комедия', 'Данте')
book11.century = 14

book12 = Book('Идиот', 'Фёдор Достоевский')

Book.books.sort(key=lambda book: book.name)
for b in Book.books:
    print(b.name, b.author, sep=' - ')
print()
Book.books.sort(key=lambda book: book.century)
for b in Book.books:
    print(f'{b.century} век - {b.name}')

with open('lab1.txt', 'w+', encoding="utf-8") as file:
    file.writelines(f'{i.name}, {i.author}, {i.century} век\n' for i in Book.books)
