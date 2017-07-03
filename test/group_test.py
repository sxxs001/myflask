from cmdblib.client import Client


def GetGroup(appid):
    client = Client(host="cmdb.elenet.me", port=80, client_id="2d8dae19c0c44a82a707b507104d0594",
                    secret="isQfGATK9CoIyyzIcZRf0jpgc2MnzksEmiTdTgPLY0Kx2FZdb7Hnc8JjzDLyLdF3gUl5KoxQX98QQu7XMwbOIyEF6FkRSKkTLTmDve1aILbWWvBColx6RsnXUpkCEEDO")
    search_results = client.search_entities_by_query('\"' + appid + '\"', size=1000)
    #print(search_results)
    results = {}
    for i in search_results:
        if str(type(i)) == "<class 'cmdblib.entity.rl_group_hosts'>":
            if i.env == 'prod' and len(i.hosts) != 0:
                results[i.name] = i.hosts
    print(results)


if __name__ == '__main__':
    GetGroup('lpd_team.galaxy_engine')