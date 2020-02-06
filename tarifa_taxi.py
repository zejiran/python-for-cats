def calcular_tarifa_taxi (kms_recorridos:float)->int:
    cien_metros = (kms_recorridos*1000)/100
    tarifa = 4000 + (82*(cien_metros))
    return int(round(tarifa))