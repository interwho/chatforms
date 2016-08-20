#!/usr/bin/env python
import web
import decision_tree

urls = (
    '/incoming', 'handle_message',
)

app = web.application(urls, globals())

class handle_message:
	def GET(self):
		output = 'NOT IMPLEMENTED' # decision_tree.incoming(params)
		return output

if __name__ == "__main__":
	app.run()