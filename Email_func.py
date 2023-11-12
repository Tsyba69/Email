def email_gen(list_of_names):
    """Генерация e-mail исходя из имени и фамилии пользователя"""
    emails = []
    for i in list_of_names:
        letter = 1
        number = 1
        while (i[1] + '.' + i[0][0:letter] + '@company.io') in emails:
            letter += 1
            if letter > len(i[0]):
                break

        if letter > len(i[0]):
            while (i[1] + '.' + i[0][0:letter] + str(number) + '@company.io') in emails:
                number += 1
            emails.append(i[1] + '.' + i[0][0:letter] + str(number) + '@company.io')
        else:
            emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails