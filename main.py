from Email_func import  email_gen
import  data_refactoring

main_file = open('task_file.txt')
users_list = []
#Парсим текстовый файл построчно, создавая список из пользователей
for line in main_file:
    list_return = data_refactoring.cast_to_list(line)
    users_list.append(list_return)
main_file.close()

result_list = [users_list[0]]
users_list.pop(0)

list_usernames=[]
#список имен пользователей
for list in range(0, len(users_list)):
    list_username=[]
    for elem in range(1, 3):
        list_username.append(users_list[list][elem])
    list_usernames.append(list_username)

#Генерируем e-mail абсолютно всем пользователям
user_emails = email_gen(list_usernames)

#Соединяем два списка: список с пользователями и список с их созданными e-mail. Если у пользователя некорректны вписаны
# данные, то вместе ячейки 'e-mail' будет написано 'Not e-mail'
for i in range(0, len(users_list)):
    for j in range(0, len(users_list[i])):
        if (users_list[i][1] != '' and users_list[i][2] != '' and users_list[i][3] != '' and users_list[i][4] != ''
                and len(users_list[i][3])==7):
            users_list[i][0] = user_emails[i]
        else:
            users_list[i][0] = 'Not e-mail'
    result_list.append([users_list[i]])

#Создаем файл 'task_file_new.txt' с результатом программы
new_file = open('task_file_new.txt', 'w')
new_file.write(', '.join(map(str, result_list[0])) + '\n\n')
for user in range(1,len(result_list)):
    string=''
    for i in range(0,len(result_list[user])):
        string = ', '.join(map(str,result_list[user][i]))
        new_file.write(string+'\n\n')