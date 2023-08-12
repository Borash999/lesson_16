# Возьмите любые 1-3 задачи из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации. 
# Также реализуйте возможность запуска из командной строки с передачей параметров.

def convert_format(input: list[str] = None) -> list[float]:
    if len(input) == 1:
        j = 0
    else:
        j = 1
    m_1 = []
    m_2 = []
    input[j].append(' ')
    for i in input[j]:
        if i == ' ':
            m_2.append(list(m_1))
            m_1.clear()
        else:
            m_1.append(float(i))
    return m_2


