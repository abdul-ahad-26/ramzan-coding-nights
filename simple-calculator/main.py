# Imports
import streamlit as st

def main():
    st.title("Simple Calculator")

    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input("Enter num1", step=1.0)

    with col2:
        num2 = st.number_input("Enter num2",step=1.0)

    operator = st.selectbox("Select the operator",["+","/","-","*"])

    if st.button("Calculate"):
        try:
            if operator == "+":
                result = num1 + num2
            
            elif operator == "-":
                result = num1 - num2
                
            elif operator == "*":
                result = num1 * num2
            else:
                if num2 == 0:
                    st.error("Error: Division by zero")
                    return 
                
                result= num1/ num2

            st.success(f"{num1} {operator} {num2} = {result}")
        except Exception as e:
            st.error(f"An error occured: {str(e)}")

if __name__ == "__main__":
    main()

        
    
