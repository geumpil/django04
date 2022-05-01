import googletrans
from googletrans import Translator
 
d = googletrans.LANGUAGES 
text1 = "Hello welcome to my website!"
translator = Translator() 
for i in d:

    trans1 = translator.translate(text1, src='ko', dest=i)
    print(f"{d[i]} 인사 : ", trans1.text)
