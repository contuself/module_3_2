def send_email(message, recipient, *, sender = "university.help@gmail.com"): #функция
    if "@" not in recipient or "@" not in sender or not recipient.endswith((".com", ".ru", ".net")) or not sender.endswith((".com", ".ru", ".net")): #условие, которое проверяет наличие все символов в почте
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}") #вывод на экран
    elif recipient == sender: #упроверка на отличие
        print("Нельзя отправить письмо самому себе!") #вывод на экран
    elif sender == "university.help@gmail.com": #условие. Если почта по умолчанию, то
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}") #вывод на экран
    else: #иначе
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}") #вывод на экран

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com') #вывод на экран
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com') #вывод на экран
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk') #вывод на экран
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru') #вывод на экран