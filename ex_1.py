def su_m(q):
    if q == []:
        return 0
    else:
        summing = su_m(q[1:])
        summing = summing + q[0]
        return summing


def main():
    case = [16,17,18,19,20,21,22,23,24]
    summing = su_m(case)
    print(summing)


if __name__ == "__main__":
    main()
