"""Simple Decimal to Binary and Hexadecimal Number Converter."""


def main():
    user_input = input("Enter a decimal integer: ").strip()

    try:
        decimal_number = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a whole decimal number (for example: 25).")
        return

    binary_result = bin(decimal_number)
    hex_result = hex(decimal_number)

    print(f"Decimal:     {decimal_number}")
    print(f"Binary:      {binary_result} (without prefix: {binary_result[2:] if decimal_number >= 0 else '-' + binary_result[3:]})")
    print(f"Hexadecimal: {hex_result} (without prefix: {hex_result[2:].upper() if decimal_number >= 0 else '-' + hex_result[3:].upper()})")


if __name__ == "__main__":
    main()
