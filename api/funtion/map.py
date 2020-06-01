

def getQueryTodict(query) :
    dict_items = dict()
    if len(query) > 0 :
        query_split = query.split("&")
        for i in query_split :
            query_key = i.split("=")
            dict_items[query_key[0]] = query_key[1]

    return dict_items


def checkKey(dic, key): 
      
    if key in dic: 
        return True
    else: 
        return False