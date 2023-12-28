# Write a function that when given a URL as a string, parses out just the
# domain name and returns it as a string. For example:
#
# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

from urllib.parse import urlparse


def domain_name(url):
    return url.split("www.")[-1].split("//")[-1].split(".")[0]


url = "http://www.zombie-bites.com"
print(domain_name(url))

# Best solutions:


import re
def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')


def domain_name(url):
    url = url.replace('www.', '')
    url = url.replace('https://', '')
    url = url.replace('http://', '')

    return url[0:url.find('.')]


import re
def domain_name(url):
    return re.search("(//|www.)(\w+)[.]", url).group(2)