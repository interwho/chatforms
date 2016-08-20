#!/usr/bin/env python
import web
import form_engine
import decision_tree

urls = (
    '/incoming', 'handleMessage',
    '/forms/(.*)', 'getForm'
)

app = web.application(urls, globals())

class handleMessage:
	def GET(self):
		web.header("Content-Type", "text/xml") # Set the Header

		sender = web.input().From
		message = web.input().Body

		output = """<?xml version="1.0" encoding="UTF-8"?>
					<Response>
						<Message>
							{message}
						</Message>
					</Response>""".format(message=decision_tree.processMessage(sender, message))

		return output

class getForm:
	def GET(self, name):
        if name in os.listdir("output"):  # Security
            web.header("Content-Type", "application/pdf") # Set the Header
            return open('output/%s'%name, "rb").read() # Notice 'rb' for reading images
        
        else:
            raise web.notfound()

if __name__ == "__main__":
	app.run()