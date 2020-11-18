from store_history import StoreHistory
from read_history import ReadHistory

# Devuelve la cantidad de [[bbs ganados, historial de bbs gandos], [bbs pedidos, historial de bbs perdidos], total de manos]
data = ReadHistory().read()

# session es el registro del núemero de manos que juego en cada sesión
session = ReadHistory().hands_per_day_register()

# Manos medias que juego en cada sesión
session_mean = 0
for i in session:
    session_mean += i
session_mean /= len(session)


bbsW = data[0]
bbsL = data[1]
total_hands = data[2]

# Bbs cada 100 manos

bbsW_100 = int(bbsW[0]/total_hands * 100)
bbsL_100 = int(bbsL[0]/total_hands * 100)

# Las bbs que gano cada 100 manos restadas las bbs que pierdo cada 100 manos
# wr = win rate = ganancia neta(falta restar el rake) por cada 100 manos

wr = bbsW_100 - bbsL_100
bbs = 0.02

# Objetivo es cuanto dinero(en €) quiero ganar en un tiempo determinado. Servirá para conocer la cantiad de manos que debo jugar

objetivo = 300
objetivo_en_bbs = objetivo / bbs
cantidad_de_manos = 100 / wr * objetivo_en_bbs


print('bbsW/100: {} '.format(bbsW_100))
print('bbsL/100: {}'.format(bbsL_100))
print('WR: {}bbs/100manos'.format(wr))
print('{}€ = {} manos'.format(objetivo, int(cantidad_de_manos)))
print('{} manos por sesión'.format(session_mean))
