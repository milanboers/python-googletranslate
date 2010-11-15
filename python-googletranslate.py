# Google Translate for Python 2 v0.2.1
# By Milan Boers, 2010
# Licensed under the MIT license
#
# Usage:
# myTranslation = Translation("Text to be translated")
# 
# To detect the language
# myTranslation.detectLanguage()
#
# To translate from English to French
# myTranslation.translate('en','fr')
#
# Or combine both, translating from a detected language to French
# myTranslation.translate('fr')
#
# For a complete list of the language codes see http://code.google.com/apis/language/translate/v2/using_rest.html#language-params
# ValueError exception is raised when one of the parameters is wrong
# IOError exception is raised when the connection to Google could not be made
# KeyError is raised when you forgot to set the API key

try:
	import simplejson as json
except ImportError:
	import json
import urllib

# Get a key at http://code.google.com/apis/console and place it here
GOOGLE_API_KEY = ''
# Google Translate URL. You don't want to touch this.
TRANSLATE_URL = 'https://www.googleapis.com/language/translate/v2'

class Translation:
	def __init__(self, text):
		self.translateString = text;
		
	def getGTranslateFeedback(self, params):
		page     = urllib.urlopen(TRANSLATE_URL + "?%s" % params)
		return json.loads(page.read())
	
	def detectLanguage(self):
		params   = urllib.urlencode({'key' : GOOGLE_API_KEY, 'target' : 'en', 'q' : self.translateString})
		feedback = self.getGTranslateFeedback(params)
		
		language = feedback['data']['translations'][0]['detectedSourceLanguage']
		return language
		
	def translate(self,language,targetLanguage = None):
		if targetLanguage == None:
			params   = urllib.urlencode({'key' : GOOGLE_API_KEY, 'target' : language, 'q' : self.translateString})
		else:
			params   = urllib.urlencode({'key' : GOOGLE_API_KEY, 'source' : language, 'target' : targetLanguage, 'q' : self.translateString})
		
		feedback = self.getGTranslateFeedback(params)
		
		translation = feedback['data']['translations'][0]['translatedText']
		return translation
	
	@staticmethod
	def dctDetectLanguage(text):
		thisTranslation = Translation(text)
		return thisTranslation.detectLanguage()
	
	@staticmethod
	def dctTranslate(text,language,TargetLanguage = None):
		thisTranslation = Translation(text)
		return thisTranslation.translate(language,TargetLanguage)