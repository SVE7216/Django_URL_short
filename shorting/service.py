import uuid


class GenerateShortURL:
    '''Class for generate id'''

    @staticmethod
    def generate_id():
        short_id = str(uuid.uuid4())[:8]
        return short_id
