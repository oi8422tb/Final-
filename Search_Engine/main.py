import PySimpleGUI as sg
from GUI import window
from Search import Search
import webbrowser


def main():
    search = Search()
    h = 600
    w = 800
    g = window(w,h)
    while True:
        event, value = g.window.read()
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED:
            break
        if event == 'Search':
            result = search.reg_Search(value[0])
        elif event == 'Random Search':
            result = search.search_rand()
        else:
            continue
        if result is None:
            print("Article not found")
        else:
            print("The article is", result)
            webbrowser.open(result)








main()