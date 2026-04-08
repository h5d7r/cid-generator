# Author: Mr. Velox
# GitHub: https://github.com/h5d7r

import random
import string
import pyperclip


CHARS = string.ascii_uppercase + string.digits


def generate_cid():
    up_part = f"UP{random.randint(0, 9999):04d}"
    cusa_part = f"CUSA{random.randint(0, 99999):05d}"
    last_part = "".join(random.choices(CHARS, k=15))
    return f"{up_part}-{cusa_part}_00-{last_part}"


def ask_count():
    while True:
        user_input = input("How many CIDs do you want to generate? ").strip()

        try:
            count = int(user_input)
            if count > 0:
                return count
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    count = ask_count()
    cids = [generate_cid() for _ in range(count)]
    output = "\n".join(cids)

    print("\nGenerated CIDs:\n")
    print(output)

    # Copy all lines at once
    pyperclip.copy(output)
    print("\nCopied to clipboard.")


if __name__ == "__main__":
    main()
