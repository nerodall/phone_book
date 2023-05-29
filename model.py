phone_book: list[dict[str, str]] = []
path = 'phones.txt'


def open_pb():
    global phone_book
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(':')
        new = {'0id': contact[0], '1name': contact[1], '2phone': contact[2], '3comment': contact[3]}
        phone_book.append(new)


def save_pb():
    global phone_book
    data = []
    for contact in phone_book:
        # if contact.get('name') != 'deleted':
        data.append(':'.join([value for value in contact.values()]))
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)


def get_bp():
    global phone_book
    return phone_book


def add_contact(new: dict[str, str]) -> str:
    global phone_book
    new_id = int(phone_book[-1].get('0id')) + 1
    new['0id'] = str(new_id)
    phone_book.append(new)
    return new.get('0id')


def search_contact(word: str) -> list[dict[str, str]]:
    global phone_book
    result = []
    for contact in phone_book:
        for field in contact.values():
            if word.lower() in field.lower():
                result.append(contact)
                break
    return result


def change_contact(new: dict, index: int):
    global phone_book
    for contact in phone_book:
        if index == contact.get('0id'):
            contact['1name'] = new.get('1name', contact.get('1name'))
            contact['2phone'] = new.get('2phone', contact.get('2phone'))
            contact['3comment'] = new.get('3comment', contact.get('3comment'))

            return contact.get('name')


def delete_contact(index: int):
    global phone_book
    for contact in phone_book:
        if index == contact.get('0id'):
            contact['1name'] = 'deleted'
            return contact.get('1name')
