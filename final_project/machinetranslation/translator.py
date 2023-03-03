import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

import os
from dotenv import load_dotenv


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)

language_translator.set_service_url(url)


def englishToFrench(englishText):
    if englishText =='':
        return 'Empty'
    translation = language_translator.translate(englishText, model_id='en-fr').get_result()
    frenchText= translation.get("translations")[0].get("translation")
    return frenchText
    
#englishToFrench(englishText="Hello")

def frenchToEnglish(frenchText):
    if frenchText =='':
        return 'Empty'
    translation = language_translator.translate(frenchText, model_id='fr-en').get_result()
    englishText= translation.get("translations")[0].get("translation")
    return englishText
    
#frenchToEnglish(frenchText="Bonjour")

