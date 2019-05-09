def sort_contacts(contact_dict):
    contact_dictItems = sorted(contact_dict.items())
    contact_dict_list = list(contact_dictItems)
    
    sorted_list = []
    for key, value in contact_dict_list:
        sorted_list.append((key, value[0], value[1]))
    
    return sorted_list
    
