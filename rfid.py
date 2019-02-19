from firebase import firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("./rfid-proje-firebase-adminsdk-za8ng-14ce04a301.json")
firebase_admin.initialize_app(cred , {
    'databaseURL': 'https://rfid-proje.firebaseio.com/'
})

                              
#db = firestore.client()
ref = db.reference('/admin')

print(ref.get())

#firebase= firebase.FirebaseApplication('https://rfid-proje.firebaseio.com/')
#resultput = firebase.put('kimlik', 'buket bingöl', 6)
#result = firebase.get('/kimlik',None)
#print(result)
