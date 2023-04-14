import os, importlib
from .base import Spider

BASE_DIR = os.path.dirname(os.path.abspath(__name__))

MODULES_DIR = os.path.join(BASE_DIR, 'utils','modules')
LIST_MODULES = [x.replace('.py','') for x in os.listdir(MODULES_DIR) if x not in ['__init__.py','__pycache__']]
ALL_MODULES = [importlib.import_module(f'utils.modules.{module}').__dict__.items() for module in LIST_MODULES]

DAY_REPLACEMENT = {
    
    'Senin':'Monday',
    'Selasa':'Tuesday',
    'Rabut':'Wednesday',
    'Kamis':'Thursday',
    'Jum\'at':'Friday',
    'Sabtu':'Saturday',
    'Minggu':'Sunday'
}

def get_scaraper() -> list :
    result = []
    for i in ALL_MODULES:
        for k, v in i:
            if type(v) == type and issubclass(v, Spider) and k != 'Spider':
                result.append(v)
    return result


