import streamlit as st

# Initialize session state for login status
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def login(username, password):
    # In a real application, you would authenticate with a backend service
    if username == 'admin' and password == 'password':
        st.session_state['logged_in'] = True
    else:
        st.error("Invalid username or password")

def logout():
    st.session_state['logged_in'] = False

def main_menu():
    st.title("Logistics App - Main Menu")
    
    # Display different sections of the app
    if st.button("Inventory"):
        st.write("This is the Inventory page.")
    if st.button("Shipments"):
        st.write("This is the Shipments page.")
    if st.button("Orders"):
        st.write("This is the Orders page.")
    
    # Logout button
    if st.button("Logout"):
        logout()

def login_page():
    st.title("Logistics App - Login")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        login(username, password)

# Main logic
if st.session_state['logged_in']:
    main_menu()
    st.write("Logged in as Admin")
else:
    login_page()
