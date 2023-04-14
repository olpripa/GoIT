from ex1 import get_name

def goodbuy(name):
    print(f'GoodBuy {name}')

def main ():
    name = get_name()
    goodbuy(name)

if __name__ == '__main__':
    main()