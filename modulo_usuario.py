import os

usuario_list=[]

def validar_sexo(sexo):
    if sexo in ["M", "F"]:
        return True
    else:
        print("error es valido F o M")
        return False

def validar_passwood(password):
    if len(password.strip())<8:
        print("error, falta de caracteres")
        return False
    
    tiene_numero= False
    for letra in password:
        if letra.isnumeric():
            tiene_numero = True
            
    tiene_letra= False
    for letra in password:
        if letra.isalpha():
            tiene_numero = True
            
    if " " in password:
        print("error, no puede tener espacios vacios")
        return False
    return tiene_letra and tiene_numero

def imprimir_usuario(usuario):
    print(f"""
        ------------------------------
        Nombre usuario: {usuario["nombre_usuario"]}
        Sexo: {usuario["sexo"]}
        password: {usuario["password"]}
        
        """)