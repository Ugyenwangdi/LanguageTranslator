import googletrans  # In order to use google trans library
from googletrans import Translator

t = Translator()

# Store all the supported languages in a variable
supported_langs = googletrans.LANGUAGES   # This will be a python dictionary

# Print all the languages in 
print('Supported languages: ')
for key, value in supported_langs.items():
    print(key, ':', value)

# Get the source language
def get_source():
    source_lang = input('Source language: ')

    # is source_lang in lanuguage keys
    if source_lang in supported_langs.keys():
        return source_lang

    # Check if it is present in language values
    for key, value in supported_langs.items():
        if source_lang == value:   # Check if the value is in 
            return key
            
    else:
        return ''

# Get destination language
def get_dest():
    dest_lang = input('Translate to: ')    
    
    # if dest_lang in language key
    if dest_lang in supported_langs.keys():
        return dest_lang

    # Check if it is present in language values
    for key, value in supported_langs.items():
        if dest_lang == value:   # Check if the value is in 
            return key

    else:
        return ''

def translate():
    print('Choose the language from the supported languages')
    source_lang = get_source()
    # print(source_lang)
    
    dest_lang = get_dest()
    # print(dest_lang)

    text = input("Enter your Text: ")
    print("Text to be translated: "+ text)

    # Let's print the language of input text
    input_text = t.translate(text)
    s = input_text.src
    print('Entered text is in:', s) 

    # We can obtain the attributes with following
    # print(result.src)
    # print(result.dest)
    # print(result.origin)
    # print(result.text)
    # print(result.pronunciation)


    # The get_source() or get_dest() returns null means inputs are invalid which means the language is unsupported
    if source_lang == '' or dest_lang == '':
        print("Invalid input...")

    try:
        if source_lang and dest_lang:  
            # Using translate() method which requires
            # three arguments, 1st the sentence which needs to be translated 
            # 2nd source language
            # and 3rd to which we need to translate in
            result = t.translate(text, src=source_lang, dest=dest_lang)   # Translate the text 

            # Ensure the input to be entered using the language specified
            if source_lang == s:
                print(f'Translated text to {supported_langs[dest_lang]}: {result.text}')
                print(f"Pronunciation in {supported_langs[dest_lang]}: {result.pronunciation}")

            else:
                print('Enter in ', supported_langs[source_lang])

    except:
        print("Unable to understand the input...")

    

if __name__=='__main__':
    translate()  # Run it continuously
    while True:
        q = input('Do you want to continue? (y/n): ')
        if q == 'n':
            break
        else:
            translate()







