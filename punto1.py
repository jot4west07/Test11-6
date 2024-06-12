paises_g7 = ['Italia', 'Alemania', 'Canadá', 'Francia', 'Japón', 'Reino Unido', 'Estados Unidos']

def inversa(paises_g7):
    if len(paises_g7) == 0:
        return paises_g7
    else:
        return [paises_g7[-1]] + inversa(paises_g7[:-1])
print("Lista al revés:")
print(inversa(paises_g7))


