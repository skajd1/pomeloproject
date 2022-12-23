import re
def is_url_valid(url):
    REGEX_URL = '[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}([-a-zA-Z0-9@:%_\+.~#?&//=]*)'
    if not re.fullmatch(REGEX_URL, url):
        return False
    return True