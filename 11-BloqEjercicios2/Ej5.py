"""
Crear una lista con el contenido de la siguiente
tabla: Tabla de videojuegos
ACCION          AVENTURA            DEPORTES
GTA             UNCHARTED           FIFA
COD             CRASH               PRO
PUBG            WOW                 GT21
KILLZONE        LOR                 MOTO GP

Mostrar la informacion ordenada
"""

tabla = [
    {
        "categoria": "ACCION",
        "juegos": ["GTA", "Call of Duty", "PUBG", "KILL ZONE"]
    },
    {
        "categoria": "AVENTURA",
        "juegos": ["UNCHARTED", "CRASH", "WOW", "LORD OF THE RINGS"]
    },
    {
        "categoria": "DEPORTES",
        "juegos": ["FIFA 21", "PRO EVOLUTION SOCCER", "GRAN TURISMO", "MOTO GP"]
    }
]

print("-     TABLA DE VIDEOJUEGOS     -")
for categoria in tabla:
    print(f"------ {categoria['categoria']} ------")
    for juegos in categoria['juegos']:
        print(f"++{juegos}")


