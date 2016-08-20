from form_engine import forms
from firebase import firebase

firebase = firebase.FirebaseApplication('https://hackthe6-6f06c.firebaseio.com', None)

new_user = 'mad shang'

result = firebase.post('/users', new_user)
print result

res = forms.getTempalte() #[[title: "NDA", description: 'blah', keywords: ["kw1", "kw2"....]],[title: T1, description: "blah", keywords: [...] ]]
list=[]
for i in res:
    list.append(i['keywords'])
print list
val='How do I fill out an a'
def compare(val):
   list2=val.split(" ")
   i=0
   for i in range(0,len(list)):
       if set(list[i]).intersection(list2):
           return res[i]['title']

   
def initfrm( uid, msg ):
   
   
   "This prints a passed string into this function"
   print str
   return



