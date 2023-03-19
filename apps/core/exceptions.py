class CustomException(Exception):
    def __init__(self, error="Error al procesar la solicitud", code=400):
        self.error = error
        self.code = code
        super().__init__(self.error)