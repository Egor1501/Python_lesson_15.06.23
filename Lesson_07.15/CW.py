


def schedule(file_name: str):
    result = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            tmp = line.split(';')
            key = tmp[0].strip() + '-' + tmp[1].strip()
            value = tmp[-1].strip()
            result[key] = value

    return result

