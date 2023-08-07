import streamlit as st
import pandas as pd
# List of names
NameList = ['Rohan', 'Roshan', 'Ankit', 'Anusha']

def filter_names(search_string):
    return [name for name in NameList if search_string.lower() in name.lower()]

def main():
    st.title('Name Search Web App')
    
    # Text input
    search_input = st.text_input("Enter a string to search for names:")
    
    # Find button
    if st.button('Find'):
        filtered_names = filter_names(search_input)
        
        # Dropdown box
        if len(filtered_names) > 0:
            selected_name = st.selectbox('Select a name:', filtered_names)
            st.write(f'You selected: {selected_name}')
        else:
            st.write('No matching names found.')
            
        if st.button("Submit"):
            st.success(f"Selected Name: {selected_name}")
            df = pd.DataFrame({'Selected Name': [selected_name]})
            st.write('Response recorded!')
            
            # Append the DataFrame to an Excel file
            #with pd.ExcelWriter('responses.xlsx', mode='a', engine='openpyxl') as writer:
                #df.to_excel(writer, sheet_name='Responses', index=False, header=not writer.sheets['Responses'])
     
if __name__ == "__main__":
    main()
