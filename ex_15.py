def copod():
    string = input()
    pre_string = string.split(' ')
    res_string = pre_string[::-1]
    result = ' '.join(res_string)
    print(result)





def main():
    copod()

if __name__ == "__main__":
    main()
