import streamlit as st
import re
import random
import string

st.title("🔐 Password Analyzer")

password = st.text_input("Enter your password", type="password")

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


def generate_custom_password(base_word):
    word = base_word.capitalize()
    extras = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(4))
    special = random.choice("!@#$%^&*")
    return word + special + extras + str(random.randint(100, 999))


if password:
    strength, suggestions = analyze_password(password)

    st.subheader(f"Strength: {strength}")

    if suggestions:
        st.write("### Suggestions:")
        for s in suggestions:
            st.write("- ", s)

    if st.button("Generate Strong Password"):
        st.write("🔐 Example:")
        st.code(generate_custom_password(password))


# Custom generator
st.write("## Custom Password Generator")
base = st.text_input("Enter name / pet / place")

if st.button("Generate Custom Password"):
    if base:
        st.code(generate_custom_password(base))
