translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}
word=input('Enter english word to translate: ')
if word in translations:
    print('Translated word in PL:', translations[word])
else:
    print('Translation unvailable')