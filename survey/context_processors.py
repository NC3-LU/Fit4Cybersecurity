
import os
import json
from csskp.settings import BASE_DIR

def get_version(request):
    try:
        with open(os.path.join(BASE_DIR,'VERSION.json'), 'r') as json_file:
            data = json.load(json_file)
            version = "{}.{}.{}".format(data['major'], data['minor'],
                                            data['hotfix'])
    except:
        version = "0.0.0"
    return {
        'app_version': version
    }
