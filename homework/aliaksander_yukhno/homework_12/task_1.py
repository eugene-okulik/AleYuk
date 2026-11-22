class Flower:
    def __init__(self, flower_name, price, lifetime, color, stem_length):
        self.flower_name = flower_name
        self.price = price
        self.lifetime = lifetime
        self.color = color
        self.stem_length = stem_length

    def __str__(self):
        return (f"{self.flower_name}, цвет: {self.color}, цена: {self.price} BYN, "
                f"завянет через: {self.lifetime} дней, длина {self.stem_length} см")

    def __repr__(self):
        return f"{type(self).__name__}({self.flower_name!r})"


class Roses(Flower):

    def __init__(self, flower_name, price, lifetime, color, stem_length, is_thorn, bud_shape):
        super().__init__(flower_name, price, lifetime, color, stem_length)
        self.is_thorn = is_thorn
        self.bud_shape = bud_shape


class Carnations(Flower):

    def __init__(self, flower_name, price, lifetime, color, stem_length, shrub_type):
        super().__init__(flower_name, price, lifetime, color, stem_length)
        self.shrub_type = shrub_type


class Violet(Flower):

    def __init__(self, flower_name, price, lifetime, color, stem_length, flower_shape):
        super().__init__(flower_name, price, lifetime, color, stem_length)
        self.flower_shape = flower_shape


damask_rose = Roses("Роза Исфахан", 100, 20, "розовая",
                    50, True, "чашеобразная")
avalanche = Roses("Персиковая роза", 80, 9, "персиковая",
                  60, False, "конусообразная")
moonlight = Carnations("Корнес", 50, 2, "розово-белая",
                       2500, "кустовая")
liberty = Carnations("Гвоздика пышная", 110, 14, "белая",
                     1100, "кустовая")
garden_violet = Violet("Фиалка душистая", 15, 4, "розовая",
                       25, "чашеобразная")
saintpaulia = Violet("Фиалка трёхцветная", 20, 5, "фиолетовая",
                     15, "колоколообразный")


class Bouquet:
    def __init__(self):
        self.buket = []

    def add_flower(self, flowers):
        self.buket.append(flowers)

    def remove_flower(self, flowers):
        self.buket.remove(flowers)

    def trash_time(self):
        return sum(flowers.lifetime for flowers in self.buket) / len(self.buket)

    def sort_by_parameter(self, parameter, reverse=False):
        self.buket.sort(key=lambda flowers: getattr(flowers, parameter), reverse=reverse)

    def find_by(self, parameter, value):
        return [flowers for flowers in self.buket if getattr(flowers, parameter) == value]

    def __iter__(self):
        return iter(self.buket)


bouquet_of_flowers = Bouquet()
bouquet_of_flowers.add_flower(saintpaulia)
bouquet_of_flowers.add_flower(liberty)
bouquet_of_flowers.add_flower(moonlight)
bouquet_of_flowers.add_flower(damask_rose)
bouquet_of_flowers.add_flower(garden_violet)

print(f"Букет цветов: {bouquet_of_flowers.buket}")
print("Цветы в букете: ")
for flower in bouquet_of_flowers.buket:
    print(f"\tцветок: {flower.flower_name}, цвет: {flower.color}, цена: {flower.price} BYN, "
          f"завянет через: {flower.lifetime} дней, длина {flower.stem_length} см")

print(f"Завянут через: {bouquet_of_flowers.trash_time()} дней")
print("Сортировка по параметру:")
bouquet_of_flowers.sort_by_parameter("lifetime")
for flower in bouquet_of_flowers.buket:
    print(f"\tцветок: {flower.flower_name}, {flower.lifetime}")
print(f'Поиск по параметру: {bouquet_of_flowers.find_by("color", "розовая")}')
