from models import Authors, Quotes
from pymongo import MongoClient
from connect import mongo_user, mongodb_pass, domain
import json


client = MongoClient(f'mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/?retryWrites=true&w=majority')
db = client['test']

with open('authors.json') as f:
    authors_data = json.load(f)
    db.authors.insert_many(authors_data)

with open('quotes.json') as f:
    quotes_data = json.load(f)
    db.quotes.insert_many(quotes_data)


# for author_data in authors_data:
#     author = Authors(**author_data)
#     author.save()
#
# for quote_data in quotes_data:
#     quote = Quotes(**quote_data)
#     quote.save()










# tag = Tag(name='Purchases')
#
# record1 = Record(description='Buying sausage')
# record2 = Record(description='Buying milk')
# record3 = Record(description='Buying oil')
#
# Notes(name='Shopping', records=[record1, record2, record3], tags=[tag, ]).save()
#
# Notes(name='Going to the movies', records=[Record(description='Went to see the Avengers'), ], tags=[Tag(name='Fun'), ]).save()
#
