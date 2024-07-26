import firebase_admin 
from firebase_admin import credentials 
from firebase_admin import db

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
   'databaseURL':"https://faceattendancesystem-32771-default-rtdb.firebaseio.com/"
})



ref = db.reference("Students")

data={
    "AIDS22037":{

       "COURSE":"B-TECH",
       "BRANCH":"CSE DS",
       "BATCH":"2022-2026",
       "NAME":"VISHAL GUPTA",
       "ROLL NO":"AIDS22037",
       "TOTAL ATTENDANCE":10,
       "LAST MARKED":"2024-07-19 09:00:00"

    },

    
    "EC22149":{
       "COURSE":"B-TECH",
       "BRANCH":"ECE",
       "BATCH":"2022-2026",
       "NAME":"TARNEET SINGH",
       "ROLL NO":"EC22149",
       "TOTAL ATTENDANCE":10,
       "LAST MARKED":"2024-07-19 09:00:00"


    },


    "CSAIML22153":{

       "COURSE":"B-TECH",
       "BRANCH":"CSE AIML",
       "BATCH":"2022-2026",
       "NAME":"KUNAL SHARMA",
       "ROLL NO":"CSAIML153",
       "TOTAL ATTENDANCE":10,
       "LAST MARKED":"2024-07-19 09:00:00"

      

    },



}

for key, value in data.items():
    ref.child(key).set(value)

