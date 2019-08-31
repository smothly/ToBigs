from House import House

class Apartment(House):
    def __init__(self, dongho, size, room):
        super().__init__(size, room)
        self.dongho=dongho
        
    def __str__(self):
        return ('%s동 %s호의 %d개의 방이 있는 %d평의 아파트입니다.'\
                %(self.dongho.split('-')[0], self.dongho.split('-')[1], self.room, self.size))

    def __lt__(self, other):
        if self.size < other.size:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.size == other.size:
            return True
        else:
            return False
