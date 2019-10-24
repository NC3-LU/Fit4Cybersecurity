
import json

def get_version(request):
    try:
        with open('VERSION.json', 'r') as json_file:
            data = json.load(json_file)
            version = "{}.{}.{}".format(data['major'], data['minor'],
                                            data['hotfix'])
    except:
        version = "0.0.1"
    return {
        'app_version': version
    }
