from store_history import StoreHistory
from read_history import ReadHistory
from display import Window

# Devuelve la cantidad de [[bbs ganados, historial de bbs gandos], [bbs pedidos, historial de bbs perdidos], total de manos]
data = ReadHistory().read()

# session es el registro del núemero de manos que juego en cada sesión
session = ReadHistory().hands_per_day_register()
hands = ReadHistory().totalHands()

bb = 0.02
bbW = data[0][0]
bbL = data[1][0]

wr = (bbW - bbL) / bb
wr_100 = (wr / hands) * 100

# Imprimir los datos en la pantalla

Window.wr_display(wr_100)