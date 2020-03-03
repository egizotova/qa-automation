import csv
import json
from random import randint


def write_json_to_file(file_path: str, data):
    with open(file_path, "w") as write_file:
        json.dump(data, write_file)


def read_from_csv(file_path: str):
    with open(file_path) as File:
        reader = csv.reader(File)
        books = []
        for row in reader:
            books.append(row)
    return books


def read_from_json(file_path: str):
    with open(file_path) as json_file:
        data = json.load(json_file)
        return data


def assign_books_to_users(books: list, users: dict):
    users_with_book = []
    books_size = len(books)
    for user in users:
        random_books = []
        for i in range(0, randint(0, 4)):
            one_book = books[randint(1, books_size - 1)]
            random_books.append(
                {
                    "title": one_book[0],
                    "author": one_book[1],
                    "height": one_book[2]
                }
            )
        users_with_book.append(
            {
                'name': user['name'],
                'gender': user['gender'],
                'address': user['address'],
                'books': random_books
            }
        )
    return users_with_book


def generate_data(csv_file, json_file, output_file):
    books = read_from_csv(csv_file)
    users = read_from_json(json_file)
    users_with_books = assign_books_to_users(books, users)
    write_json_to_file(output_file, users_with_books)


if __name__ == '__main__':
    generate_data(csv_file='books.csv', json_file='users.json', output_file='result.json')
