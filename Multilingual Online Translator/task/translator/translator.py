from requests import get
from bs4 import BeautifulSoup
from sys import argv


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


def get_translate(language, word, number):
    translation_list, example_list = parse(language, word)
    out_lang = language.replace('/', '').split('-')[1]
    if number == 1:
        with open(f'/Users/aleksandrugrak/PycharmProjects/Multilingual Online Translator/'
                  f'Multilingual Online Translator/task/{word}.txt', 'a') as file:
            file.write(f'{out_lang.capitalize()} Translations:\n')
            file.write(translation_list[1] + '\n')
            file.write(f'\n{out_lang.capitalize()} Examples:\n')
            file.write(example_list[0] + '\n')
            if out_lang.lower() == 'turkish':
                file.write(example_list[1])
            else:
                file.write(example_list[1] + '\n\n\n')

    print(f'\n{out_lang.capitalize()} Translations:')
    for i in translation_list[1:number + 1]:
        print(i)
    print(f'\n{out_lang.capitalize()} Examples:')
    counter = 0
    for i in example_list[:number * 2]:
        print(i)
        counter += 1
        if counter == 2:
            print()
            counter = 0


if __name__ == "__main__":
    lang_dict = {0: 'all', 1: 'arabic', 2: 'german', 3: 'english', 4: 'spanish', 5: 'french', 6: 'hebrew',
                 7: 'japanese', 8: 'dutch', 9: 'polish', 10: 'portuguese', 11: 'romanian', 12: 'russian', 13: 'turkish'}
    if len(argv) == 4:
        inp_lang, out_lang, word = argv[1], argv[2], argv[3]
    else:
        print('''Hello, welcome to the translator. Translator supports: 
1. Arabic\n2. German\n3. English\n4. Spanish\n5. French\n6. Hebrew\n7. Japanese
8. Dutch\n9. Polish\n10. Portuguese\n11. Romanian\n12. Russian\n13. Turkish''')
        inp_lang = int(input('Type the number of your language:\n'))
        out_lang = int(input("Type the number of a language you want "
                             "to translate to or '0' to translate to all languages:\n"))
        word = input('Type the word you want to translate:\n')
        inp_lang = lang_dict[inp_lang]
        out_lang = lang_dict[out_lang]

    if out_lang == 'all':
        for key, value in lang_dict.items():
            if lang_dict[key] != inp_lang and lang_dict[key] != 'all':
                language = inp_lang.lower() + '-' + lang_dict[key].lower() + '/'
                get_translate(language, word, 1)
    else:
        language = inp_lang.lower() + '-' + out_lang.lower() + '/'
        get_translate(language, word, 5)
