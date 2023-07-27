
import streamlit as st

def calculate_bmi(weight, height):
    if height == 0:
        return "Invalid height. Height cannot be zero!"
    bmi = weight / ((height / 100) ** 2)
    return round(bmi, 2)

def main():
    
    st.title("BMI Calculator")

    name = st.text_input("Name")

    gender = st.radio("Gender", ("Male", "Female", "Other"))

    age = st.number_input("Age", min_value=0, max_value=150, value=25)
                          
    address = st.text_area("Address")

    hobbies = st.checkbox("Hobbies")

    weight = st.number_input("Weight (kg)", min_value=0, value=60)
    
    height = st.number_input("Height (cm)", min_value=0, value=170)

    bmi = calculate_bmi(weight, height)

    st.write(f"Your BMI: {bmi}")

if __name__ == "__main__":
    main()
