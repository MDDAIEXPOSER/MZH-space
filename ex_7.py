def main():
    money = 1572
    k_items = int(input())
    items = money // k_items
    print(items)
    if k_items > 1572:
        print("Nope, too expensive - 0")
    else:
        print("Ye,",items)
if __name__ == "__main__":
    main()
