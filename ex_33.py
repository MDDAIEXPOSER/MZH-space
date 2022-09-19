def main():
    l_char = ["=","?","*","^","$","№","@","_"]
    l = []

    print('Enter logname:')
    loG_name = input()
    for i in loG_name:
        if i in l_char:
            l.append(i)
        else:
            break
    print(' '.join(l))







if __name__ == "__main__":
    main()
