
def check_input(input):
    if input.isnumeric():
        return f'input value cannot be numeric'
    if input.split()[0] not in ['view', 'make', 'quit']:
        return f'Wrong input order'
    return True