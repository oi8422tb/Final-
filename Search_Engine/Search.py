import PySimpleGUI as sg 
import random
from read import article_dic


class Search():
    #Open The File To The Dictinary
    #self.open = pass
    #This Will Be For The Random Search Button
    def __init__(self):
        self.articles = article_dic

   


    def reg_Search(self, text):
        for key in self.articles:
            if text in key:
                return self.articles[key]
        return None





    def search_rand(self):
        return random.choice(list(self.articles.values()))

