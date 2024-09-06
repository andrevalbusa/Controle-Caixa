import pandas as pd
from PyQt5 import QtWidgets, uic
from datetime import datetime, timedelta
import main
from layout_CC import Ui_MainWindow

df_banco = pd.read_csv('bancos.csv')


def extrair_codigo():
    ui = Ui_MainWindow()
    codigo = ui.cod_boleta.text()
    cod_inst = codigo[0:3]
    ################ DATA DE VENCIMENTO ################
    cod_vencimento = int(codigo[31:35])
    data_base = '07/10/1997'
    formato_data = "%d/%m/%Y"
    data_base_obj = datetime.strptime(data_base, formato_data)
    data_calculada = data_base_obj + timedelta(days=cod_vencimento)
    data_vencimento = data_calculada.strftime(formato_data)

    #################### VALOR BOLETO ##################
    cod_reais = codigo[35:43]
    cod_centavos = codigo[43:45]
    valor_boleto = (cod_reais + ',' + cod_centavos)

    ##################### FORNECEDOR ###################
    


    
    return 
