def main():
    num = int(input())
    numi = 0
    while num > 0:
        numeo = num % 10
        num = num // 10
        numi = numi * 10
        numi = numi + numeo
    print(numi)


if __name__ == "__main__":
    main()
