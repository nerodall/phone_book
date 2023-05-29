import text
import view
import model


def start():
    while True:
        choice = view.main_menu()

        match choice:
            case 1:
                model.open_pb()
                view.print_message(text.load_successful)
            case 2:
                model.save_pb()
                view.print_message(text.save_successful)
            case 3:
                pb = model.get_bp()
                view.print_contacts(pb, text.pb_empty)
            case 4:
                contact = view.input_contact(text.input_new_contact)
                name = model.add_contact(contact)
                view.print_message(text.new_contact_successful(name))
            case 5:
                key_word = view.input_search(text.input_search)
                result = model.search_contact(key_word)
                view.print_contacts(result, text.empty_search(key_word))
            case 6:
                key_word = view.input_search(text.input_change)
                result = model.search_contact(key_word)
                if result:
                    if len(result) != 1:
                        view.print_contacts(result, '')
                        current_id = view.input_search(text.input_index)
                    elif not result:
                        view.print_message(text.empty_search(key_word))
                    else:
                        current_id = result[0].get('0id')
                    new_contact = view.input_contact(text.change_contact)
                    name = model.change_contact(new_contact, current_id)
                    view.print_message(text.change_successful(name))
                else:
                    view.print_message(text.empty_search(key_word))
            case 7:
                key_word = view.input_search(text.input_delete_contact)
                result = model.search_contact(key_word)
                if result:
                    if len(result) != 1:
                        view.print_contacts(result, '')
                        current_id = view.input_search(text.input_index)
                    elif not result:
                        view.print_message(text.empty_search(key_word))
                    else:
                        current_id = result[0].get('0id')
                    name = model.delete_contact(current_id)
                    view.print_message(text.contact_deleted)
            case 8:
                break
