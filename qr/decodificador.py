import base64

def decode(data):
    '''
    Funcion que decodifica un mensaje recursivamente en base64
    '''
    try: # Decodificamos el mensaje en base64 varias veces
        decoded_data = base64.b64decode(data)
        return decode(decoded_data)
    
    except Exception as e: # Si ya no se puede decodificar más (por error o porque no hay más datos), devolvemos el mensaje decodificado
        return data