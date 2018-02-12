# Created to read information from locations.list
# Return information in form of dictionary


def read_file():
    '''
    () -> dictionary
    return: dictionary wit year as key, list with films and locations in list
    as value
    '''
    with open('locations.list') as file:
        # Skip first lines
        for i in range(14):
            next(file)
        information = {}
        for line in file:
            index1 = line.strip().find('(')
            # Trying to transform information between '(' and ')' into year
            try:
                key, value = int(line[index1 + 1:index1 + 5]), line[0:index1] + \
                             line[index1 + 6::]
            except Exception:
                continue

            value = value.split('\t')
            # Deleting of unuseful information
            if value[-1].startswith('('):
                value = value[0:-1]

            # Creating of the dictionary
            value = [value[0], value[-1].strip()]

            if key not in information:
                information[key] = [value]
            else:
                information[key].append(value)
        print(list((key, len(information[key])) for key in information))
        return information
