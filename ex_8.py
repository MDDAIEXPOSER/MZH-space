def main():
    num = int(input())
    first_zaryad = num // 100
    x_factor = first_zaryad * 100
    second_z = num - x_factor
    second_q = second_z // 10
    third_z = num - x_factor - second_q*10
    print(third_z + second_q + first_zaryad)

if __name__ == "__main__":
    main()
