class LanguageTranslator:
    def __init__(self):
        self.language_translation = {
            "Hello": {
                "Spanish": "Holla",
                "Indiana": "Namaste",
                "Korean": "Yebuseo"
            },
            "Good Morning": {
                "Spanish": "adios",
                "Indiana": "SuPrabhat",
                "Korean": "Anyogeseo"
            }
        }

    def translate(self,word,language):
        if word in self.language_translation:
            if language in self.language_translation[word]:
                return self.language_translation[word][language]
            else:
                return f"Transalation can not be done for {language}"
        else:
            return "Word not found!"
        

lt=LanguageTranslator()

print(lt.translate("Hello","Spanish"))
print(lt.translate("Hella","Spanish"))
