
import re
import getpass

COMMON_PASSWORDS = {
    "password", "password123", "12345678",
    "qwerty123", "admin123", "welcome123"
}

def check_password(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1
    else:
        suggestions.append("Consider using 12 or more characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add a number.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add a special character.")

    if password.lower() in COMMON_PASSWORDS:
        return "Weak", ["This is a commonly used password. Choose a unique one."]

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, suggestions


def main():
    print("=== Password Strength Checker ===")
    password = getpass.getpass("Enter a test password: ")

    strength, suggestions = check_password(password)
    print("\nStrength:", strength)

    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("All basic checks passed!")

    print("\nNote: This is an educational checker,")
    print("not a guarantee against password attacks.")


if __name__ == "__main__":
    main()
