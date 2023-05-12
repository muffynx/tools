def get_base(num_str):
    if num_str.startswith("0b") or set(num_str) <= {"0", "1"}:
        return '2 binary'
    elif num_str.startswith("0o") or num_str.startswith("1"):
        return '8 octal'
    elif num_str.endswith("6e") or num_str.find("6c") or num_str.find("6f") or num_str.find("6d")or set(num_str) <= {"6c","0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"}:
        return '16 hexadecimal'
    elif num_str.isdigit():
        return '10 decimal'
    elif set(num_str) <= {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"}:
        return 'unknown base (likely base 16)'
    else:
        return 'unknown base'


def octal_to_word(num_str):
    # Remove leading zeros from the octal string
    num_str = num_str.lstrip('0')
    
    # Pad the string with zeros if its length is not a multiple of 3
    if len(num_str) % 3 != 0:
        num_str = '0' * (3 - len(num_str) % 3) + num_str
    
    # Convert the octal string to a list of decimal integers
    decimal_list = [int(num_str[i:i+3], 8) for i in range(0, len(num_str), 3)]
    
    # Convert the decimal integers to ASCII characters and concatenate them
    word = ''.join([chr(d) for d in decimal_list])
    
    return word


num_str = input("Enter a number: ")
num_str = num_str.replace(" ", "")
base = get_base(num_str)

if base == '16 hexadecimal':
    hex_bytes = bytes.fromhex(num_str)
    ascii_str = hex_bytes.decode('ascii')
    print(f"{base} {num_str} is '{ascii_str}' in ASCII.")
elif base == '2 binary':
    binary_bytes = int(num_str, 2).to_bytes((len(num_str) + 7) // 8, byteorder='big')
    ascii_str = binary_bytes.decode('ascii')
    print(f"{base} {num_str} is '{ascii_str}' in ASCII.")
elif base == '8 octal':
    ascii_str2 = octal_to_word(num_str)
    print(f"{base} {num_str} is '{ascii_str2}' in ASCII.")



else:
    print("unknown base")
