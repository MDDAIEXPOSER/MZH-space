def main():
    itemc = input()
    its = itemc.split(" ")
    print(its)
    c_i = list(map(int, its))
    print(c_i)
    if c_i[0] < c_i[1] and c_i[1] < c_i[2] and c_i[0] < c_i[2]:
        print('Akcia ! Yout cost -', 10000/2)
    elif c_i[0] > c_i[1] and c_i[0] > c_i[2] and c_i[1] > c_i[2]:
        print('Akcia ! Your cost -', 10000/3)
    else:
        print('No akcia')



if __name__ == "__main__":
    main()
