def main():

    abscent = input()
    org_abs = abscent
    symbol_1 = "a"
    symbol_2 = "b"
    symbol_3 = "c"
    for sym in org_abs:
        key_a = org_abs.find(symbol_1)
        key_b = org_abs.find(symbol_2)
        key_c = org_abs.find(symbol_3)
    print(key_a)
    print(key_b)
    print(key_c)





if __name__ == "__main__":
    main()
