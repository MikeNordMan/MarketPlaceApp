from Marketplace import Marketplase
from Traider import Tr


def main():
    print('Start Main:')
    mp = Marketplase('Traiding','www.tr')
    mp.testClass()
    print('___________________________________')
    mp2 = Tr('LME', 'www.lme.com', 'проверка')
    mp2.pasrsing()
    mp2.testClass()
    print(mp2.nameMarket)



if __name__ == '__main__':
    main()
