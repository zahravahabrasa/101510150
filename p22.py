class Triangle:
    def __init__(self, zele1, zele2, zele3):
        self._zele1 =zele1
        self._zele2 =zele2
        self._zele3 =zele3

    def is_valid(self):
        return self._zele1 > 0 and self._zele2 > 0 and self._zele3 > 0

    def fisaghores(self):
        zeleha = sorted([self._zele1, self._zele2, self._zele3])
        return zeleha[0]**2 + zeleha[1]**2 == zeleha[2]**2

    def type_mosalas(self):
        if self._zele1 == self._zele2 == self._zele3:
            return " motesavi azla "
        elif (self._zele1 == self._zele2 or self._zele1 == self._zele3 or self._zele2 == self._zele3) and not self.fisaghores():
            return "motesavi o saghein "
        elif self._zele1 != self._zele2 and self._zele1 != self._zele3 and self._zele2 != self._zele3 and not self.fisaghores():
            return " mohktalef azla "
        elif self.fisaghores():
            return " ghaem ol zavieh "
        else:
            return " invalid "

    def zele(self):
        return f" zelha : {self._zele1}, {self._zele2}, {self._zele3}"

mosalas=Triangle(zele1=3,zele2=3,zele3=3)

print(mosalas.zele())
print("azla invalid ? ", mosalas.is_valid())
print("ghaem ol zavieh ast ? ", mosalas.fisaghores())
print("type mosalas  : ", mosalas.type_mosalas())

