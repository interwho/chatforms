import firebase
import form_engine

class decision_tree:
   
   
   def __init__(self, sender, message):
      self.fb = firebase.FirebaseApplication('https://hackthe6-6f06c.firebaseio.com', None)
      self.result = self.fb.post('/users', sender)
      self.messageResponse='BLAH'
      #res = fb.post({'user_id': 'wilma', 'text': 'Hello'})
      #print res
      self.sender=sender
      self.message=message
      self.res = self.fb.get('/users',None)
      self.formEngine = form_engine.form_engine()
      self.templates = self.formEngine.getTemplates()
      
   def __str__(self):
      return self.messageResponse
   
   def Matchlist(self,val):   #This doesn't need to be abstracted
      list=[]
      for i in self.templates:
         list.append(i['keywords'])
         
      matchlist=[]
      list2=val.split(" ")
      i=0
      for i in range(0,len(list)):
         if set(list[i]).intersection(list2):
            matchlist.append(self.templates[i]['title'])
      self.matchlist=matchlist
      
   #### This function maps the phone number to the unique id    
   #def map(self):   
   
   #### This function would search the user based on the userid and return the rest of the data
   def searchUser(self):
      result = fb.get('/users', None)
      for i in self.res.values():
         if self.sender in  self.res.values()[i]['sender']:
            return self.res.values()[i]
         else:
            return None   
   def Code(self):
      if self.searchUser() != None: 
         stageData= (self.searchUser())['stage']
         print "statge" +stageData
      
      if stageData==0:
         outputdata='Hello. How can I help you today ?'
         stageData=1
         #call method with above qs
         #got a call back with unique id and the message i.e. "i want a nda"
         
         self.Matchlist(self.message)
      elif stageData==1:
         if len(self.matchlist)>1:
            outputdata='Which option among these do you want to choose? pick a number'
         else:
            outputdata='Are you sure you want to choose this option?'
      elif stageData==2:
         outputdata='I would like to ask you a few questions. Thanks for the cooperation.  '
         for i in len (self.res.values()):
            keyData = self.res.values()[i]['key']
      else: 
         outputdata='Thank you for using the service. '
      result= self.fb.post('/users', outputdata)
      if self.searchUser !=None:
         result=self.fb.put('/users/%s'%self.searchUser(),stageData)
      
      print result
      
decision_tree('226', 'message message2 message3')      
      