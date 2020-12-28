import yaml
import pytest

def get_datas():
    with open("./data.yml", 'rb') as f:
        datas = yaml.safe_load(f)
        print(datas)
        return datas

def pytest_collection_modifyitems(session, config, items):
    print(type(items))
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')