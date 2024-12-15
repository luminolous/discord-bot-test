from random import choice, randint

def get_responses(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well you\'re awfully silent...'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'how are you' in lowered:
        return 'I\'m doing well, thank you!'
    elif 'weather' in lowered:
        return f'The weather is {choice(["sunny", "cloudy", "rainy"])} today.'
    elif 'goodbye' in lowered:
        return 'Goodbye!'
    elif 'joke' in lowered:
        jokes = [
            'Why did the chicken cross the road?',
            'Why did the scarecrow win an award?',
            'Why did the tomato turn red?',
            'Why did the cow cross the road?',
            'Why did the elephant win an award?',
            'Why did the puppy go to the dentist?',
            'Why did the cowboy go to the doctor?',
            'Why did the scarecrow get lost?',
            'Why did the fox cross the road?',
            'Why did the cowboy get lost?',
            'Why did the mouse go to the doctor?',
            'Why did the chicken go to the dentist?',
            'Why did the scarecrow get lost?',
            'Why did the puppy get lost?',
            'Why did the cowboy get lost?',
            'Why did the cowboy get lost?']
        return choice(jokes)
    elif 'random number' in lowered:
        return f'Here is a random number: {randint(1, 100)}'
    else:
        return choice(['I do not understand...', 
                       'What are you talking about?', 
                       'Do you mind rephrasing that?'])
