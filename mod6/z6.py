def get_recipe(path, search_id):
    ingr = []
    frecept = []
    recepts_key = ["id", "names", "ingredients"]

    with open(path,'r') as fh:
        lines = fh.read().splitlines()
        for l in lines:
            sp = l.split(',')
            #print(l)
            if sp[0] == search_id:
                ingr.append(sp.pop(0))
                ingr.append(sp.pop(0))
                ingr.append(sp)
                return dict(zip(recepts_key, ingr))
        return None 


print(get_recipe('recept.txt', "60b90c3b13067a15887e1ae4"))
