class Book:
    def __init__(self, title, author, year):
       
        self.title = title 
        self.author = author  
        self.year = year  

    def display_info(self):
       
        print("Title:", self.title)  
        print("Author:", self.author)  
        print("Year:", self.year) 
        print("---")  



book1 = Book("Cây cam ngọt của tôi", " José Mauro de Vasconcelos", 2012)
book2 = Book("Pride and Prejudice", "Jane Austen", 1813)


book1.display_info()
book2.display_info()