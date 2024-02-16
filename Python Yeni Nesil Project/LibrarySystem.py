class Library:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(self.file_name, 'a+')
        self.Books=[] # List of Books
        self.read_file()
        self.Menu()
        

    def __del__(self):
        self.file.close()
    
    def Menu(self):
        print("1. Display Books")
        print("2. Add Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("q For Exit")
        
        choice = input("Enter your choice: \n ")
        
        if choice == '1':
            self.display_books()
        elif choice == '2':
            self.add_books()
        elif choice == '3':
            self.search_book()
        elif choice == '4':
            self.remove_book()
        elif choice == 'q':
            self.__del__()
        else:
            print("Invalid Choice")
            self.Menu()
            
    def read_file(self): # Dosyayı okuyup listeme ekleyen method.
        self.Books.clear()
        self.file.seek(0)
        lines = self.file.read().splitlines()
            
        for line in lines:
            book_info = line.strip().split(',')
            dict_book = {'Book Name': book_info[0], 
                         'Author': book_info[1], 
                         'Release Year': book_info[2], 
                         'Number Of Page': book_info[3]}
            
            self.Books.append(dict_book)
                
        
    
    def display_books(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        print("Kitaplar Listelendi: \n")
        for line in lines:
            book_info = line.strip().split(',')
            print(f"Book Name: {book_info[0]}, Author: {book_info[1]}, Release Year: {book_info[2]}, Number Of Page: {book_info[3]}\n")
        self.Menu() 
        
    def add_books(self):
        book_name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")
        release_year = input("Enter Release Year: ")
        number_of_page = input("Enter Number Of Page: ")
        
        self.file.write(f"{book_name},{author},{release_year},{number_of_page}\n")  # Write metoduyla dosyaya yazdım.
        
        self.read_file() #Dosyayı okuyup listemi güncelledim. Eklenenleri tekrar initteki listeme ekledim.
    
        self.Menu()
    
    def search_book(self):
        search = input("Enter Book Name: ")
        for book in self.Books:
            if search == book['Book Name']:
                print(book)
                break
        else:
            print("Book is Not Found")
            
        self.Menu()
        
    def remove_book(self):
        search = input("Enter Book Name: ")
        #I delete the book from the list.
        for book in self.Books:
            if search == book['Book Name']:
                self.Books.remove(book)
                break
        else:
            print("Book is Not Found")
            
        #I delete the book from the file.
        self.file.seek(0)
        lines = self.file.read().splitlines()
        self.file.seek(0)
        self.file.truncate() # Dosyayı temizledim.

        for line in lines:
            book_info = line.strip().split(',')
            if book_info[0] != search:
                self.file.write(line + '\n')         
        self.Menu()
        
if __name__ == '__main__':
    library = Library('books.txt')