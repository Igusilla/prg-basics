class Ebook:
    def __init__(self, title, author, number_of_pages, current_page):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.current_page = current_page
        self.opened = False
    
    def book_open(self):
        self.opened = True
    
    def book_close(self):
        self.opened = False
        if self.opened:
            def next_page(self):
                self.current_page += 1
                if self.current_page > self.number_of_pages:
                    self.current_page = self.number_of_pages
            
            def previous_page(self):
                self.current_page -= 1
                if self.current_page < self.number_of_pages:
                    self.current_page = 1

            def book_status(self):
                print(f"Title: {self.title}, Author: {self.author}, Number of pages: {self.number_of_pages}, Current page: {self.number_of_pages}")