def main():
    weight = int(input())
    height = int(input())
    height_ultra = height**2
    IMT = (weight / height_ultra)
    print("Result - ", round(IMT, 6))


if __name__ == "__main__":
    main()
