# Complete the function/method so that it returns the url with anything after the anchor (#) removed.
# Examples
#
# "www.codewars.com#about" --> "www.codewars.com"
# "www.codewars.com?page=1" -->"www.codewars.com?page=1"


def remove_url_anchor(url):
    return url.partition("#")[0]


print(remove_url_anchor("www.codewars.com#about"))


# Best solutions:


def remove_url_anchor(url):
  return url.split('#')[0]


def remove_url_anchor(url):
    index = url.find('#')
    return url[:index] if index >= 0 else url


