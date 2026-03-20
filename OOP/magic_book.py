class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}, {self.num_pages} pages"
    
    def __eq__(self, value):
        return self.title == value.title and self.author == value.author
    
    def __lt__(self, value):
        return self.num_pages < value.num_pages
    
    def __gt__(self, value):
        return self.num_pages > value.num_pages

    def __add__(self, value):
        return f"{self.num_pages + value.num_pages} pages"
    
    def __contains__(self, value):
        return value in self.title or value in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        if key == "author":
            return self.author
        if key == "num_pages":
            return self.num_pages
        else:
            return "Invalid key"
        

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
book3 = Book("1984", "George Orwell", 328)
book4 = Book("White Nights", "Fyodor Dostoevsky", 100)
book5 = Book("White Nights", "Fyodor Dostoevsky", 120)

print(book1)
print(book4 == book5)
print(book1 < book2)
print(book3 > book2)
print(book1 + book4)
print("Great" in book1)
print(book1["author"])