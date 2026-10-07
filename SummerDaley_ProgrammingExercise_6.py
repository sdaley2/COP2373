import re

def validate_phone(phone_number):
    """Check the phone number format using a regular expression."""

    match = re.fullmatch(r"\d{3}-\d{3}-\d{4}", phone_number)
    return match

def validate_ssn(ssn):
    """Check the social security number format using a regular expression."""

    match = re.fullmatch(r"\d{3}-\d{2}-\d{4}", ssn)
    return match

def validate_zip(zip_code):
    """Check the zip code format using a regular expression."""

    match = re.fullmatch(r"\d{5}", zip_code)
    return match

def main():
    """Run the validation program."""

    phone_number = input("Please enter your phone number (XXX-XXX-XXXX): ")
    ssn = input("Please enter your social security number (XXX-XX-XXXX): ")
    zip_code = input("Please enter your 5-digit zip code: ")

    if validate_phone(phone_number):
        print("Phone number is valid")
    else:
        print("Phone number is invalid")

    if validate_ssn(ssn):
        print("Social security number is valid")
    else:
        print("Social security number is invalid")

    if validate_zip(zip_code):
        print("Zip code is valid")
    else:
        print("Zip code is invalid")

if __name__ == "__main__":
    main()