from datetime import datetime, date

class Data_Utils:

    FORMATO_DATA = "%d/%m/%Y"

    @staticmethod
    def string_para_data(data):
        return datetime.strptime(data,Data_Utils.FORMATO_DATA).date()
    
    @staticmethod
    def data_para_string(data):
        return data.strftime(Data_Utils.FORMATO_DATA)
    
    @staticmethod
    def validar_data(data):
        try:
            datetime.strptime(data, Data_Utils.FORMATO_DATA)
            return True
        except ValueError:
            return False
        

    @staticmethod
    def calcular_idade(data):
        data_inicio = data
        if isinstance(data, str):
            data_inicio = Data_Utils.string_para_data(data)
        elif not isinstance(data, date):
            raise ValueError("A data está em um formato inválido.")
        hoje = date.today()
        idade = hoje.year - data_inicio.year
        if(hoje.month, hoje.day) < (data_inicio.month, data_inicio.day):
            idade -= 1
        return idade    
