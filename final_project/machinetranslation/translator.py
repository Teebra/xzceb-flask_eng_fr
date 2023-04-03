""" Python Web Application Creation and Deployment """
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def english_to_french(english_text):
    #write the code here
    """authentication and Translate English To French"""
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    language_translator.set_service_url(url)

    if not english_text:
        return ""

    if english_text is None:
        return ""
    else:
        #Translate the text from English to French
        translation = language_translator.translate(
        text=english_text,
        source='en',
        target='fr'
        ).get_result()
    
        #extract the translated text
        french_text = translation['translations'][0]['translation']
        return french_text

def french_to_english(french_text):
    #write the code here
    """authentication and Translate French to English"""
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    language_translator.set_service_url(url)

    if not french_text:
        return ""

    #Translate the text from French to English
    if french_text is None:
        return ""
    else:
        translation = language_translator.translate(
        text=french_text,
        source='fr',
        target='en'
        ).get_result()
    
        #extract the translated text
        english_text = translation['translations'][0]['translation']
        return english_text