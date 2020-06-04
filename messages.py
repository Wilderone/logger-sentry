import random
import json


class Declar:
    def __init__(self, times=0):
        self.times = times
        self.first = [
            "Коллеги,",
            "В то же время,",
            "Однако,",
            "Тем не менее,",
            "Следовательно,",
            "Соответственно,",
            "Вместе с тем,",
            "С другой стороны,"
        ]

        self.second = [
            "парадигма цифровой экономики",
            "контекст цифровой трансформации",
            "диджитализация бизнес-процессов",
            "прагматичный подход к цифровым платформам",
            "совокупность сквозных технологий ",
            "программа прорывных исследований",
            "ускорение блокчейн-транзакций ",
            "экспоненциальный рост Big Data",
        ]

        self.third = [
            "открывает новые возможности для",
            "выдвигает новые требования",
            "несет в себе риски",
            "расширяет горизонты",
            "заставляет искать варианты",
            "не оставляет шанса для ",
            "повышает вероятность",
            "обостряет проблему",
        ]

        self.fourth = [
            "дальнейшего углубления",
            "бюджетного финансирования",
            "синергитического эффекта",
            "компрометации конфиденциальных",
            "универсальной коммодитизации",
            "несанкционированной кастомизации",
            "нормативного регулирования",
            "практического применения"
        ]

        self.fifth = [
            "знаний и компетенций.",
            "непроверенных гипотез.",
            "волатильных активов.",
            "опасных экспериментов.",
            "государственно-частных партнёрств",
            "цифровых следов граждан.",
            "нежелательных последствий.",
            "внезапных открытий",

        ]

    def return_declar(self):
        res_many = []
        messag = {}

        rand = f'{random.choice(self.first)} {random.choice(self.second)} {random.choice(self.third)} {random.choice(self.fourth)} {random.choice(self.fifth)}'

        if self.times == 0:
            messag["message"] = rand

            jmessag = json.dumps(messag, ensure_ascii=False)
            return jmessag
        if self.times > 0:

            for i in range(self.times):

                res_many.append(rand)

            messag["messages"] = res_many
            jmessag = json.dumps(messag, ensure_ascii=False)
            return jmessag

a = Declar()
r = a.return_declar()
print(r)