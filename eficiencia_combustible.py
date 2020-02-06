def convertir_eficiencia_combustible (millas_por_galon:float)->float:
    conversion = 236.25 / millas_por_galon
    return round(conversion, 2)
