def main():
    sum = int(input())
    if sum % 2 == 0:
        while sum % 2 == 0:
            sum /= 2
        print(sum)
    elif sum % 2 != 0:
        sum = (sum * 15) / 100
        print('К оплате',sum)
    else:
        print('К оплате',sum)
if __name__ == "__main__":
    main()
