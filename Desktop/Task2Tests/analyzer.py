import re


def analyzer(text):
    characters_counter = 0
    words_counter = 0
    exclamation_mark = 0
    dot = 0
    question_mark = 0
    three_dots = 0
    for i in text:
        if i.isalpha() or i.isdigit():
            characters_counter += 1
        elif i == '!':
            exclamation_mark += 1
        elif i == '.':
            dot += 1
        elif i == '?':
            question_mark += 1
        elif i == '…':
            three_dots += 1
        sentences_counter = (dot + exclamation_mark + question_mark + three_dots)
    opt = re.sub(r'[^\w\s]', '', text)
    split_regex = re.compile(r'[.!?…]')
    for c in opt.split():
        if c.isalpha() or c.isdigit():
            words_counter += 1
        time = (round((words_counter / 1500), 2))
    sentences = filter(lambda t: t, [t.strip() for t in split_regex.split(text)])
    count_comma = 0
    for s in sentences:
        if ',' in s:
            count_comma += 1
    return f'Text contains: {characters_counter} characters, {words_counter} words, ' \
           f'{sentences_counter} \
    sentences, {dot} sentences with dot, {exclamation_mark} \
    sentences with exclamation mark, {question_mark} sentences \
    with question mark, {count_comma} sentences with one or more comma, \
    you need {time}  min to reed it.'


if __name__ == '__main__':
    analyzer("What Is an Example of an API?")


