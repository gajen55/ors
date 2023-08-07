import streamlit as st
import pandas as pd
import openpyxl

# Sample list of names
NameList = ['Rohan', 'Roshan', 'Ankit', 'Anusha']

# Function to filter names based on input string
def filter_names(input_string):
    return [name for name in NameList if input_string.lower() in name.lower()]

# Function to save responses to Excel
def save_to_excel(name):
    data = {'Selected Name': [name]}
    df = pd.DataFrame(data)
    with pd.ExcelWriter('responses.xlsx', mode='a') as writer:
        df.to_excel(writer, index=False, header=not writer.sheets)

# Streamlit app
def main():
    st.title('Name Search Web App')

    input_string = st.text_input('Enter a string:')
    find_button = st.button('Find')

    if find_button:
        filtered_names = filter_names(input_string)
        selected_name = st.selectbox('Select a name:', filtered_names)

        if selected_name:
            save_to_excel(selected_name)
            st.success(f'You have selected: {selected_name}')
    
if __name__ == '__main__':
    main()
