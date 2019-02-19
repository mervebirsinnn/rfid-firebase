from firebase import firebase
firebase = firebase.FirebaseApplication('https://rfid-proje.firebaseio.com/', None)
result = firebase.get('/admin','Merve Birsin')
id="13 13 250 42 208"
print(type(result))
print(type(id))
if(id==result):
    print("Merve giris yaptı")
    print(result)
else:
    print("esit degil")
    result1=firebase.get('/admin','Feride Ünlü')
    #if(id==result1)
    print("Feride giris yaptı")
    {'1': 'John Doe'}
