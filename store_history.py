class StoreHistory(object):   
    def start():
        manos = 0
        while True:
            registro = input(': ').upper()
            if registro[0] == 'W':
                manos += 1
                with open('History/win_register.txt', 'a') as file:
                    file.write('{}\n'.format(registro[1:]))
                    
                with open('History/total_played_register.txt', 'a') as file:
                    file.write('M')

            elif registro[0] == 'L':
                manos += 1
                with open('History/lose_register.txt', 'a') as file:
                    file.write('{}\n'.format(registro[1:]))
                    
                with open('History/total_played_register.txt', 'a') as file:
                    file.write('M')
                    
            elif registro == 'M':
                manos += 1
                with open('History/total_played_register.txt', 'a') as file:
                    file.write('M')
            else:
                print(manos)
                with open('History/hands_per_day.txt', 'a') as file:
                    file.write('{}\n'.format(manos))
                break