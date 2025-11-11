class Circle:
    def __init__(self, shoa):
        self._shoa = shoa

    def str_shoa(self):
        return str(self._shoa)

    def mohit(self):
        return 2 * 3.14 * self._shoa

    def masahat(self):
        return 3.14 * self._shoa * self._shoa
mosalas = Circle(shoa=3)

print( " shoa :", mosalas.str_shoa())
print(" mohit :", mosalas.mohit())
print(" masahat :", mosalas.masahat())
