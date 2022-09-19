import random

def main():
    print('Welcome dude !')
    counter = 0
    start_game = input()
    if start_game.lower() == 'game':
        while counter < 3:
            print('Wth num?')
            num = int(input())
            if num == 5:
                print('OK, you won')
                break
            else:
                print("try enother")
                counter += 1
        print('Game OVER')

    else:
        print('Nope')



if __name__ == "__main__":
    main()
