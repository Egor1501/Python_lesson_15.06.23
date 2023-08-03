# скрипт, который для пяти целочисленных значений (вводит пользователь с клавиатуры), находит минимум, максимум и среднее.
if __name__ == '__main__':
    a, b, c, d, e = int(input('a=')),\
                    int(input('b=')),\
                    int(input('c=')),\
                    int(input('d=')),\
                    int(input('e='))

    print('Max=', max(a, b, c, d, e))
    print('Min=', min(a, b, c, d, e))
    print('Avg=', (a + b + c + d + e) / 5)
