from peewee import  SqliteDatabase
from datetime import datetime
from peewee import  CharField,DateTimeField,UUIDField,Model


db= None
def getConnectionCache():
    global db
    if db is None:
        db = SqliteDatabase('example.db')
        db.connect()
    return db



class User(Model):
    id = UUIDField(primary_key=True)
    name = CharField( null=False)
    createdAt = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    deleted_at = DateTimeField(null=True)
    def soft_delete(self):
        self.deleted_at = datetime.now()
        self.save()

    def update_timestamps(self):
        self.updated_at = datetime.now()
        self.save()
    class Meta:
        database = getConnectionCache()

