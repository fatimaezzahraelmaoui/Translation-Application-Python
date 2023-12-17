# pip install translator - translate
import translate
from translate import Translator
data = Translator(from_lang="french", to_lang="english")
res = data.translate("merci")
print(res)