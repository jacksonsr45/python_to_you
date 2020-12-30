class Error():
    def __init__(self, message, status):
        self.message = message
        self.status = status


    def get_message(self):
        return {
            "message": self.message,
            "status": self.status
        }
    