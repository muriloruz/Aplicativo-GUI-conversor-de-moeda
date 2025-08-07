import conversor_moedas as cnv
import tkinter as tk
from tkinter import ttk
import re

class ConversorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Moedas e Criptomoedas")
        self.root.geometry("500x400")
        
        # Instância da classe de conversão
        self.conversor = cnv.Conversao()
        
        # Variáveis de controle
        self.valor = tk.DoubleVar(value=1.0)
        self.moeda_origem = tk.StringVar()
        self.moeda_destino = tk.StringVar()
        self.resultado = tk.StringVar(value="Resultado aparecerá aqui")
        
        # Mapeamento de códigos para nomes de métodos
        self.mapeamento_metodos = {
            "BRL": "real",
            "USD": "dolar",
            "EUR": "eu",
            "GBP": "libra",
            "ARS": "peso",
            "CNY": "china",
            "BTC": "btc",
            "ETH": "eth",
            "XRP": "xrp"
        }
        
        # Configurar estilo
        self.setup_style()
        
        # Criar widgets
        self.create_widgets()
    
    def setup_style(self):
        style = ttk.Style()
        style.configure('TFrame', background='#f0f0f0')
        style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        style.configure('TButton', font=('Arial', 10), padding=5)
        style.configure('TCombobox', padding=5)
        style.configure('TEntry', padding=5)
        
    def create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        titulo = ttk.Label(main_frame, text="Conversor de Moedas", font=('Arial', 16, 'bold'))
        titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Campo de valor
        ttk.Label(main_frame, text="Valor:").grid(row=1, column=0, sticky=tk.W, pady=5)
        valor_entry = ttk.Entry(main_frame, textvariable=self.valor, width=20)
        valor_entry.grid(row=1, column=1, sticky=tk.EW, pady=5)
        
        # Moeda de origem
        ttk.Label(main_frame, text="De:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.origem_cb = ttk.Combobox(main_frame, textvariable=self.moeda_origem, width=18)
        self.origem_cb.grid(row=2, column=1, sticky=tk.EW, pady=5)
        
        # Moeda de destino
        ttk.Label(main_frame, text="Para:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.destino_cb = ttk.Combobox(main_frame, textvariable=self.moeda_destino, width=18)
        self.destino_cb.grid(row=3, column=1, sticky=tk.EW, pady=5)
        
        # Configurar as opções das combobox
        self.moedas = [
            ("Real Brasileiro", "BRL", "R$"),
            ("Dólar Americano", "USD", "U$"),
            ("Euro", "EUR", "€"),
            ("Libra Esterlina", "GBP", "£"),
            ("Peso Argentino", "ARS", "$"),
            ("Yuan Chinês", "CNY", "¥"),
            ("Bitcoin", "BTC", "₿"),
            ("Ethereum", "ETH", "Ξ"),
            ("XRP", "XRP", "✕")
        ]
        
        # Lista formatada para exibição
        moedas_display = [f"{nome} ({simbolo})" for nome, codigo, simbolo in self.moedas]
        self.origem_cb['values'] = moedas_display
        self.destino_cb['values'] = moedas_display
        
        # Selecionar padrões
        self.origem_cb.current(1)  # Dólar
        self.destino_cb.current(0)  # Real
        
        # Botão de conversão
        converter_btn = ttk.Button(main_frame, text="Converter", command=self.converter)
        converter_btn.grid(row=4, column=0, columnspan=2, pady=20)
        
        # Resultado
        resultado_frame = ttk.Frame(main_frame, borderwidth=1, relief=tk.SOLID)
        resultado_frame.grid(row=5, column=0, columnspan=2, sticky=tk.EW, pady=10)
        
        ttk.Label(resultado_frame, textvariable=self.resultado, 
                 font=('Arial', 12), wraplength=400, justify=tk.CENTER,
                 padding=10).pack(fill=tk.BOTH, expand=True)
        
        # Configurar expansão
        main_frame.columnconfigure(1, weight=1)
    
    def extrair_valor(self, texto):
        """Extrai o valor numérico do texto de resultado"""
        try:
            # Procura o último número no texto
            numeros = re.findall(r"[\d,]+\.\d{2}", texto)
            if numeros:
                # Pega o último número encontrado
                valor_str = numeros[-1].replace(',', '')
                return float(valor_str)
            return None
        except:
            return None
        
    def converter(self):
        try:
            # Obter os valores selecionados
            valor = self.valor.get()
            origem_idx = self.origem_cb.current()
            destino_idx = self.destino_cb.current()
            
            if origem_idx == -1 or destino_idx == -1:
                self.resultado.set("Selecione as moedas de origem e destino")
                return
            
            # Obter códigos das moedas
            origem_codigo = self.moedas[origem_idx][1]
            destino_codigo = self.moedas[destino_idx][1]
            
            # Verificar se é a mesma moeda
            if origem_codigo == destino_codigo:
                self.resultado.set(f"O valor é o mesmo: {valor}")
                return
            
            # Atualizar valor no conversor
            self.conversor.valor = valor
            
            # Obter nomes dos métodos
            origem_metodo = self.mapeamento_metodos.get(origem_codigo)
            destino_metodo = self.mapeamento_metodos.get(destino_codigo)
            
            if not origem_metodo or not destino_metodo:
                self.resultado.set("Moeda não suportada")
                return
            
            # Determinar qual método de conversão chamar
            metodo_direto = f"cnv_{origem_metodo}_{destino_metodo}"
            metodo_inverso = f"cnv_{destino_metodo}_{origem_metodo}"
            
            if hasattr(self.conversor, metodo_direto):
                resultado = getattr(self.conversor, metodo_direto)()
                self.resultado.set(resultado)
            elif hasattr(self.conversor, metodo_inverso):
                # Se existir o método inverso, faz a conversão inversa
                self.conversor.valor = valor
                resultado_inverso = getattr(self.conversor, metodo_inverso)()
                valor_convertido = self.extrair_valor(resultado_inverso)
                
                if valor_convertido is not None:
                    resultado = f"O valor de {origem_codigo}{valor} é um total de {destino_codigo}{valor_convertido:.2f}"
                    self.resultado.set(resultado)
                else:
                    self.resultado.set("Erro ao converter valor")
            else:
                # Tentar conversão via Dólar
                if origem_codigo != "USD" and destino_codigo != "USD":
                    # Converter origem -> USD
                    metodo_origem_usd = f"cnv_{origem_metodo}_dolar"
                    metodo_usd_destino = f"cnv_dolar_{destino_metodo}"
                    
                    if hasattr(self.conversor, metodo_origem_usd) and hasattr(self.conversor, metodo_usd_destino):
                        # Primeira conversão: origem -> USD
                        self.conversor.valor = valor
                        resultado_parcial = getattr(self.conversor, metodo_origem_usd)()
                        valor_usd = self.extrair_valor(resultado_parcial)
                        
                        if valor_usd is None:
                            self.resultado.set("Erro na conversão intermediária")
                            return
                        
                        # Segunda conversão: USD -> destino
                        self.conversor.valor = valor_usd
                        resultado_final = getattr(self.conversor, metodo_usd_destino)()
                        self.resultado.set(f"{origem_codigo} → USD → {destino_codigo}\n{resultado_final}")
                    else:
                        self.resultado.set("Conversão não disponível")
                else:
                    self.resultado.set("Conversão não disponível")
                    
        except Exception as e:
            self.resultado.set(f"Erro na conversão: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConversorApp(root)
    root.mainloop()