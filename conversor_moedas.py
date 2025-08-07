import requests as rqst

class Conversao():
    valor = float

    def _obter_media_valores(self, url, chave):
        response = rqst.get(url)
        if response.status_code == 200:
            dados = response.json()
            high = float(dados[chave]['high'])
            low = float(dados[chave]['low'])
            return (high + low) / 2
        else:
            raise Exception(f"Erro na resposta: {response.status_code}")

    def _converter(self, url, chave, para_real=True, simbolo_origem='', simbolo_destino=''):
        try:
            media = self._obter_media_valores(url, chave)
            if para_real:
                resultado = self.valor * media
                return f'O valor de {simbolo_origem}{self.valor} é um total de {simbolo_destino}{resultado:.2f}'
            else:
                resultado = self.valor / media
                return f'O valor de {simbolo_origem}{self.valor} é um total de {simbolo_destino}{resultado:.2f}'
        except Exception as e:
            return f'\033[31mO erro é {e}\033[0m'

    # ======================
    # CATEGORIA: REAL (BRL)
    # ======================
    def cnv_dolar_real(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/USD-BRL", "USDBRL", True, "U$", "R$")
    
    def cnv_real_dolar(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/USD-BRL", "USDBRL", False, "R$", "U$")
    
    def cnv_eu_real(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/EUR-BRL", "EURBRL", True, "€", "R$")
    
    def cnv_real_eu(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/EUR-BRL", "EURBRL", False, "R$", "€")
    
    def cnv_libra_real(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/GBP-BRL", "GBPBRL", True, "£", "R$")
    
    def cnv_real_libra(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/GBP-BRL", "GBPBRL", False, "R$", "£")
    
    def cnv_peso_real(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/ARS-BRL", "ARSBRL", True, "$ (ARS)", "R$")
    
    def cnv_real_peso(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/ARS-BRL", "ARSBRL", False, "R$", "$ (ARS)")
    
    def cnv_china_real(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/CNY-BRL", "CNYBRL", True, "¥", "R$")
    
    def cnv_real_china(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/CNY-BRL", "CNYBRL", False, "R$", "¥")
    
    def cnv_btc_real(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/BTC-BRL", "BTCBRL", True, "₿", "R$")
    
    def cnv_eth_real(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/ETH-BRL", "ETHBRL", True, "Ξ", "R$")
    
    def cnv_xrp_real(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/XRP-BRL", "XRPBRL", True, "✕", "R$")

    # =======================
    # CATEGORIA: DÓLAR (USD)
    # =======================
    def cnv_libra_dolar(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/GBP-USD", "GBPUSD", True, "£", "U$")
    
    def cnv_dolar_libra(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/GBP-USD", "GBPUSD", False, "U$", "£")
    
    def cnv_peso_dolar(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/ARS-USD", "ARSUSD", True, "$ (ARS)", "U$")
    
    def cnv_dolar_peso(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/ARS-USD", "ARSUSD", False, "U$", "$ (ARS)")
    
    def cnv_china_dolar(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/CNY-USD", "CNYUSD", True, "¥", "U$")
    
    def cnv_dolar_china(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/CNY-USD", "CNYUSD", False, "U$", "¥")
    
    def cnv_btc_dolar(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/BTC-USD", "BTCUSD", True, "₿", "U$")
    
    def cnv_dolar_btc(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/BTC-USD", "BTCUSD", False, "U$", "₿")
    
    def cnv_eth_dolar(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/ETH-USD", "ETHUSD", True, "Ξ", "U$")
    
    def cnv_dolar_eth(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/ETH-USD", "ETHUSD", False, "U$", "Ξ")
    
    def cnv_xrp_dolar(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/XRP-USD", "XRPUSD", True, "✕", "U$")
    
    def cnv_dolar_xrp(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/XRP-USD", "XRPUSD", False, "U$", "✕")

    # =====================
    # CATEGORIA: EURO (EUR)
    # =====================
    def cnv_libra_euro(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/GBP-EUR", "GBPEUR", True, "£", "€")
    
    def cnv_euro_libra(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/GBP-EUR", "GBPEUR", False, "€", "£")
    
    def cnv_peso_euro(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/ARS-EUR", "ARSEUR", True, "$ (ARS)", "€")
    
    def cnv_euro_peso(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/ARS-EUR", "ARSEUR", False, "€", "$ (ARS)")
    
    def cnv_china_euro(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/CNY-EUR", "CNYEUR", True, "¥", "€")
    
    def cnv_euro_china(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/CNY-EUR", "CNYEUR", False, "€", "¥")
    
    def cnv_btc_euro(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/BTC-EUR", "BTCEUR", True, "₿", "€")
    
    def cnv_euro_btc(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/BTC-EUR", "BTCEUR", False, "€", "₿")
    
    def cnv_eth_euro(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/ETH-EUR", "ETHEUR", True, "Ξ", "€")
    
    def cnv_euro_eth(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/ETH-EUR", "ETHEUR", False, "€", "Ξ")
    
    def cnv_xrp_euro(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/XRP-EUR", "XRPEUR", True, "✕", "€")
    
    def cnv_euro_xrp(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/XRP-EUR", "XRPEUR", False, "€", "✕")

    # ========================
    # CATEGORIA: LIBRA (GBP)
    # ========================
    def cnv_china_libra(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/CNY-GBP", "CNYGBP", True, "¥", "£")
    
    def cnv_libra_china(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/CNY-GBP", "CNYGBP", False, "£", "¥")
    
    def cnv_peso_libra(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/ARS-GBP", "ARSGBP", True, "$ (ARS)", "£")
    
    def cnv_libra_peso(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/ARS-GBP", "ARSGBP", False, "£", "$ (ARS)")
    
    def cnv_btc_libra(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/BTC-GBP", "BTCGBP", True, "₿", "£")
    
    def cnv_libra_btc(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/BTC-GBP", "BTCGBP", False, "£", "₿")
    
    def cnv_eth_libra(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/ETH-GBP", "ETHGBP", True, "Ξ", "£")
    
    def cnv_libra_eth(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/ETH-GBP", "ETHGBP", False, "£", "Ξ")
    
    def cnv_xrp_libra(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/XRP-GBP", "XRPGBP", True, "✕", "£")
    
    def cnv_libra_xrp(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/XRP-GBP", "XRPGBP", False, "£", "✕")

    # ========================
    # CATEGORIA: BITCOIN (BTC)
    # ========================
    def cnv_peso_btc(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/ARS-BTC", "ARSBTC", True, "$ (ARS)", "₿")
    
    def cnv_btc_peso(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/ARS-BTC", "ARSBTC", False, "₿", "$ (ARS)")
    
    def cnv_china_btc(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/CNY-BTC", "CNYBTC", True, "¥", "₿")
    
    def cnv_btc_china(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/CNY-BTC", "CNYBTC", False, "₿", "¥")
    
    def cnv_eth_btc(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/ETH-BTC", "ETHBTC", True, "Ξ", "₿")
    
    def cnv_btc_eth(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/ETH-BTC", "ETHBTC", False, "₿", "Ξ")
    
    def cnv_xrp_btc(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/XRP-BTC", "XRPBTC", True, "✕", "₿")
    
    def cnv_btc_xrp(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/XRP-BTC", "XRPBTC", False, "₿", "✕")

    # ========================
    # CATEGORIA: YUAN (CNY)
    # ========================
    def cnv_peso_china(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/ARS-CNY", "ARSCNY", True, "$ (ARS)", "¥")
    
    def cnv_china_peso(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/ARS-CNY", "ARSCNY", False, "¥", "$ (ARS)")
    
    def cnv_eth_china(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/ETH-CNY", "ETHCNY", True, "Ξ", "¥")
    
    def cnv_china_eth(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/ETH-CNY", "ETHCNY", False, "¥", "Ξ")
    
    def cnv_xrp_china(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/XRP-CNY", "XRPCNY", True, "✕", "¥")
    
    def cnv_china_xrp(self): return self._converter(
        "https://economia.awesomeapi.com.br/last/XRP-CNY", "XRPCNY", False, "¥", "✕")