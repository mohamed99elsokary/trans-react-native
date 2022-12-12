__pragma__("skip")


def __pragma__(*s):
    return False


def require(*s):
    return False


def fetch(s):
    return None


class Document:
    def getElementById(self, str_):
        False


document = Document()


class Object:
    @staticmethod
    def assign(*o):
        False

    @staticmethod
    def keys(o):
        False


window = console = module = None
__pragma__("noskip")


def validate(form_keys, form_dict):
    missing = []
    for key in form_keys:
        exist = form_dict.get(key)
        if not exist:
            missing.append(key)
    return missing


def handleChange(values, value, attr):
    values[attr] = value
