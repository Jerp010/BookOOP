from abc import ABC, abstractmethod

# Abstraction
class Displayable(ABC):
    @abstractmethod
    def display_info(self):  # Polymorphism
        pass

# OOP and Encapsulation
class Author:
    def __init__(self, name, nationality):
        self._name = name           # Encapsulation
        self._nationality = nationality  # Encapsulation

    def get_details(self):  # Instance Method
        return f"{self._name} ({self._nationality})"

    @classmethod
    def from_string(cls, info):  # Class Method
        name, nationality = info.split("-")
        return cls(name, nationality)

# Composition + Inheritance + Polymorphism
class Book(Displayable):
    def __init__(self, title, author):  # Composition: Author inside Book
        self._title = title             # Encapsulation
        self._author = author           # Encapsulation

    def display_info(self):  # Polymorphism
        print(f"Title: {self._title}")
        print(f"Author: {self._author.get_details()}")

def main():
    author1 = Author("George Orwell", "England")
    book1 = Book("1984", author1)

    author2 = Author.from_string("Haruki Murakami-Japan")
    book2 = Book("Kafka on the Shore", author2)

    book1.display_info()
    print("")
    book2.display_info()



if __name__ == "__main__":
    main()
