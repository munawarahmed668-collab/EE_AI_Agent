class ChatMemory:

    def __init__(self):
        self.history = []

    def add(self, role, message):
        self.history.append({
            "role": role,
            "message": message
        })

    def get_context(self):

        text = ""

        for item in self.history[-10:]:

            text += f"{item['role']}: {item['message']}\n"

        return text

    def clear(self):
        self.history = []