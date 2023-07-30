from ldap3 import Server, Connection, SIMPLE, SYNC, ASYNC, SUBTREE, ALL

def get_developers_AD():
    AD_SERVER = '0.0.0.0'
    AD_USER = 'kevin.merfi@exmaple.com'
    AD_PASSWORD = 'password'
    AD_SEARCH_TREE = 'dc=exmaple,dc=com'
    server = Server(AD_SERVER)
    conn = Connection(server, user=AD_USER, password=AD_PASSWORD)
    print(conn.bind())

    list_title = ['Должность сотрудника', ]
    list_develop = []
    count = 0
    for i in list_title:
        conn.search(AD_SEARCH_TREE, f'(&(objectCategory=Person)(title={i}))', SUBTREE,
            attributes =['department','sAMAccountName', 'title'])
        for entry in conn.entries:
            list_develop.extend(entry.sAMAccountName)
            list_develop.extend((entry.title))
            count += 1
    print(count, list_develop)
    return list_develop


get_developers_AD()