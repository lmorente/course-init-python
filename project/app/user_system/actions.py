from project.app.user_system import user
from project.app.notes import actions

class sys_action():

    def start(self):
        print("""
        Acciones disponibles:
            - registro
            - login
            """)

    def register(self):
        print("Procedemos al registro en el sistema ...")
        print("Indica los siguientes campos:")

        name = input("Nombre: ")
        surname = input("Apellidos: ")
        mail = input("Email: ")
        password = input("Contraseña: ")

        new_user = user.User('', name, surname, mail, password)
        user_register = new_user.register()

        if(user_register[0] >= 1):
            user_registry = user.User(user_register[0], user_register[1].get_name(), user_register[1].get_surname(),
                                      user_register[1].get_mail(), user_register[1].get_password())
            print(f"Perfecto {user_registry.get_name()} te has registrado correctamente con el email {user_registry.get_mail()}")
        else:
            print("El registro no se completo correctamente")


    def login(self):
        print("Identificate en el sistema")

        try:
            mail = input("Email: ")
            password = input("Contraseña: ")

            user_login = user.User('', '', '', mail, password)
            login = user_login.authenticate()

            if mail == login[3]:
                user_loged = user.User(login[0], login[1], login[2], login[3], login[4])
                print(f"Bienvenido {user_loged.get_name()}, te has registrado en el sistema el {login[5]}")
                self.next_actions(user_loged)

        except TypeError:
            print("Login incorrecto. Intenalo más tarde")

    def next_actions(self, user):
        print("""
        Acciones disponibles:
        - (Accion) -> (comando)
        - Crear nota -> crear
        - Mostrar notas -> ver
        - Eliminar nota -> eliminar
        - Salir -> salir
        """)

        action = input("Escoge una acción: ")
        note_action = actions.note_actions()

        if action.upper() == "CREAR":
            print("Creando ...")
            note_action.create(user)
            self.next_actions(user)

        elif action.upper() == "VER":
            print("Mostrando ...")
            note_action.show(user)
            self.next_actions(user)

        elif action.upper() == "ELIMINAR":
            print("Eliminando ...")
            note_action.delete(user)
            self.next_actions(user)

        elif action.upper() == "SALIR":
            print(f"¡Hasta pronto {user.get_name()}!")
            exit()

