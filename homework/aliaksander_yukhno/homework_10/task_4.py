PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

PRICE_LIST = PRICE_LIST.split()
PRICE_LIST = [int(x[:-1]) if PRICE_LIST.index(x) % 2 != 0 else x for x in PRICE_LIST]
PRICE_LIST = dict(zip(PRICE_LIST[::2], PRICE_LIST[1::2]))
print(PRICE_LIST)
