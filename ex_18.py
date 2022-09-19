def mine():
    conspect = input()
    short_1 = ('ическая')
    short_2 = ("ическое")
    short_3 = ("ический")
    short_4 = ("ические")
    if short_1 in conspect:
        conspect = conspect.replace(short_1, ".")
    if short_2 in conspect:
        conspect = conspect.replace(short_2, ".")
    if short_3 in conspect:
        conspect = conspect.replace(short_3, ".")
    if short_4 in conspect:
        conspect = conspect.replace(short_4, ".")
    print(conspect)
def main():
    mine()



if __name__ == "__main__":
    main()
