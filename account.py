import streamlit as st
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth
import json
import requests
import Medhak, account
from streamlit_option_menu import option_menu

# initizaliing firebase and credentials from the json file
cred = credentials.Certificate("Swan.json")
if not firebase_admin._apps:
    cred = credentials.Certificate("Swan.json")
    firebase_admin.initialize_app(cred)

#user login and signup functions
def login():

    st.title('Welcome to :violet[SWAN] :swan:')

    # if the username and email doesnt exist, initizalizes a session state
    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''

    # signs a user up with their email and password using firebase authentication
    def sign_up_with_email_and_password(email, password, username=None, return_secure_token=True):
        try:
            rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signUp"
            payload = {
                "email": email,
                "password": password,
                "returnSecureToken": return_secure_token
            }
            # adds username if provided
            if username:
                payload["displayName"] = username
            payload = json.dumps(payload)
            #sends a request to sign up the user to firebase
            r = requests.post(rest_api_url, params={"key": "AIzaSyApr-etDzcGcsVcmaw7R7rPxx3A09as7uw"}, data=payload)
            try:
                # if successful it returns the email that was sent
                return r.json()['email']
            except:
                #shows a signup failed message 
                st.warning(r.json())
        except Exception as e:
            st.warning(f'Signup failed: {e}')

    # function to sign the user in 
    def sign_in_with_email_and_password(email=None, password=None, return_secure_token=True):
        rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"
        try:
            payload = {
                "returnSecureToken": return_secure_token
            }
            if email:
                payload["email"] = email
            if password:
                payload["password"] = password
            payload = json.dumps(payload)
            print('payload sign in', payload)
            # sends a post request to firebase API
            r = requests.post(rest_api_url, params={"key": "AIzaSyApr-etDzcGcsVcmaw7R7rPxx3A09as7uw"}, data=payload)
            try:
                # gets the user data
                data = r.json()
                user_info = {
                    'email': data['email'],
                    'username': data.get('displayName')  # gets a username if available
                }
                return user_info
            except:
                # if failed, shows a warning
                st.warning(data)
        except Exception as e:
            st.warning(f'Signin failed: {e}')

    # function to reset the persons password
    def reset_password(email):
        try:
            rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode"
            payload = {
                "email": email,
                "requestType": "PASSWORD_RESET"
            }
            payload = json.dumps(payload)
            # sends a post request to firebase api
            r = requests.post(rest_api_url, params={"key": "AIzaSyApr-etDzcGcsVcmaw7R7rPxx3A09as7uw"}, data=payload)
            if r.status_code == 200:
                return True, "Reset email sent"
            else:
                error_message = r.json().get('error', {}).get('message')
                return False, error_message
        except Exception as e:
            return False, str(e)

    # login logic function
    def f():
        try:
            # user authentication
            userinfo = sign_in_with_email_and_password(st.session_state.email_input, st.session_state.password_input)
            st.session_state.username = userinfo['username']
            st.session_state.useremail = userinfo['email']

            # stores the username
            global Usernm
            Usernm = (userinfo['username'])

            #set session state to sign in
            st.session_state.signedout = True
            st.session_state.signout = True

        except:
            st.warning('Login Failed')

    #sign out stuff
    def t():
        st.session_state.signout = False
        st.session_state.signedout = False
        st.session_state.username = ''

    # password reset stuff
    def forget():
        email = st.text_input('Email')
        if st.button('Send Reset Link'):
            success, message = reset_password(email)
            if success:
                st.success("Password reset email sent successfully.")
            else:
                st.warning(f"Password reset failed: {message}")

    
    if "signedout" not in st.session_state:
        st.session_state["signedout"] = False
    if 'signout' not in st.session_state:
        st.session_state['signout'] = False

    # shows login and signup options
    if not st.session_state["signedout"]:
        choice = st.selectbox('Login/Signup', ['Login', 'Sign up'])
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')
        st.session_state.email_input = email
        st.session_state.password_input = password

        #account creation/login handler
        if choice == 'Sign up':
            username = st.text_input("Enter your unique username")
            if st.button('Create my account'):
                user = sign_up_with_email_and_password(email=email, password=password, username=username)
                st.success('Account created successfully!')
                st.markdown('Please login using your email and password')
                st.balloons()
        else:
            st.button('Login', on_click=f)
            forget()  # shlwos password reset option

    # if signed in, shows the sign out button
    if st.session_state.signout:
        Medhak.run()  # runs the main app
        if st.sidebar.button('Sign out', on_click=t, type="primary", use_container_width=True):
            st.write("Signed out")

# handling multiple apps
class MultiApp:

    def __init__(self):
        self.apps = []


    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })


account.login()
