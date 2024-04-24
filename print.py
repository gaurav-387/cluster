# import streamlit as st
# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
# from dotenv import load_dotenv

# # Load environment variables from a .env file
# load_dotenv()

# # Get MongoDB connection string from environment
# uri = os.environ["mongo_connection"]

# # Connect to MongoDB server
# client = MongoClient(uri, server_api=ServerApi('1'))  # Use appropriate server API version

# try:
#     client.admin.command('ping')
#     print("Connected to MongoDB!")
# except Exception as e:
#     print(f"Error connecting to MongoDB: {e}")
#     st.error("Failed to connect to database. Please check your connection details.")
#     exit(1)  # Exit the application if connection fails

# # Get database and collection references
# db = client["new"]
# col = db["group"]


# def hash_password(password):
#     # Implement a secure password hashing algorithm (e.g., bcrypt)
#     # This example doesn't implement hashing for demonstration purposes
#     # Replace with your chosen hashing library and logic
#     return password


# def login():
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         # Implement logic to verify username and password against a secure storage
#         # (e.g., compare hashed password with stored hash)
#         # Replace with your authentication logic
#         if username == "admin" and password == "secret":  # Placeholder for real validation
#             st.success("Login successful!")
#             # Redirect to chat interface (replace with your chat logic)
#             st.write("**Chat interface not implemented yet.**")
#         else:
#             st.error("Invalid username or password.")


# def signup():
#     username = st.text_input("Username", key="uname")
#     email = st.text_input("Email ID")
#     mobile_number = st.number_input("Mobile Number")
#     password = st.text_input("Password", key="pass")
#     confirm_password = st.text_input("Confirm Password", key="cpass")

#     new_user = {
#         "biodata": {
#             "uid": username,
#             "eid": email,
#             "numeric_data": {
#                 "number": mobile_number,
#                 "confidential": {
#                     "pword": hash_password(password)  # Hash password before storing
#                 }
#             }
#         }
#     }

#     if st.button("Signup"):
#         if password == confirm_password:
#             try:
#                 col.insert_one(new_user)
#                 st.success("Account created successfully!")
#             except Exception as e:
#                 print(f"Error creating user: {e}")
#                 st.error("An error occurred while creating your account. Please try again.")
#         else:
#             st.error("Passwords do not match.")


# def main():
#     st.title('Welcome To:blue[Your Buddy]:wink:')
#     st.caption('Your:blue[stuff] = our :blue[stuff]:')

#     option = st.sidebar.selectbox("Menu", ["Login", "Signup"])

#     if option == "Login":
#         login()
#     elif option == "Signup":
#         signup()


# if __name__ == "__main__":
#     main()



# import streamlit as st
# from streamlit_option_menu import option_menu
# import json
# import uuid


# def load_json():
#     with open("data.json") as file:
#         data= json.load(file)
#     return data

# def save_json(data):
#     with open("data.json","w") as file:
#         json.dump(data,file,indent=4)

# def login():
#     flag=0
#     username = st.text_input("username",key="un")
#     password = st.text_input("password")
#     if st.button("login"):
#         adata=load_json()
#         for user in adata["users"]:
#             if username==user["uname"] and password==user["pword"]:
#                 st.write("welcome to nowhere")
#                 st.balloons()
#                 flag=0
#             else:
#                 flag=1
#         if flag==1:
#             st.write("incorrect username or password")       
            
# def signup():
#     username = st.text_input("username")
#     age_= st.number_input('age')
#     email=st.text_input('email id')
#     mnumber = st.number_input('mobile no')
#     password = st.text_input("password")
#     confirm_password= st.text_input("confirm password")

#     if st.button("signup"):
#         data = load_json()

#         if password==confirm_password:
            
#             newuser={
#             "biodata":{

#                 "uid":username,

#                 "eid":email,

#                 "numeric data":
#                 {
#                 "age":age_,

#                 "mno":mnumber,

#             "confenditial":{
                
#                "pword" :password
              
#                }
                
#                 }
            
#             }

#         }
#             data["users"].append(newuser)
#             save_json(data)
#             st.success("account created sucessfully !!")
#         else:
#             st.write("password does not match!!")

# def main():

#     st.title('welcome to :blue[Chatapp] :sunglasses:')
#     st.caption('finding new :blue[friends] = creating new :blue[memories] :wink:')

#     option= option_menu("menu",["login","signup"],orientation="vertical")
#     if option=="login":
#         login()
#     elif option=="signup":
#         signup()

# main()



