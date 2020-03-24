from modulos.persona import Persona


class Deportista(Persona):

    def deporte(self, deporte):
        return deporte

    def detener(self):
        return 'Está detenido'

    def correr(self):
        return 'Está corriendo'

    def saltar(self):
        return 'Está saltando'

    def __nadar(self):  # Este metodo solo se puede usar dentro de la clase
        return 'Está nadando'
