favorite_languages = {'jen':['python','ruby'],'sarah':['c'],'edward':['ruby','go'],'phil':['python','haskell'],}
for name, languages in favorite_languages.items():
    print("\n"+name.title()+"'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
#friends = ['phil','sarah']
#other_friends = ['jen','edward']
#for name in favorite_languages.keys():
#    if name in friends:
#        print(name.title()+", participou da enquente.")
#    elif name in other_friends:
#        print(name.title()+", não participou da enquete.")
#print("The following languages have benn mentioned:")
#for language in set(favorite_languages.values()):
#    print(language.title())
#for language in favorite_languages.values():
#    print(language.title())
#for name in sorted(favorite_languages.keys()):
#    print(name.title()+" thank you for taking the poll.")
#if 'erin' not in favorite_languages.keys():
#    print("Erin, please take our poll!")
#print("Sarah's favorite language is "+favorite_languages['sarah'].title()+".")
#for name in favorite_languages.keys():
#    print(name.title())
#    if name in friends: 
#        print("Hi " + name.title()+", I see your favorite language is "+favorite_languages[name].title()+"!")

#for name, language in favorite_languages.items():
#    print(name.title()+"'s favorite language is "+ language.title()+".")