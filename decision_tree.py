import firebase
import form_engine

class decision_tree:
   
   
   def __init__(self, sender, message):
      self.fb = firebase.FirebaseApplication('https://hackthe6-6f06c.firebaseio.com', None)
      self.result = self.fb.post('/users', sender)
      self.messageResponse='BLAH'
      #res = fb.post({'user_id': 'wilma', 'text': 'Hello'})
      #print res
      self.res = self.fb.get('/users',None)
      self.formEngine = form_engine.form_engine()
      self.templates = self.formEngine.getTemplates()
      
   def __str__(self):
      return self.messageResponse
   
   def Matchlist(self,val):   #This doesn't need to be abstracted
      list=[]
      for i in self.res:
         list.append(i['keywords'])
         
      matchlist=[]
      list2=val.split(" ")
      i=0
      for i in range(0,len(list)):
         if set(list[i]).intersection(list2):
            matchlist.append(self.res[i]['title'])
      self.matchlist=matchlist
   
   def Code(self):
      
      for i in len (self.res.values()):
        stageData= self.res.values()[i]['stage']
      
      if stageData==0:
         outputdata='Hello.How can I help you today ?'
      elif stageData==1:
         if len(self.matchlist)>1:
            outputdata='Which option among these do you want to choose? pick a number'
         else:
            outputdata='Are you sure you want to choose this option?'
      elif stageData==2:
         outputdata='I would like to ask you a few questions. Thanks for the cooperation.  '
         for i in len (self.templates.values()):
            stageData = self.templates.values()[i]['key']
      else: 
         outputdata='Thank you for using the service. '
      result= self.fb.post('/users', outputdata)
      print result
      
decision_tree('226', 'yoyo')      
      
   
      