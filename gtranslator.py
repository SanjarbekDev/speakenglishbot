from googletrans import Translator
tr=Translator()
# translate=translator.translate("Salom",dest='en')
# detect_lan=translator.detect('mening ismim sanjar')

# print(translate.text)
# print(detect_lan.lang)

def translator(word):
    lang=tr.detect(word).lang
    dest='uz' if lang=='en' else 'en'
    return tr.translate(word,dest=dest).text 

def detect_lang(word):
    return tr.detect(word).lang

if __name__=='__main__':
    print(detect_lang('salom'))