from pprint import pprint
import re
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    new_contact_list = []
    len_title = len(contacts_list[0])


def editing_data():
    for contact in contacts_list:
        '''Разделение ФИО путем перебора и условия (Ф + ИО, ФИО == Ф+И+О)'''
        zero_contact = (contact[0].split())
        one_contact = (contact[1].split())
        if len(zero_contact) == 1:
            pass

            if len(one_contact) == 1:
                pass

            else:
                for x in range(len(one_contact)):
                    contact[x+1] = one_contact[x]

        else:
            for x in range(len(zero_contact)):
                contact[x] = zero_contact[x]
    return


def editing_number():
    '''Функция для редактирвоания номера телефона'''
    pattern_obj = re.compile(r"(\+7|8)?\s?\(?(\d{3})\)?[\-]?\s?(\d{3})[\-]?(\d{2})[\-]?(\d{2})[\-]?\s?\(?(доб.)?\s?(\d+)?\)?")
    for contact in contacts_list:
        contact[-2] = pattern_obj.sub(r"+7(\2)\3-\4-\5 \6\7", contact[-2])
    return


def del_clon():
    '''Функция для обработки дублей'''
    for contact in contacts_list[1:]:
        first_name = contact[0]
        last_name = contact[1]
        for new_contact in contacts_list:
            new_first_name = new_contact[0]
            new_last_name = new_contact[1]
            if first_name == new_first_name and last_name == new_last_name:
                if contact[2] == '':
                    contact[2] = new_contact[2]
                if contact[3] == '':
                    contact[3] = new_contact[3]
                if contact[4] == '':
                    contact[4] = new_contact[4]
                if contact[5] == '':
                    contact[5] = new_contact[5]
                if contact[6] == '':
                    contact[6] = new_contact[6]

    for contact in contacts_list:
        if len(contact) != len_title:
            del contact[-1]

        if contact not in new_contact_list:
            new_contact_list.append(contact)
    return new_contact_list



if __name__ == '__main__':
    editing_data()
    editing_number()
    del_clon()
    pprint(new_contact_list)

    with open("phonebook.csv", "w", encoding='utf-8') as nf:
        datawriter = csv.writer(nf, delimiter=',')
        datawriter.writerows(new_contact_list)




