import requests


class Marketplase:
    '''Описание класса'''
    def __init__(self, name, url):
        self.nameMarket = name
        self.urlMarket = url


    def testClass(self):
        print(self.nameMarket)
        print(self.urlMarket)


    '''проверка работы сервера'''
    def get_Html(self):
        r = requests.get(self.urlMarket)
        if r.ok:
            print('Все Ок! Сервер отвечает!')
            return r.text
        else:
            print('Сервер не дает данных')
    '''Получение данных с сервера'''

    def printHTML(self):
        print(self.get_Html())





    '''Метод отправки валидированных в БД'''
    def setData(self):
        pass




