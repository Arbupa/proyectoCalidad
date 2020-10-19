def opening_screen():
    with open("pokemon_logoTB.txt") as reader:
        content = reader.read()
        print(content)

def main():
    opening_screen()


if __name__ == "__main__":
    main()