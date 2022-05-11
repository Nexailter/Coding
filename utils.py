def check_class(character_class):
    if character_class == "Hunter" or character_class == "Demon" or character_class == 'Wizard':
        return True
    else:
        return False

def check_element(character_element):
    if character_element == 'ice' or character_element == 'lightning' or character_element == 'fire' or character_element == 'earth': 
        return True
    else:
        return False

def check_username(character_username):
    bad_words = ['fuck','fuck off',' ','shit','asshole','penis']
    if character_username not in bad_words:
        return True

    else:
        return False
