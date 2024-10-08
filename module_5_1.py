class House:  # Создаем класс House
    def __init__(self, name, number_of_floors):  # используем метод init
        self.name = name  # присваиваем значение атрибутам
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor): #Создаем метод go_to с параметром new_floor
        self.new_floor = new_floor
        number_of_floors = int(self.number_of_floors)

        if int(new_floor) > number_of_floors or int(new_floor) < 1:  # сравнение new_floor и чем self.number_of_floors
            print('Такого этажа не существует')
        else:
            floor = 0
            for floor in range(0, new_floor):  # перебираем количество этажей
                floor = floor + 1
                print(floor)
            return floor

        def main():
            
            h1 = House('ЖК Горский', 18)
            h2 = House('Домик в деревне', 2)

            h1.go_to(5)
            h2.go_to(10)

            print('Такого этажа не существует!')

        if __name__ == '__main__':
            main()
