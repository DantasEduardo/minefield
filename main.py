import argparse
from src.screen import Screen

def check_difficulty():
    difficulty = input("What difficulty do you want to play?\n 1-)easy    2-)medium\n 3-)hard\n")
    if difficulty == '1' or difficulty=='easy':
        main('easy')
    elif difficulty == '2' or difficulty=='medium':
        main('medium')
    elif difficulty == '3' or difficulty=='hard':
        main('hard')
    else:
        print("Please select a valid difficulty")
        check_difficulty()

def main(difficulty):
    if difficulty == 'easy':
        size = 8,10
        bombs = 0.1

    if difficulty == 'medium':
        size = 18,14
        bombs = 0.16

    if difficulty == 'hard':
        size = 24,20
        bombs = 0.2

    screen = Screen(600,600, size, bombs)
    screen.run()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-e','--easy', default=False, action='store_true', 
                    help='start th game in easy mode')
    parser.add_argument('-m','--medium', default=False, action='store_true', 
                    help='start th game in medium mode')
    parser.add_argument('-a','--hard', default=False, action='store_true', 
                help='start th game in hard mode')
    args = parser.parse_args()

    if args.easy:
        main('easy')
    elif args.medium:
        main('medium')
    elif args.hard:
        main('hard')
    else:
        check_difficulty()