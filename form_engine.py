import sys, glob, errno
import json
import uuid
import pdfkit

class form_engine:
	TEMPLATE_PATH = './templates/'
	OUTPUT_PATH = './output/'
	TEMPLATE_FILE_EXTENSION = '.json'
	OUTPUT_FILE_EXTENSION = '.pdf'

	def getTemplates(self):
		TEMPLATE_PATH = './templates/'
		TEMPLATE_FILE_EXTENSION = '.json'
		path = TEMPLATE_PATH + '*' + TEMPLATE_FILE_EXTENSION
		outputDict = {}
		files = glob.glob(path)
		for name in files: # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
			try:
				with open(name) as f: # No need to specify 'r': this is the default.
					currentData = json.load(f)
					objectDict = {}

					objectDict['description'] = currentData['description'] # A string
					objectDict['keywords'] = currentData['keywords'] # A list

					outputDict[currentData['title']] = objectDict

			except IOError as exc:
				if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
					raise # Propagate other kinds of IOError.

		return outputDict

	def getFields(self, title):
		TEMPLATE_PATH = './templates/'
		TEMPLATE_FILE_EXTENSION = '.json'
		fileName = TEMPLATE_PATH + title + TEMPLATE_FILE_EXTENSION

		try:
			with open(fileName) as f: # No need to specify 'r': this is the default.
				currentData = json.load(f)
				fieldDict = currentData['fields']

		except IOError as exc:
			raise # Failed to open template, does it exist?

		return fieldDict

	def generatePdf(self, title, keys):
		TEMPLATE_PATH = './templates/'
		OUTPUT_PATH = './output/'
		TEMPLATE_FILE_EXTENSION = '.json'
		OUTPUT_FILE_EXTENSION = '.pdf'
		options = {
    		'page-size': 'Letter',
    		'margin-top': '0.75in',
    		'margin-right': '0.75in',
    		'margin-bottom': '0.75in',
    		'margin-left': '0.75in',
    		'encoding': "UTF-8",
    		'quiet': ''
		}
		fileName = TEMPLATE_PATH + title + TEMPLATE_FILE_EXTENSION

		try:
			with open(fileName) as f: # No need to specify 'r': this is the default.
				currentData = json.load(f)

				templateHtml = currentData['html']
				for fieldKey in currentData['fields']:
					templateHtml = templateHtml.replace("{" + fieldKey + "}", keys[fieldKey])

				outputFileName = str(uuid.uuid4()) + OUTPUT_FILE_EXTENSION
				outputFilePath = OUTPUT_PATH + outputFileName
				pdfkit.from_string(templateHtml, outputFilePath, options=options)

		except:
			raise # Failed to open template, does it exist?

		return outputFileName

#if __name__ == "__main__":
#	print "The form engine cannot be run directly. Please run app.py instead."
#	sys.exit()


print form_engine().getTemplates()
print form_engine().getFields("nda")

params = {
    'party1': 'Justin',
    'party2': 'Not Justin',
    'party1-initials': 'JP',
    'party2-initials': 'NJ',
    'date': '05/23/2016'
}

print form_engine().generatePdf('nda', params)