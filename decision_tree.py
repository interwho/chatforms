import datetime
import form_engine

class decision_tree:
   def __init__(self, sender, message):
      if "|" in message:
         paramArray = message.split("|")
         
         today = datetime.date.today().strftime("%B %d, %Y")
         
         params = {
            'party1': paramArray[0],
            'party2': paramArray[1],
            'party1-initials': paramArray[2],
            'party2-initials': paramArray[3],
            'date': today
         }

         finalUrl = form_engine.form_engine().generatePdf('nda', params)
         
         self.messageResponse = "Your form can be found at https://hackthe6-prtfw.c9users.io/forms/" + finalUrl
      else:
         self.messageResponse = "Welcome to chatforms! You can fill out an NDA by replying with the following parameters, in the following order: party1|party2|party1-initials|party2-initials"
         
   def __str__(self):
      return self.messageResponse