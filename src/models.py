from mongoengine import Document
from mongoengine.fields import ListField, StringField, ReferenceField, BooleanField, EmailField


class Authors(Document):
    fullname = StringField(required=True, unique=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quotes(Document):
    tags = ListField(StringField())
    author = ReferenceField(Authors, required=True)
    quote = StringField()


class Contacts(Document):
    fullname = StringField(required=True)
    email = EmailField(required=True)
    address = StringField()
    email_sent = BooleanField(default=False)
