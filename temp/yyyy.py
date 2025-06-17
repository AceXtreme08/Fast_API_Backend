def valid_password(password: str):
    has_letter = False
    has_number = False

    for char in password:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_number = True
    return has_letter and has_number


def get_password_input(password: str):
    if len(password) < 8 or not valid_password(password):
        raise ValueError("error pass")



