def get_cats_info(path):
    dict_cats = []
    dict_cats_keys = ["id", "name", "age"]

    with open(path, 'r') as fh:
        lines = fh.read().splitlines()
        print(lines)
        for i in lines:
            r1 = dict(zip(dict_cats_keys, i.split(',')))
            dict_cats.append(r1)

        return dict_cats


print(get_cats_info('cats_info.txt'))
