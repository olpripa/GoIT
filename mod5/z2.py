articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]
def find_articles(key, letter_case=False):
    result = []
    for st in articles_dict:
        title = st['title']
        author = st['author']
        if not letter_case:
            title = title.lower()
            author = author.lower()
            key = key.lower()
        if key in title or key in author:
            result.append(st)
    
    return result

#print(find_articles('Ocean'))
print(find_articles('Ocean',letter_case=True))
