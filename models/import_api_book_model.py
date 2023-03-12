from models.book_model import book_model
from models.author_model import author_model

book_model = book_model()
author_model = author_model()

class import_api_book_model():
#TO DO:inserts should be bulk 
   def insert(self,booklist,bookCnt):
        i=1
        #loop through each book
        for book in booklist:
            #check if isbn13 already exists if yes than just add to qty 
            isbn13=book.get('isbn13')
            updateCnt=book_model.update_qty_isbn13(isbn13)
            #if isbn not found insert book
            if updateCnt <= 0:
                #get authors from api data
                authorApi=book.get('authors')
                authorListApi = authorApi.split("/") 
                author_selected_list=[] #list of author ids to send to insert book
                #check if author already exists in sytem if yes get id or else insert and get id
                for author in authorListApi:
                    author_selected_list.append(author_model.insert_if_not_exists(author))
                #get book title from api data
                title=book.get('title')
                qty='1'
                #insert book
                book_model.insert(title,isbn13,qty,author_selected_list)
            # print(isbn13)
            if i < bookCnt: i=i+1
            else: break #break when reqd count is met

        return "Books Imported Successfully"