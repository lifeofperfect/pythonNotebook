import sys 

from notebook import Note, NoteBook

class Menu:
    def __init__(self):
        self.notebook = NoteBook()
        self.choices = {
            '1': self.show_notes,
            '2': self.search_notes,
            '3': self.add_notes,
            '4': self.modify_note,
            '5': self.quit
        }

    def display_menu(self):
        print(
            """
            Notebook Menu
            1. to show all notes
            2. Search
            3. ADD NEW NOTES
            4. Modify
            5. QUIT
            """
        )

    def run(self):
        while True:
            self.display_menu()
            choice = input('hey pick an option: ')
            action = self.choices.get(choice)

            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
    
    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes

        for note in notes:
            print("{0}: {1}\n{2}".format(note.id, note.tags.note.memo))


    def search_notes(self):
        filter = input('sEARCH FOR: ')
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_notes(self):
        memo = input('Type in your memo: ')
        self.notebook.new_note(memo)
        print('Your note has been added')

    def modify_note(self):
        id = input('Enter id here: ')
        memo = input('Modify notes: ')
        tags = input('modify tags: ')

        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        print('Thank you for using my Notebook')
        sys.exit(0)
if __name__ == '__main__':
    Menu().run()
    
