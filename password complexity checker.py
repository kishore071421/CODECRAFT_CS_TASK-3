import math
import re

COMMON_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "admin", "letmein",
    "welcome", "iloveyou", "monkey", "dragon", "football", "login"
}

def calculate_entropy(password):
    """Estimate password entropy in bits."""
    charset = 0
    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[^A-Za-z0-9]", password):
        charset += 33
        
    if charset == 0:
        return 0
    
    return round(len(password) * math.log2(charset), 2)


def check_patterns(password):
    patterns = [
        "qwerty", "asdf", "zxcv", 
        "1234", "1111", "abcd"
    ]
    
    password_lower = password.lower()
    for pattern in patterns:
        if pattern in password_lower:
            return True
    return False


def password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 25
    elif len(password) >= 8:
        score += 10
    else:
        feedback.append("Password too short. Minimum recommended length is 8.")

    # Contains uppercase
    if re.search(r"[A-Z]", password):
        score += 15
    else:
        feedback.append("Add at least one uppercase letter.")

    # Contains lowercase
    if re.search(r"[a-z]", password):
        score += 15
    else:
        feedback.append("Add at least one lowercase letter.")

    # Contains numbers
    if re.search(r"[0-9]", password):
        score += 15
    else:
        feedback.append("Add at least one number.")

    # Contains symbols
    if re.search(r"[^A-Za-z0-9]", password):
        score += 15
    else:
        feedback.append("Add at least one special character.")

    # Repeated characters
    if re.search(r"(.)\1{2,}", password):
        feedback.append("Avoid repeating characters like 'aaa' or '111'.")
        score -= 10

    # Common password
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("This password is too common. Choose something unique.")
        score -= 40

    # Pattern detection
    if check_patterns(password):
        feedback.append("Avoid keyboard patterns like qwerty, asdf, or 1234.")
        score -= 20

    # Entropy calculation
    entropy = calculate_entropy(password)
    if entropy > 50:
        score += 20
    elif entropy > 30:
        score += 10
    else:
        feedback.append("Password entropy is low. Increase complexity.")

    score = max(0, min(score, 100))

    return score, entropy, feedback


# Main program
if __name__ == "__main__":
    pwd = input("Enter a password to test: ")

    score, entropy, suggestions = password_strength(pwd)

    print("\n=== PASSWORD ANALYSIS ===")
    print(f"Strength Score: {score}/100")
    print(f"Entropy: {entropy} bits")

    if score >= 80:
        print("Strength: VERY STRONG")
    elif score >= 60:
        print("Strength: STRONG")
    elif score >= 40:
        print("Strength: MEDIUM")
    else:
        print("Strength: WEAK")

    print("\nSuggestions:")
    if suggestions:
        for s in suggestions:
            print(" -", s)
    else:
        print("Your password is strong with no major issues.")
