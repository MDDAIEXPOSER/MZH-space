def main():
    suma = 0
    number = int(input())
    criteria_2 = number % 10
    while number != 0:
        suma = suma + number % 10
        number = number // 10
    if suma % 3 == 0:
        if criteria_2 % 2 == 0:
            print("defenning 6")
    else:
        print('Not Ok')

if __name__ == "__main__":
    main()
