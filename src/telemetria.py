import random
from datetime import datetime

def coletar():
    """Simula a coleta de dados de telemetria do satélite AgroSat."""
    
    dados = {
        "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        
        # Saúde do sensor multiespectral (NDVI) — de 0 a 100%
        "ndvi_saude": round(random.uniform(60, 100), 1),
        
        # Temperatura do payload óptico em graus Celsius
        "temperatura_payload": round(random.uniform(15, 75), 1),
        
        # Capacidade de armazenamento restante em %
        "armazenamento": round(random.uniform(10, 95), 1),
        
        # Qualidade do sinal de downlink em %
        "sinal_downlink": round(random.uniform(40, 100), 1),
        
        # Nível de energia das baterias em %
        "energia": round(random.uniform(10, 100), 1),
        
        # Estabilidade de atitude (orientação do satélite) em %
        "estabilidade_atitude": round(random.uniform(70, 100), 1),
    }
    
    return dados