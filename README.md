🔐 Password Strength Checker (Python)

A comprehensive Python tool that evaluates the strength, entropy, and security risks of user-provided passwords.
The program checks length, character diversity, patterns, repetitions, entropy score, and common password lists to produce a final strength rating.

🚀 Features
✔ Entropy Calculation

Estimates password entropy in bits using character-set size.

Shows how mathematically strong the password is.

✔ Pattern Detection

Detects weak patterns such as:

qwerty, asdf, zxcv

1234, 1111, abcd

✔ Security Checks

Uppercase letters

Lowercase letters

Numbers

Special characters

Repeated characters (e.g., aaa, 111)

Known common passwords

✔ Scoring System (0–100)

Password is categorized as:

Very Strong

Strong

Medium

Weak

✔ Clear Feedback

Provides human-readable suggestions to improve password safety.

📂 Project Structure
Password-Strength-Checker/
│
├── password_checker.py
└── README.md

🧠 How Entropy Works

Entropy formula used:

entropy = length × log2(character_set_size)


Higher entropy = harder for attackers to brute-force.

▶️ Running the Program
python password_checker.py


Sample Output:

=== PASSWORD ANALYSIS ===
Strength Score: 72/100
Entropy: 44.5 bits
Strength: STRONG

Suggestions:
 - Add at least one uppercase letter.
 - Avoid keyboard patterns like qwerty, asdf, or 1234.

🏆 Author

B BHARATH KISHORE

📄 License

Free to use for learning and educational purposes.
