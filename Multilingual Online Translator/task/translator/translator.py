from requests import get
from bs4 import BeautifulSoup

print('''Hello, you're welcome to the translator. Translator supports: 
1. Arabic
2. German
3. English
4. Spanish
5. French
6. Hebrew
7. Japanese
8. Dutch
9. Polish
10. Portuguese
11. Romanian
12. Russian
13. Turkish''')
inp_language = int(input('Type the number of your language:\n'))
out_language = int(input('Type the number of language you want to translate to:\n'))
word = input('Type the word you want to translate:\n')

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}
lang_dict = {1: 'Arabic', 2: 'German', 3: 'English', 4: 'Spanish', 5: 'French', 6: 'Hebrew', 7: 'Japanese',
             8: 'Dutch', 9: 'Polish', 10: 'Portuguese', 11: 'Romanian', 12: 'Russian', 13: 'Turkish'}

language = lang_dict[inp_language].lower() + '-' + lang_dict[out_language].lower() + '/'
response = get('https://context.reverso.net/translation/' + language + word, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')
translations = soup.find_all(['a', 'div'], {'class': 'translation'})
translation_list = []
for word in translations:
    translation_list.append(word.get_text().strip())
print(f'\n{lang_dict[out_language]} Translations:')
for i in translation_list[1:6]:
    print(i)

examples = soup.select('#examples-content span.text')
example_list = [phrase.get_text().strip() for phrase in examples]
print(f'\n{lang_dict[out_language]} Examples:')
counter = 0
for i in example_list[:10]:
    print(i)
    counter += 1
    if counter == 2:
        print()
        counter = 0
