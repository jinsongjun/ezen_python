class User:
    # 클래스 변수 생성
    # 같은 클래스를 생성하는 경우 공유할 수 있는 변수
    user_list = []
    def __init__(self, _name, _birth, _phone):
        self.name = _name
        self.birth = _birth
        self.phone = _phone
        self.user_list.append(_name)
    
    def info(self):
        # return 'name : '+self.name+'birth : '+self.birth+'phone : '+self.phone
        return f'name : {self.name} birth : {self.birth} phone : {self.phone}'


class Wallet(User):
    # 클래스 변수 생성 (일의 타입, 물품명 딕셔너리)
    work_type = {
        '사무직' : 100000, 
        '현장직' : 110000, 
        '관리직' : 150000
    }
    unit_cost = {
        '가방' : 5000000, 
        '맥북' : 2000000
    }

    # 생성자 함수 
    def __init__(
            self, 
            _name, 
            _birth, 
            _phone, 
            _balance = 0
            ):
        # 부모 클래스에 있는 생성자 함수를 호출
        # super() : 부모 클래스
        super().__init__(_name, _birth, _phone)
        self.balance = _balance

    # work() 함수를 생성 : 매개변수 self, _type
    def work(self, _type):
        if _type in self.work_type.keys():
            self.balance += self.work_type[_type]
        else:
            return '일의 타입이 존재하지 않습니다.'
        return f'{_type}의 일을 완료하였습니다. 현재 지갑의 잔액은 {self.balance}입니다.'
    # 오버라이드 : 기존의 info() 함수가 하는 행동을 Wallet에서는 다른 행동으로 변경
    def info(self):
        return f'지갑의 소유자는 {self.name}이고 잔액은 {self.balance}입니다'
    
    def flex(self, _type):
        if _type in self.unit_cost.keys():
            price = self.unit_cost[_type]
        else:
            return '해당 물품의 정보가 존재하지 않습니다'

        if self.balance >= price:
            self.balance -= price
            result = f'{_type} 구매가 완료되었습니다.'
        else:
            result = '지갑의 잔액이 부족합니다. 일을 좀 더 하세요'
        
        return result