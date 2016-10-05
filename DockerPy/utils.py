def tag(a):
    """This function return tags of particular image """
    from urllib.request import urlopen
    import yaml
    t = []
    for i in yaml.load(urlopen("https://registry.hub.docker.com/v2/repositories/library/"+a+"/tags/").read().decode("utf8"))['results']:
        t.append(i['name'])
    t.sort()
    return t