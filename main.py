meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "LARP":"Creerse un presonaje o persona famosa",
            "67":"balbuseos sin sentido",
            "PROYECTARSE":"decir algo profundo y personal",
            "PEAK": "es lo mejor que se haya visto",
            "AURA FARMING": "personal con estilo deslumbrante o actitud",
            "LOLCOW": "persona con poco cerebro o boba",
            "RAGEBAIT": "caer en el enojo"
            }
print ("Hola bienvenido a palabras confusas actuales")
for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("creo que la escribiste mal o en minusculas prueba de nuevo")
