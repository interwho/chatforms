import firebase
import form_engine

class decision_tree:
   def __init__(self, sender, message):
      fb = firebase.FirebaseApplication('https://hackthe6-6f06c.firebaseio.com', None)
      result = fb.post('/users', sender)
      
      formEngine = form_engine.form_engine()
      formEngine.getT
      
   def matchlist(self,val):   
      list=[]
      for i in self.templates:
         list.append(i['keywords'])
         
      matchlist=[]
      list2=val.split(" ")
      i=0
      for i in range(0,len(list)):
         if set(list[i]).intersection(list2):
            matchlist.append(self.templates[i]['title'])
      return matchlist
      
   def __str__(self):
      return 'test message'
      