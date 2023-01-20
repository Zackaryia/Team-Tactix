
def zip_fill_none(l1, l2):
    longest_len = max(len(l1), len(l2))
    
    rl = []

    for i in range(longest_len):
        x = []
        
        if i < len(l1):
            x.append(l1[i])
        else:
            x.append(None)
        
        if i < len(l2):
            x.append(l2[i])
        else:
            x.append(None)
        
        rl.append(x)
    
    return rl

def get_largest_key_from_list_of_dicts(list_of_dicts, key):
    largest_dict_index = None
    largest_value = None
    
    for dict_i in range(len(list_of_dicts)):
        dict = list_of_dicts[dict_i]

        if largest_value == None or dict[key] > largest_value:
            largest_value = dict[key]
            largest_dict_index = dict_i
    return largest_dict_index