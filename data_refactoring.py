def cast_to_list(input_line):
    """Разделение строки на элементы списка для удобства обработки"""
    line_list = input_line.split(", ")
    new_list =[]
    for i in line_list:
        new_list.append(i.strip())

    return new_list
