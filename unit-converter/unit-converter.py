import streamlit as st

# 1. User will enter the value
# 2. select from unit
# 3. select to unit
# 4. Converted value from a created function will be shown 

def convert_units(value, unit_from, unit_to):
    
    conversions={
        "meter_to_kilometer":0.001,
        "kilometer_to_meter":1000,
        "gram_to_kilogram":0.001,
        "kilogram_to_gram":1000
    }

    key=f"{unit_from}_to_{unit_to}"

    if key in conversions:
        return value * conversions[key]
    else:
        return "Conversion not supported"
    

st.title("Unit Coverter")
value = st.number_input("Enter the value",min_value=1.0,step=1.0)
unit_from = st.selectbox("Convert from", ["meter","kilometer","gram","kilogram"])
unit_to = st.selectbox("Convert to", ["meter","kilometer","gram","kilogram"])

if st.button("Convert"):
    result = convert_units(value,unit_from, unit_to)
    st.write(f"Converted value: {result}")

