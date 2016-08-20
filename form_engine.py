import sys
import pdfkit

class form_engine:
	def getTemplates(self):
		return False #NOT IMPLEMENTED

	def getFields(self, title):
		return False #NOT IMPLEMENTED

	def generatePdf(self, keys):
		options = {
    		'page-size': 'Letter',
    		'margin-top': '0.75in',
    		'margin-right': '0.75in',
    		'margin-bottom': '0.75in',
    		'margin-left': '0.75in',
    		'encoding': "UTF-8",
    		'no-outline': None,
    		'quiet': ''
		}

		#pdfkit.from_string('file open template html', 'randomout.pdf', options=options)

		return False #NOT IMPLEMENTED

if __name__ == "__main__":
	print "The form engine cannot be run directly. Please run app.py instead."
	sys.exit()
