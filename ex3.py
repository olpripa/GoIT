import sys
from ex1 import main as greeting
from ex2 import main as exiting

def main():
    try:
        if sys.argv[1] == 'greet':
            greeting()
        elif sys.argv[1] == 'byu':
            exiting()
        else:
            print('Unknown argument')
    except IndexError:
        print("argument must be 'greet' or 'buy'")

if __name__ == '__main__':
    main()