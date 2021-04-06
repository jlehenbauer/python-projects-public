from chess import Board

def main():
    c = Board()

    c.set_standard()

    while True:
        print(c)
        if c.TURN:
            print("White, it's your turn.")
            # TODO: create verification for chess notation
            c.move(input("Enter your move: "))
        else:
            print("Black, it's your turn.")
            # TODO: create verification for chess notation
            c.move(input("Enter your move: "))



if __name__ == "__main__":
    main()