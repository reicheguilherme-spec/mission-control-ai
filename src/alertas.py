def avaliar(dados):
    """Avalia os dados de telemetria e retorna lista de alertas."""
    
    alertas = []
    acoes_automaticas = []

    # Verifica temperatura do payload
    if dados["temperatura_payload"] > 65:
        alertas.append("🔴 CRÍTICO: Temperatura do payload óptico muito alta ({:.1f}°C)!".format(dados["temperatura_payload"]))
        acoes_automaticas.append("⚡ AÇÃO AUTOMÁTICA: Modo de resfriamento ativado!")
    elif dados["temperatura_payload"] > 55:
        alertas.append("🟡 ATENÇÃO: Temperatura do payload elevada ({:.1f}°C).".format(dados["temperatura_payload"]))

    # Verifica nível de energia
    if dados["energia"] < 20:
        alertas.append("🔴 CRÍTICO: Nível de energia muito baixo ({:.1f}%)!".format(dados["energia"]))
        acoes_automaticas.append("⚡ AÇÃO AUTOMÁTICA: Modo de economia de energia ativado!")
    elif dados["energia"] < 35:
        alertas.append("🟡 ATENÇÃO: Nível de energia baixo ({:.1f}%).".format(dados["energia"]))

    # Verifica sinal de downlink
    if dados["sinal_downlink"] < 50:
        alertas.append("🔴 CRÍTICO: Sinal de downlink muito fraco ({:.1f}%)!".format(dados["sinal_downlink"]))
        acoes_automaticas.append("⚡ AÇÃO AUTOMÁTICA: Tentando reconexão com estação terrestre!")
    elif dados["sinal_downlink"] < 65:
        alertas.append("🟡 ATENÇÃO: Sinal de downlink fraco ({:.1f}%).".format(dados["sinal_downlink"]))

    # Verifica armazenamento
    if dados["armazenamento"] < 15:
        alertas.append("🔴 CRÍTICO: Armazenamento quase cheio! Apenas {:.1f}% livre.".format(dados["armazenamento"]))
        acoes_automaticas.append("⚡ AÇÃO AUTOMÁTICA: Compressão de dados iniciada!")
    elif dados["armazenamento"] < 25:
        alertas.append("🟡 ATENÇÃO: Armazenamento baixo ({:.1f}% livre).".format(dados["armazenamento"]))

    # Verifica saúde do sensor NDVI
    if dados["ndvi_saude"] < 70:
        alertas.append("🔴 CRÍTICO: Sensor NDVI com falha ({:.1f}% de saúde)!".format(dados["ndvi_saude"]))
        acoes_automaticas.append("⚡ AÇÃO AUTOMÁTICA: Diagnóstico do sensor NDVI iniciado!")
    elif dados["ndvi_saude"] < 80:
        alertas.append("🟡 ATENÇÃO: Sensor NDVI degradado ({:.1f}% de saúde).".format(dados["ndvi_saude"]))

    # Verifica estabilidade de atitude
    if dados["estabilidade_atitude"] < 80:
        alertas.append("🔴 CRÍTICO: Instabilidade de atitude detectada ({:.1f}%)!".format(dados["estabilidade_atitude"]))
        acoes_automaticas.append("⚡ AÇÃO AUTOMÁTICA: Sistema de controle de atitude reativado!")

    # Se tudo estiver bem
    if not alertas:
        alertas.append("✅ Todos os sistemas operando normalmente.")

    return alertas, acoes_automaticas