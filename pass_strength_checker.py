import streamlit as st
import re
import random
import string

def password_strength(password):
    score = 0 #initialize score list to store the score of each condition

    feedback = []  #initialize feedback list to store the feedback of each condition

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❗ Password length should be at least 8 characters")
        
    if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
        score += 1
    else:
        feedback.append("❗ Password should contain both uppercase and lowercase letters")

    if re.search(r"\d",password):
        score += 1
    else: 
        feedback.append("❗ Password should contain at least one number")

    if re.search(r"[ !@#$%^&*()_+{}\[\]:;\"'<,>.?/\\|`~]",password):
        score += 1
    else:
        feedback.append("❗ Password should contain at least one special character")


    if score == 4:
        return "💪🏻 Strong password",feedback
    elif score == 3:
        return "⚠️ Moderate password - Consider adding more security features.",feedback
    else:
        return "❌ Weak password - Improve it using the suggestions above.",feedback
    




# define a function to generate strong password

def generate_password(length):

    all_possible_chars = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.sample(all_possible_chars,length))
    return password

    



page_bg = """
<style>
[data-testid = "stAppViewContainer"]{
background-color : #80775C;
color:black
}

[data-testid = "stMainBlockContainer"]{
background-color : #FAE8B4;
margin-top: 100px;
margin-bottom: 50px;
border-radius:40px;
padding:50px
}
</style>

"""    

st.set_page_config(page_title="HackProof", page_icon="🔒")

st.markdown(page_bg,unsafe_allow_html=True)

st.title("🔒HackProof - Password Strength Checker")

st.write("Enter your password below to check its strength")



user_password = st.text_input("Password", type="password")



if user_password:  # Ensure feedback appears only when a password is entered
    result, suggestions = password_strength(user_password)
    if result == "❌ Weak password - Improve it using the suggestions above.":
        st.error(f"### {result}")  
    elif result == "⚠️ Moderate password - Consider adding more security features.":
        st.warning(f"### {result}")
    else:
        st.success(f"### {result}")    


    # chech if there are any suggestions or not


    if suggestions:
        st.markdown("#### Suggestions to improve:")
        for suggestion in suggestions:
            st.write(suggestion)  # Display each suggestion separately




# new section for password generator
st.write("---")
st.title("🔑 Generate Strong Password")

len = st.number_input("Length",
    min_value=8,  # Minimum value of 8
    step=1,       # Increase by 1
    value=12      # Default value 
    )
if st.button("Generate"):
    st.markdown("Here is generated password")
    st.success(generate_password(len))