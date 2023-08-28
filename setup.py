import os
import src.systems.database.users as users

filename = 'save_file.json'
if filename not in os.listdir():
    users.create_user('player')
