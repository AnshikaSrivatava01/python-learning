def get_valid_number():
    while True:
        entry = input("Enter a valid float or integer:").strip()
        try:
            val=float(entry)
            return val 
        except ValueError:
            print(f"'{entry}' is invalid. Please try again")

valid_val = get_valid_number()
print(f"You entered: {valid_val}")            