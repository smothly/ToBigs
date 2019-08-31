from House import House

class Vile(House):
    
    def __init__(self, address, size, room, yard):
        super().__init__(size, room) # 부모의 생성자
        self.address=address
        self.yard=yard

    # print 문
    def __str__(self):
        if self.yard=='T':
            return ('%s에 위치해 있는 %d개의 방이 있고 마당이 있는 %d평의 주택입니다.'\
                    % (self.address, self.room, self.size))
        else:
            return ('%s에 위치해 있는 %d개의 방이 있고 마당이 없는 %d평의 주택입니다.'\
                    % (self.address, self.room, self.size))

    # 비교함수
    def __lt__(self, other):
        if self.size < other.size:
            return True
        else:
            return False

    
