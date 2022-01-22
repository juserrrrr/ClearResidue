import os
import shutil
def LimparResiduo(pasta):
    arquivos = os.listdir(pasta)
    for nome in arquivos:
        try:
            if os.path.isdir(pasta+nome):
                shutil.rmtree(pasta+nome)
                print(f'Removido {nome} com sucesso!')
            else:
                os.remove(pasta+nome)
                print(f'Removido {nome} com sucesso!')
        except:
            print(f'Falha ao remover {nome}!')

usuario = os.getlogin()
caminhos = [f'C:/Users/{usuario}/AppData/Local/Temp/']
for endereco in caminhos:
    LimparResiduo(endereco)
