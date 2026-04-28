import re
import random
import string

# -------- LEVEL 1 --------
def generate_stronger_password(password):
    new_password = password

    if not re.search(r"[A-Z]", new_password):
        new_password = new_password.capitalize()

    if not re.search(r"[0-9]", new_password):
        new_password += str(random.randint(10, 99))

    if not re.search(r"[!@#$%^&*]", new_password):
        new_password += random.choice("!@#$%^&*")

    while len(new_password) < 12:
        new_password += random.choice(string.ascii_letters + string.digits)

    return new_password


def generate_multiple(password, count=3):
    return list({generate_stronger_password(password) for _ in range(count)})


# -------- LEVEL 2 (ULTRA RANDOM) --------
def generate_ultra_strong(length=16):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-="
    return ''.join(random.choice(chars) for _ in range(length))


# -------- LEVEL 3 (CUSTOM BASED) --------
def generate_custom_password(base_word):
    word = base_word.capitalize()

    # Mix with random
    extras = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(4))
    special = random.choice("!@#$%^&*")

    return word + special + extras + str(random.randint(100, 999))


# -------- ANALYZER --------
def analyze_password(password):
    score = 0
    suggestions = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        suggestions.append("Increase length")
    else:
        suggestions.append("Increase length")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add numbers")

    if re.search(r"[!@#$%^&*]", password):
        score += 2
    else:
        suggestions.append("Add special characters")

    if score <= 3:
        return "Weak ❌", suggestions
    elif score <= 6:
        return "Medium ⚠️", suggestions
    else:
        return "Strong ✅", suggestions


# ================= MAIN =================
password = input("Enter your password: ")

strength, suggestions = analyze_password(password)

print("\nStrength:", strength)

if suggestions:
    print("\nSuggestions to improve:")
    for s in suggestions:
        print("-", s)

    print("\n🔐 Strong Password Suggestions:")
    strong_list = generate_multiple(password, 3)

    for i, p in enumerate(strong_list, 1):
        print(f"{i}. {p}")

# -------- ASK FOR ULTRA MODE --------
choice = input("\nDo you want auto-generated strongest password? (yes/no): ").lower()

if choice == "yes":

    while True:
        print("\nChoose what to include:")
        print("1. Name")
        print("2. Pet Name")
        print("3. Place/House")
        print("4. Custom Word")
        print("5. Exit")

        option = input("Enter choice: ")

        if option == "5":
            print("Exiting... 👋")
            break

        base = input("Enter your word: ")

        print("\n🔐 Custom Strong Password:")
        print("👉", generate_custom_password(base))

else:
    print("\n👍 Done.")