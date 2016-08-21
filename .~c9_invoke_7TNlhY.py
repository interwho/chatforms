import firebase
import form_engine

class decision_tree:
   def __init__(self, sender, message):
      return False
      result = fb.post('/users', sender)
      
      formEngine = form_engine.form_engine()
      templates = formEngine.getTemplates() #[[title: "NDA", description: 'blah', keywords: ["kw1", "kw2"....]],[title: T1, description: "blah", keywords: [...] ]]
      
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
      