from src.screen import Screen

def main():
    a = 'easy'

    if a == 'easy':
        size = 8
        bombs = 10

    screen = Screen(400,400, size, bombs)
    screen.play()

if __name__ == '__main__':
    main()