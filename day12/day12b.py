Mid-Morning Session

### How to connect a Flask App to a MongoDB database

## Let's get copies of the community board app we saw this morning
git clone https://github.com/upperlinecode/stock-query-mongodb.git

## To connect your database,
from flask_pymongo import PyMongo

MONGO_DBNAME = ''
MONGO_DB_USERNAME = ''
MONGO_DB_PASSWORD = ''

app.config['MONGO_DBNAME'] = MONGO_DBNAME
app.config['MONGO_URI'] = f'mongodb+srv://{MONGO_DB_USERNAME}:{MONGO_DB_PASSWORD}@cluster0-kxrbn.mongodb.net/{MONGO_DBNAME}?retryWrites=true'

mongo = PyMongo(app)




### Now we want to add new documents to our database
events_db = mongo.db.events
event = {
'name':'',
'date':''
}
events_db.insert(event)
