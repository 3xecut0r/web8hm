import re
import connect
from models import Authors, Quotes


def parser(string: str) -> list:
    if ',' in string:
        string = string.strip().replace(' ', '').split(',')
    return string


def find_match(param):
    quotes = Quotes.objects()
    result = []
    if isinstance(param, list):
        for el in param:
            for quote in quotes:
                author = Authors.objects(fullname=quote.author)
                matches = re.match(el, str(quote.tags)) or re.match(el, str(author.fullname)) or re.match(el, str(quote.quote))
                if matches:
                    result.append(matches)
    else:
        for quote in quotes:
            author = Authors.objects(fullname=quote.author)
            matches = re.match(param, str(quote.tags)) or re.match(param, str(author.fullname)) or re.match(param, str(quote.quote))
            if matches:
                result.append(matches)
    return result

if __name__ == '__main__':
    quotes = Quotes.objects()
    for quote in quotes:
        print(str(quote.author.fullname))
    # while True:
    #     arg = input('-->').strip().split(':')
    #
    #     if arg[0] == 'name':
    #         author = arg[1].strip()
    #         quotes = Quotes.objects(author__fullname=author).all()
    #         for quote in quotes:
    #             print(quote.quote.encode('utf-8'))
    #     elif arg[0] == 'tag':
    #         tag = arg[1].strip()
    #         quotes = Quotes.objects(tags=tag).all()
    #         for quote in quotes:
    #             print(quote.quote.encode('utf-8'))
    #     elif arg[0] == 'tags':
    #         tags = arg[1].strip().split(',')
    #         quotes = Quotes.objects(tags__in=tags).all()
    #         for quote in quotes:
    #             print(quote.quote.encode('utf-8'))
    #     elif arg[0] == 'exit':
    #         break



        # command = arg[0]
        # arg = parser(arg[1].strip())
        # match = find_match(arg)
        # for m in match:
        #     print(m.group().decode('utf-8'))
        #

