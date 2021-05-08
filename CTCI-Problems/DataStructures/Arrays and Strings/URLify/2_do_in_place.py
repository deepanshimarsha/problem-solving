def URLify(str):

    str = str.strip()
    str = str.replace(" ", "%20")
    return str

URLify("Mr John Smith    ")