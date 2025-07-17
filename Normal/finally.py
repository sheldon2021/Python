def main():
    try:
        n=int(input('enter a number'))
        print(n)
        return n


    except Exception as e:
        print(e)
        return e

    finally:
        print("hey i am inside finally")


main()

# finally is used in a function itll run even when return is used in try or except itll run neverthless 