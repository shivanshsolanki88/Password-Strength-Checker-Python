import re

rockyou_file_path = "C:/Users/shiva/Downloads/rockyou.txt/rockyou.txt"

def load_common_passwords(file_path):
    common_passwords = set()
    try:
        with open(file_path, "r", encoding="latin-1") as file:
            for line in file:
                password = line.strip()
                common_passwords.add(password)
    except Exception as e:
        print(f"Error reading the rockyou.txt file: {e}")
    return common_passwords

def is_password_breached(password, common_passwords):
    return password in common_passwords

def check_password_strength(password):
    strength = {
        "length": False,
        "upper_lower_case": False,
        "digit": False,
        "special_char": False,
    }

    if len(password) >= 12:
        strength["length"] = True

    if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password):
        strength["upper_lower_case"] = True

    if re.search(r'\d', password):
        strength["digit"] = True

    if re.search(r'[\W_]', password):
        strength["special_char"] = True

    if strength["length"] and strength["upper_lower_case"] and strength["digit"] and strength["special_char"]:
        return "Strong"
    elif sum(strength.values()) >= 3:
        return "Medium"
    else:
        return "Weak"

def get_improvement_suggestions(password, strength):
    suggestions = []

    if len(password) < 8:
        suggestions.append("Your password is too short. Consider using at least 8 characters.")

    if not re.search(r'[a-z]', password):
        suggestions.append("Add at least one lowercase letter to your password.")

    if not re.search(r'[A-Z]', password):
        suggestions.append("Add at least one uppercase letter to your password.")

    if not re.search(r'\d', password):
        suggestions.append("Add at least one digit to your password.")

    if not re.search(r'[\W_]', password):
        suggestions.append("Add at least one special character to your password.")

    if password.lower() in ["password", "123456", "qwerty", "letmein", "welcome"]:
        suggestions.append("Avoid common patterns and easily guessable passwords like 'password', '123456', or 'qwerty'. Consider using a passphrase.")

    suggestions.append("For better protection, periodically change your password to stay secure.")

    return suggestions

def password_checker(password):
    common_passwords = load_common_passwords(rockyou_file_path)
    
    if is_password_breached(password, common_passwords):
        print(f"Your password '{password}' is found in the breach list! It's commonly used and easily cracked.")
        print("Recommendation: Change your password immediately to something unique and stronger!")
    else:
        print(f"Your password '{password}' is not found in the breach list.")

    strength = check_password_strength(password)
    print(f"Password Strength: {strength}")

    if strength == "Weak" or strength == "Medium":
        suggestions = get_improvement_suggestions(password, strength)
        print("\nSuggestions to improve your password:")
        for suggestion in suggestions:
            print(f"- {suggestion}")
    else:
        print("\nYour password is strong! Keep up the good work.")

if __name__ == "__main__":
    user_password = input("Enter your password to check its strength: ")
    password_checker(user_password)
