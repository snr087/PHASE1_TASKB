class Book:
    def __init__(self, title, author, publisher, price):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.price = price
        self.author_royalty = 0
    
    # Getter methods
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_publisher(self):
        return self.publisher
    
    def get_price(self):
        return self.price
    
    def get_author_royalty(self):
        return self.author_royalty
    
    # Setter methods
    def set_title(self, title):
        self.title = title
    
    def set_author(self, author):
        self.author = author
    
    def set_publisher(self, publisher):
        self.publisher = publisher
    
    def set_price(self, price):
        self.price = price
    
    # royalty amount
    def royalty(self, copies_sold):
        if copies_sold <= 500:
            royalty_percentage = 0.10
        elif copies_sold <= 1500:
            royalty_percentage = 0.125
        else:
            royalty_percentage = 0.15
        
        royalty_amount = royalty_percentage * self.price * copies_sold
        
        return royalty_amount
        
class Ebook(Book):
    def __init__(self, title, author, publisher, price, ebook_format):
        super().__init__(title, author, publisher, price)
        self.ebook_format = ebook_format
    
    # Getter and setter 
    def get_ebook_format(self):
        return self.ebook_format
    
    def set_ebook_format(self, ebook_format):
        self.ebook_format = ebook_format
    
    # Override royalty() method 
    def royalty(self, copies_sold):
        gst_percentage = 0.12
        royalty_amount = super().royalty(copies_sold)
        gst_deduction = gst_percentage * royalty_amount
        
        return royalty_amount - gst_deduction 
        
