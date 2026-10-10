class Jugador:
    # Stats del jugador
    def __init__(self, nombre, vida, energia, comida):
        self.nombre = nombre
        self.vida = vida
        self.energia = energia
        self.comida = comida
        self.vivo = True
        self.dias = 1
        self.durmiendo = False


    # Efectos de los eventos al jugador
    def aplicar_efecto(self, vida=0, energia=0, comida=0):
        self.vida += vida
        self.energia += energia
        self.comida += comida

        self.vida = max(0, min(100,self.vida))
        self.energia = max(0, min(100, self.energia))
        self.comida = max(0, min(100,self.comida))

        self.vivo = self.vida > 0 and self.comida > 0

        if self.energia == 0 and self.vivo:
            self.desmayarse()

    def desmayarse(self):
        self.dias += 1
        self.energia = 50
        self.comida -= 20
        self.comida = max(0, min(100, self.comida))
        self.durmiendo = True
        # Inanicion
        self.vivo = self.comida > 0 and self.vida > 0

    # Stats que va a ver el jugador
    def __str__(self):
        return (f"{self.nombre} | Dia: {self.dias} | Vida: {self.vida} | "
                f"Energía: {self.energia} | Comida: {self.comida} | "
                f"Vivo: {self.vivo}")