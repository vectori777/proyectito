from curses import def_shell_mode
from dataclasses import dataclass
from fcntl import DN_MODIFY


class elementostructurales():
    losa = 15
    viga = 20
    columna = 18
    muro = 14
    cimentación = 40
    encontruccion = False

    def construir(self):
        self.encontruccion = True

    def estado(self):
        if(self.encontruccion):
            return "la casa esta en contrucción"
        else:

            return "la casa no esta construida"    

micasa = elementostructurales()

print("el tamaño de la losa es de",micasa.losa, "cm")
print("el tamaño de la viga es de",micasa.viga, "cm")
micasa.construir()

print(micasa.estado())

