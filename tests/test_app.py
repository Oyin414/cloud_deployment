import sys
import os
from playwright.sync_api import Page, expect


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

# def test_get_books_request_successfully_returs():
#     client = app.test_client()
#     response = client.get("/books")
#     assert response.status_code == 200
#     assert response.json == [
#     {
#         "title": "The Gruffalo",
#         "author": "Julia Donaldson"
#     },
#     {
#         "title": "Ada Twist, Scientist",
#         "author": "Andrea Beaty"
#     },
#     {
#         "title": "The Girl Who Drank the Moon",
#         "author": "Kelly Barnhill"
#     },
#     {
#         "title": "Dragons in a Bag",
#         "author": "Zetta Elliott"
#     }
#     ]


def test_get_authors_request_successful():
    client = app.test_client()
    response = client.get("/authors")
    assert response.status_code == 200
    assert response.json == [
    {
        "name": "Julia Donaldson",
        "dob": "1948-09-16"
    },
    {
        "name": "Andrea Beaty",
        "dob": "1961-10-08"
    },
    {
        "name": "Kelly Barnhill",
        "dob": "1973-01-01"
    },
    {
        "name": "Zetta Elliott",
        "dob": "1979-11-11"
    }
]

# def test_books_list_successfully_rendered(page : Page):
#     page.goto("http://127.0.0.1:5001/books")

#     books = page.locator('li')

#     expected_books = [
#     'The Gruffalo by Julia Donaldson',
#     'Ada Twist, Scientist by Andrea Beaty',
#     'The Girl Who Drank the Moon by Kelly Barnhill',
#     'Dragons in a Bag by Zetta Elliott'
#     ]

#     actual_books = books.all_inner_texts()

#     assert actual_books == expected_books


    def test_form_submission_working(page : Page):
        page.goto("http://127.0.0.1:5001/books")

        page.get_by_label("title").fill("Twilight")
        page.get_by_label("author").fill("Stephenie Meyer")
        page.get_by_role("button", name="Submit").click()

        assert page.get_by_text("Twilight by Stephanie Meyer")