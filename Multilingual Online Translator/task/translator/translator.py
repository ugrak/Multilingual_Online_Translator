from requests import get
from bs4 import BeautifulSoup
print('''Type "en" if you want to translate from French into English,
 or "fr" if you want to translate from English into French:''')
language = input()
print('Type the word you want to translate:')
word = input()
print(f'You chose "{language}" as a language to translate "{word}".')

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}
if language == 'en':
    language = 'english-french/'
elif language == 'fr':
    language = 'french-english/'
response = get('https://context.reverso.net/translation/' + language + word, headers=headers)
if response.status_code == 200:
    print('200 OK')
soup = BeautifulSoup(response.content, 'html.parser')
translations = soup.find_all(['a', 'div'], {'class': 'translation'})
translation_list = []
for word in translations:
    translation_list.append(word.get_text().strip())
print(translation_list)
examples = soup.select('#examples-content span.text')
example_list = [phrase.get_text().strip() for phrase in examples]
print(example_list)
