from requests import get
from bs4 import BeautifulSoup


def parse(language, word):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}
    response = get('https://context.reverso.net/translation/' + language + word, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    translations = soup.find_all(['a', 'div'], {'class': 'translation'})
    translation_list = []
    for word in translations:
        translation_list.append(word.get_text().strip())
    examples = soup.select('#examples-content span.text')
    example_list = [phrase.get_text().strip() for phrase in examples]
    return translation_list, example_list


def get_translate(language, word, number, out_lang):
    translation_list, example_list = parse(language, word)
    if number == 1:
        with open(f'/Users/aleksandrugrak/PycharmProjects/Multilingual Online Translator/'
                  f'Multilingual Online Translator/task/{word}.txt', 'a') as file:
            file.write(f'{lang_dict[out_lang]} Translations:\n')
            file.write(translation_list[1] + '\n')
            file.write(f'\n{lang_dict[out_lang]} Examples:\n')
            file.write(example_list[0] + '\n')
            if out_lang == 13:
                file.write(example_list[1])
            else:
                file.write(example_list[1] + '\n\n\n')

    print(f'\n{lang_dict[out_lang]} Translations:')
    for i in translation_list[1:number + 1]:
        print(i)
    print(f'\n{lang_dict[out_lang]} Examples:')
    counter = 0
    for i in example_list[:number * 2]:
        print(i)
        counter += 1
        if counter == 2:
            print()
            counter = 0


if __name__ == "__main__":
    print('''Hello, welcome to the translator. Translator supports: 
    1. Arabic\n2. German\n3. English\n4. Spanish\n5. French\n6. Hebrew\n7. Japanese
8. Dutch\n9. Polish\n10. Portuguese\n11. Romanian\n12. Russian\n13. Turkish''')
    inp_lang = int(input('Type the number of your language:\n'))
    out_lang = int(input("Type the number of a language you want "
                         "to translate to or '0' to translate to all languages:\n"))
    word = input('Type the word you want to translate:\n')
    lang_dict = {1: 'Arabic', 2: 'German', 3: 'English', 4: 'Spanish', 5: 'French', 6: 'Hebrew', 7: 'Japanese',
                 8: 'Dutch', 9: 'Polish', 10: 'Portuguese', 11: 'Romanian', 12: 'Russian', 13: 'Turkish'}

    if out_lang == 0:
        for key, value in lang_dict.items():
            if key != inp_lang:
                language = lang_dict[inp_lang].lower() + '-' + lang_dict[key].lower() + '/'
                get_translate(language, word, 1, key)
    else:
        language = lang_dict[inp_lang].lower() + '-' + lang_dict[out_lang].lower() + '/'
        get_translate(language, word, 5, out_lang)
