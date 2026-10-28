from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("http://127.0.0.1:5001")

    h1 = page.locator("h1")
    expect(h1).to_have_text("Welcome to Acereads")



    # def test_book_list_contains_all_books(page: Page):
    # connection = DatabaseConnection()
    # connection.connect()
    # connection.seed("./seeds/books.sql")

    # # the rest is unchanged
