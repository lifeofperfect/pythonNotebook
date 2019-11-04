import datetime

list_id = 0

class Note:

    def __init__(self, memo, tags=''):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()

        global list_id
        list_id += 1
        self.id = list_id

    def match(self, filter):
        return filter in self.memo or filter in self.tags


class NoteBook:
    def __init__(self):
        self.notes = []

    def new_note(self, memo, tags=''):
        self.notes.append(Note(memo,tags))

    def _find_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

    def modify_memo(self, note_id, memo):
        '''for note in self.notes:
            if note.id == note_id:
                note.memo = memo
                break'''
        self._find_note(note_id).memo = memo

    def modify_tags(self, note_id, tags):
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break
    
    def search(self, filter):
        return [note for note in self.notes if note.match(filter)]

