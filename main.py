from kivy.app import App
import sqlite3
import os
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder

dbb = sqlite3.connect('class.db')
db = dbb.cursor()

class LoginPage(Screen):
    def verify_credentials(self):
    	# Query database for username
    	email = self.ids["email"].text
    	password = self.ids["passw"].text
    	rows = db.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        #rows = db.execute("SELECT * FROM users WHERE email = :email", {"email": self.ids["email"].text})
    	results = rows.fetchall()
    	print(len(results))
        # Ensure username exists and password is correct
    	if len(results) == 1:
    		self.manager.current = "user"
        #if self.ids["login"].text == "username" and self.ids["passw"].text == "password":
         #   self.manager.current = "user"

class UserPage(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

kv_file = Builder.load_file('login.kv')

class LoginApp(App):
    def builder(self):
        return kv_file

if __name__ == '__main__':
    LoginApp().run()

#https://gist.github.com/Cheaterman/812203a74f8c552a4918#file-connected-py-L3
#https://stackoverflow.com/questions/49225685/login-system-in-kivy