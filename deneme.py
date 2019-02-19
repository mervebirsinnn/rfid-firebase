from firebase import firebase
firebase = firebase.FirebaseApplication('https://rfid-proje.firebaseio.com/', None)
result = firebase.get('/admin','Deniz Ak')
id="13 13 250 42 208"
print(type(result))
print(type(id))
if(id==result):
    print("Deniz" giris yaptı")
    print(result)
else:
    print("esit degil")
    result1=firebase.get('/admin','Eren Yazıcı')
    #if(id==result1)
    print("Eren giris yaptı")
    
