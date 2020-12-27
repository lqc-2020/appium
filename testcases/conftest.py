import yaml
import pytest

def get_datas():
    with open("./data.yml", 'rb') as f:
        datas = yaml.safe_load(f)
        print(datas)
        return datas