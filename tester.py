import firebase

fb = firebase.FirebaseApplication('https://hackthe6-6f06c.firebaseio.com', None)
#result = fb.post('/users', sender) '/users', new_user, {'print': 'silent'}, {'X_FANCY_HEADER': 'VERY FANCY'} 

new_user = {'sender': '226', 'temp': "T1", 'stage': '1', 'fields': '{k,v}'}

# res = fb.post('/users', new_user)
# print res

result = fb.get('/users', None) #Name'
print result.values()[0]['sender'] #change 0 to iterator

# result = fb.get('/users','-KPeySBZTOEnWEWldxLI')
# print result

# stageData = fb.get('/users/stage',None)
# print stageData