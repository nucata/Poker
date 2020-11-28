class ReadHistory(object):
    def __init__(self):
        self.bbsW = self.bbsW()
        self.bbsL = self.bbsL()
        self.total_hands = self.totalHands()
    def bbsW(self):
        bbs_win = 0
        bbsW_record = []
        with open('History/win_register.txt', 'r') as file:
            seq = file.read().split()
            for i in seq:
                bbs_win += float(i)
            for i in seq:
                bbsW_record.append(float(i))
        return [bbs_win, bbsW_record]

    def bbsL(self):
        bbs_lose = 0
        bbsL_record = []
        with open('History/lose_register.txt', 'r') as file:
            seq = file.read().split()
            for i in seq:
                bbs_lose += float(i)
            for i in seq:
                bbsL_record.append(float(i))
        return [bbs_lose, bbsL_record]

    def totalHands(self):
        played_hands = 0
        with open('History/total_played_register.txt', 'r') as file:
            seq = file.read()
            for i in seq:
                    played_hands += 1
        return played_hands

    def read(self):
        return [self.bbsW, self.bbsL, self.total_hands]

    def hands_per_day_register(self):
        record = []
        with open('History/hands_per_day.txt', 'r') as file:
            seq = file.read().split()
            for i in seq:
                record.append(float(i))
        return record