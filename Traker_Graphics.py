from read_history import ReadHistory

data = ReadHistory().read()
win_history = data[0][1]
lose_history = data[1][1]


print(lose_history)