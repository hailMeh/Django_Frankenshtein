def make_password():
    import random

    my_keywords = 'qwertyuioplkjhgfdsazxcvbnm!@#$%^&*()+_-1234567890QAZXSWEDCVFRTGBNHYUJM<KIOLP:{"|}'
    list_of_keywords = list(my_keywords)  # my_keywords.split('')
    password = []
    for p in list_of_keywords:
        if len(password) <= 12:
            new_symbol = random.choice(list_of_keywords)
            password.extend(new_symbol)
    return ''.join(password)