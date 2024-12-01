"""
Thomas Dallimore
CP1404 Prac10
Wikipedia Exercise
"""

import wikipedia


def main():
    while True:
        title_page = input("Enter a page title: ").strip()
        if not title_page:
            break
        try:
            page = wikipedia.page(title_page, auto_suggest=False)
            print(page.summary)

        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following or start a new search:")
            print(e.options)

        except wikipedia.exceptions.PageError:
            print("Page id does not match any pages. Try again:")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()


