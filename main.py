
class Contact:
    def __init__(self, name, last_name, phone_number, favorite_contact=False, **kwargs):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.favorite_contact = favorite_contact
        self.add_info = [f'{contact_type}: {contact}' for contact_type, contact in kwargs.items()]

    def __str__(self):
        new_str = '\n\t'
        return \
            f'Имя: {str(self.name)}\n' \
            f'Фамилия: {str(self.last_name)}\n' \
            f'Телефон: {str(self.phone_number)}\n' \
            f'В избранных: {"да" if self.favorite_contact else "нет"}\n' \
            f'Дополнительная информация:' \
            f'{new_str + new_str.join(contact for contact in self.add_info) if self.add_info else ""}' \
            f'{new_str + "нет" if not self.add_info else ""}'


class PhoneBook:
    def __init__(self, name):
        self.name = name
        self.contact_list = []

    def show_contact(self):
        for Contact in self.contact_list:
            print(Contact)

    def add_contact(self, Contact):
        self.contact_list.append(Contact)
        print('Контакт добавлен')

    def delete_contact(self, phone):
        for Contact in self.contact_list:
            if Contact.phone_number == phone:
                self.contact_list.remove(Contact)
                print('Контакт удалён')

    def search_favorite(self):
        for Contact in self.contact_list:
            if Contact.favorite_contact:
                print(Contact.phone_number)
            else:
                print('Контакт не добавлен в "Избранное"')

    def search_contact(self, name, last_name):
        for Contact in self.contact_list:
            if Contact.name == name and Contact.last_name == last_name:
                print(f'{Contact.name} {Contact.last_name}\n{Contact.phone_number}')


jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
michael = Contact('Michael', 'Fernando', '+79243581976', favorite_contact=True,
                  telephone='+79536541387', email='fermic@proton@com')

book = PhoneBook('The Book')

print(jhon)
print(michael)

# book.add_contact(jhon)
# book.add_contact(michael)
# book.show_contact()
# book.search_favorite()
# book.search_contact('Alex', 'White')
# book.search_contact('Michael', 'Fernando')
# book.search_contact('Jhon', 'Smith')
# book.delete_contact('+71234567809')
# book.search_contact('Jhon', 'Smith')
