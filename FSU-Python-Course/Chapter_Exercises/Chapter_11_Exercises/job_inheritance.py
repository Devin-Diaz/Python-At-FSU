class Employee:
    def __init__(self, name: str, emp_num: int) -> None:
        self.name = name
        self.emp_num = emp_num

    def get_name(self): return self.name
    def get_name(self): return self.emp_num
    def set_name(self, name): self.name = name
    def set_emp_id(self, emp_id): self.emp_id = emp_id

class ProductionWorker(Employee):
    def __init__(self, name: str, emp_num: int, shift_num: int, hourly_rate: float) -> None:
        super().__init__(name, emp_num)
        self.shift_num = shift_num
        self.hourly_rate = hourly_rate
    
    def get_shift_num(self): return self.shift_num
    def get_hourly_rate(self): return self.hourly_rate
    def set_shift_num(self, shift_num): self.shift_num = shift_num
    def set_hourly_rate(self, hourly_rate): self.hourly_rate = hourly_rate
    def to_string(self):
        return f'{self.name}\n{self.emp_num}\n{self.shift_num}\n{self.hourly_rate}'

def get_emp_info() -> ProductionWorker:
    name = input('Enter name: ')
    id = input('Enter Employee id: ')
    shift_num = input('Enter shift number (1 or 2): ')
    rate = input('Enter name pay rate: ')
    return ProductionWorker(name, id, shift_num, rate)

def main():
    print("Welcome to McDonald's. Please fill out your employment information")
    print('-' * 67)
    worker = get_emp_info()
    print('\nEmployee Data...')
    print(worker.to_string())

main()








