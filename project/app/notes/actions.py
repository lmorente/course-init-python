from project.app.notes.note import Note

class note_actions:

    def create(self, user):
        print(f"{user.get_name()} complete los siguientes campos: ")

        title = input("Titulo: ")
        description = input("Descripción: ")

        new_note = Note(user.get_id(), title, description)
        save = new_note.save()

        if(save[0] >= 1):
            print(f"{user.get_name()} has guardado la nota: {new_note.get_title()}")
        else:
            print(f"No se ha podido guardar la nota: {new_note.get_title()}")

    def show(self, user):
        print(f"{user.get_name()} te mostramos tus notas:")
        note = Note(user.get_id())
        notes_user = note.find()

        count = 0
        for element_note in notes_user:
            count += 1
            print(f"####Nota {count} ####################")
            print(f"Titulo: {element_note[2]}")
            print(f"Descripción: {element_note[3]}")
            print("_____________________________________________________\n")

    def delete(self, user):
        title = input("Introduce el titulo de la nota que quiere eliminar")
        note = Note(user.get_id(), title)
        delete = note.deleteByTitle()

        if delete[0] >= 1:
            print(f"Se ha eliminado la nota: {note.get_title()}")
        else:
            print(f"No se ha podido eliminar la nota seleccionada")