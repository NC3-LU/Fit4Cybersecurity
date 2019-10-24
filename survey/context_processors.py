
import json

def get_version(request):
    with open('VERSION.json', 'r') as json_file:
        data = json.load(json_file)
        version = "{}.{}.{}".format(data['major'], data['minor'],
                                        data['hotfix'])
    return {
        'app_version': version
    }
