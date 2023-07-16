from src.screen import Screen

def main():
    a = 'easy'

    if a == 'easy':
        size = 8,10
        bombs = 0.1

    screen = Screen(670,670, size, bombs)
    screen.run()

if __name__ == '__main__':
    main()