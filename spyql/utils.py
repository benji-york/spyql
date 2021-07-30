import re


def quote_ifstr(s):
    return f"'{s}'" if isinstance(s, str) else s


def make_str_valid_varname(s):
    # remove invalid characters (except spaces in-between)
    s = re.sub(r"[^0-9a-zA-Z_\s]", "", s).strip()

    # remove leading characters that are not letters or underscore
    # s = re.sub(r'^[^a-zA-Z_]+', '', s)

    # if first char is not letter or underscore then add underscore to make it valid
    if not re.match("^[a-zA-Z_]", s):
        s = "_" + s

    # replace spaces by underscores (instead of dropping spaces) for readability
    s = re.sub(r"\s+", "_", s)

    return s
