def generate_suffix(str, sign=''):
    suffixes = []
    for i in range(len(str)):
        print(str[i:])
        suffixes.append(str[i:])
    return suffixes

def generate_prefix(str, sign=''):
    prefixes = []
    for i in range(len(str)+1):
        prefixes.append(str[:i]);
    if not sign:
        return prefixes
    else:
        return prefixes + [sign]



if __name__ == '__main__':
    suffixes = generate_suffix('banana')
    prefixes = generate_prefix('banana', '$')
    print(suffixes)
    print(prefixes)
