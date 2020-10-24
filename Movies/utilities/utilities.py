def serialize(list_ids, string):
    for i in range(len(list_ids) - 1):
        string += "{0}".format(list_ids[i])
        if i != len(list_ids) - 1:
            string += " "
    return string
