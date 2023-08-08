import streamlit as st

# List of names in the backend
NameList = ['', 'Rohan', 'Roshan', 'Ankit', 'Anusha']
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

if 'selected_names' not in st.session_state:
    st.session_state.selected_names = []
    
def set_clicked():
    st.session_state.clicked = True
    
def main():
    st.title('Name Finder Web App')
    
    # Text input for user to enter a string
    user_input = st.text_input("Enter a string to find names:")
    
    # Button to trigger the name search
    st.button("Find", on_click=set_clicked)
    if user_input:
        if st.session_state.clicked:
            
            found_names = [name for name in NameList if user_input.lower() in name.lower()]
            if found_names:
                st.write("Names containing the entered string:")
                selected_names = st.selectbox("Select names:", found_names)
                    
                if selected_names:
                    if(st.button("Add")):
                        if selected_names not in st.session_state.selected_names:
                            st.session_state.selected_names.append(selected_names)
                    if(st.button("Remove")):
                        if selected_names in st.session_state.selected_names:
                            st.session_state.selected_names.remove(selected_names)

                    st.write("Selected names:")
                    
                    st.write("\n\n\n\n\n")
                    #st.write(st.session_state.selected_names)
            else:
                st.write("No names found with the entered string.")
    else:
        st.write("Please enter a string to find names.")
    final_names = list(set(st.session_state.selected_names))
    st.write(final_names)
    
if __name__ == "__main__":
    main()
