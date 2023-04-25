import base64
users_info = {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'}


def save_credentials_users(path, users_info):
    lines_tofile = []
    
    for us in users_info:
        l = str(us) + ':' + str(users_info[us])+'\n'
        lines_tofile.append(l.encode())

    with open(path, 'wb') as fh:
        fh.writelines(lines_tofile)

        
save_credentials_users('./user_data.bin', users_info)


def get_credentials_users(path):
    users_list = []
    
    with open(path, 'rb') as fh:
        for l in fh.readlines():
            users_list.append(l.decode().rstrip('\n'))
    
    return users_list

def encode_data_to_base64(data):
    user_list_b64 = []
    for l in data:
        upwd_b64_b = base64.b64encode(l.encode("utf-8"))
        upwd_b64_str = upwd_b64_b.decode("utf-8")
        user_list_b64.append(upwd_b64_str)
    return user_list_b64


encode_data_to_base64(get_credentials_users('./user_data.bin'))
