import re
import math

# Common weak passwords list
COMMON_PASSWORDS = [
    "password", "123456", "123456789", "qwerty", "abc123",
    "111111", "12345678", "iloveyou", "admin"
]

def calculate_entropy(password):
    pool = 0

    if re.search(r'[a-z]', password):
        pool += 26
    if re.search(r'[A-Z]', password):
        pool += 26
    if re.search(r'[0-9]', password):
        pool += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        pool += 32

    if pool == 0:
        return 0

    entropy = len(password) * math.log2(pool)
    return round(entropy, 2)

def password_strength(password):

    score = 0
    feedback = []

    # Length Check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short.")

    # Uppercase
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Numbers
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Symbols
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add special characters (!,@,#,$ etc).")

    # Common Password Check
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("This password is very common. Avoid using it.")
        score -= 1

    entropy = calculate_entropy(password)

    return score, entropy, feedback


def main():
    print("\n===== PASSWORD STRENGTH CHECKER =====\n")
    password = input("Enter a password to analyze: ")

    score, entropy, feedback = password_strength(password)

    print("\n-----------------------------------")
    print(f"Password Score: {score}/6")
    print(f"Password Entropy: {entropy} bits")

    # Rating
    if score <= 2:
        print("Strength: ❌ Weak")
    elif score <= 4:
        print("Strength: ⚠️ Moderate")
    else:
        print("Strength: ✅ Strong")

    print("\nFeedback:")
    if len(feedback) == 0:
        print("✔ Your password looks good!")
    else:
        for f in feedback:
            print("- " + f)

    print("-----------------------------------\n")


if __name__ == "__main__":
    main()
