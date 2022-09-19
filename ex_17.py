def bio():
    name_surn = input()
    name = name_surn.split(' ')
    surname = name[0]
    short_names = name[1][0]
    short_oldname = name[2][0]
    print(surname, short_names+'.'+short_oldname+'.')


def main():
    bio()


if __name__ == "__main__":
    main()
