class Todo:
    def __init__(self, title, is_completed)-> None:
        self.title = title
        self.is_completed = False


    def set_completed(self):
        self.is_completed = True
