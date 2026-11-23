print("Bienvenido a esto :b")
nombre = input("como te llamas?: ")
curso = input("de que curso eres?: ")

final = print(f"asi que te llamas {nombre} y eres de {curso}")

opciones = ("python", "javascrip", "java", "c++")
print("que lenguaje de programacion es tu favorito?")
print("opciones:", opciones)
lenguajes = input("escribe cual prefieres: ").lower()

if lenguajes == "python":
    print(f"eres normal {nombre}, sigue con tu vida feliz"
    )
elif lenguajes == "javascrip":
    print(f"okey eres bueno {nombre}, toma un helado :)"
    )
elif lenguajes == "java":
    print(f"me caes bien {nombre}, pero te voy a mirar raro"
    )
elif lenguajes == "c++":
    print(f"busca ayuda por favor")
else:
    print("no me suena y si no pusiste nada matate")