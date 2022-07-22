# В качестве примера исправления ошибок с помощью PEP 8, я выбрал код из задания 3

def compare(obj1,obj2):

    # PEP 8: E231 отсутствует пробел после ','

    ngrams = [obj1[i:i + 3] for i in range (len(obj1))]

    # PEP 8: E211 пробел перед '('

    count = 0
    for ngram in ngrams:
        count += obj2.count(ngram)
    return count / max(len(obj1), len(obj2))

# PEP 8: E305 ожидал 2 пустых строки после определения класса или функции, найдено 0

pairs = [
    ('saturday', 'sandy'),
    ('kitten', 'sitting'),
    ('feeling', 'fear'),
    ('море', 'гора'),
    ('спорт', 'спортивный'),
    ('компьютер', 'компьютерный'),
    ('сон', 'нос'),
]
if __name__ == '__main__':
    for s,t in pairs:

        # PEP 8: E231 отсутствует пробел после ','

        print(s,t, compare(s,t))

        # PEP 8: E231 отсутствует пробел после ','

"""
-------------------------------------------------------------------------------------------------------------------------------
"""


# Исправленный вариант:

def compare(obj1, obj2):
    ngrams = [obj1[i:i + 3] for i in range(len(obj1))]
    count = 0
    for ngram in ngrams:
        count += obj2.count(ngram)
    return count / max(len(obj1), len(obj2))


pairs = [
    ('saturday', 'sandy'),
    ('kitten', 'sitting'),
    ('feeling', 'fear'),
    ('море', 'гора'),
    ('спорт', 'спортивный'),
    ('компьютер', 'компьютерный'),
    ('сон', 'нос'),
]
if __name__ == '__main__':
    for s, t in pairs:
        print(s, t, compare(s, t))

# Вывод: после исправления всех ошибок, код стал читаться и выглядеть лучше.