'''favorite_languages={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}'''
'''for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite languages is {language.title()}")'''

'''for name in favorite_languages.keys():
	print(name.title())'''

'''friends=['phil', 'sarah']
for name in favorite_languages.keys():
	print(f"hi {name.title()}")
	if name in friends:
		language=favorite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}")'''

'''for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking this poll.")'''

'''print("the following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())'''

favorite_languages={
	'jen':['python', 'ruby'],
	'sarah':['c'],
	'edward':['ruby', 'go'],
	'phil':['python', 'haskell']
	}
for  name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"{language.title()}")
		



































