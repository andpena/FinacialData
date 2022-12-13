import socket
import win32api
import TypeDataTryd as tdt

#---ESCOLHER O ATIVO EXEMPLO:-----------#
# PETR4  - Petrobras
# VALE3  - Vale
# ITUB4  - Itau
# INDV19 - Indice Bovespa
# WINV19 - Mini Indice Bovespa
#========================================#
#ATIVO = ['PETR4','VALE3','ITUB4','BBAS3','CIEL3']
ATIVO = ['WINV19']
#========================================#

#---INFORMACOES DO SERVIDOR--------------#
#========================================#
HOST = '127.0.0.1'
PORT = 12002
#========================================#


def ByteConvert(dataInfo, ativo):
    return str.encode(dataInfo +'1|'+ ativo + '|0|1|#')

#Inicia a Execução
#oMkt = OutputMarketData()
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Id da thread principal %d" % (win32api.GetCurrentThreadId()))
        while True:
            arrInfo = []
            try:
                for item in ATIVO:
                    s.sendall(ByteConvert(tdt.LIVRO_DE_OFERTAS,item) )
                    data = s.recv(32768)
                    #Acumulando os ativos
                    arrInfo.append(data.decode().replace("LVL2!","").split(";"))
                    #oMkt.OutputData(arrInfo, ATIVO)
                print(arrInfo[0][3].replace("#",""), end=' ')
            except Exception as ex:
                print(ex)
            
except Exception as ex:
    print('Não foi possivel conectar no servidor RTD. Erro: ', ex)