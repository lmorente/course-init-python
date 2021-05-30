"""
    Python and MySQL Project:
    - Open assistant
    - Login or register
    - Create note, show note, delete note.
"""
from project.app.user_system import actions

app = actions.sys_action()
app.start()

user_action = input("¿Que quieres hacer?: ")

if user_action.upper() == "REGISTRO":
    app.register()
elif user_action.upper() == "LOGIN":
    app.login()
