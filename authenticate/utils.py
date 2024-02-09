import configparser


def get_credentials():
    config = configparser.ConfigParser()
    config.read('credentials.conf')
    api_key = config.get('Credentials', 'api_key')
    cx = config.get('Credentials', 'cx')
    return api_key, cx
