# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%
import 


# %%
get_ipython().system('pip install beautifulsoup4')


# %%
from bs4 import BeautifulSoup as bs


# %%
import requests


# %%
res = requests.get('https://careers.colesgroup.com.au/job/Hawthorn-East-Melbourne-Infrastructure-Project-Manager-VIC-3123/580400210/')


# %%
res


# %%
res.body


# %%
res.data


# %%
res.content


# %%
type(res.content)


# %%
res.raw


# %%
str(res.raw)


# %%
res.raw.headers


# %%
res.headers


# %%
bs(res.content)


# %%
soup = bs(res.content)


# %%
soup.find('h2')


# %%
soup.find('h2').text


# %%
soup.find('h2').innerhtml


# %%
soup.find('h2').inner


# %%
soup.find('h2').p


# %%
soup.find('h2').span


# %%
soup.find_all('h2').span


# %%
soup.find_all('h2')


# %%
soup.find_all(string=re.compile('Good things start here
'))


# %%
soup.find_all(string=re.compile('Good things start here'))


# %%
import re


# %%
soup.find_all(string=re.compile('Good things start here'))


# %%
soup.find_all('span', string=re.compile('Good things start here'))


# %%
soup.find_all(string=re.compile('Good things start here'))


# %%
soup.find_all('span', string=re.compile('Good things start here'))


# %%
soup.find_all('span', style='font-family:Verdana, Geneva, sans-serif')


# %%
spans = soup.find_all('span', style='font-family:Verdana, Geneva, sans-serif')


# %%
spans[0]


# %%
spans[0].string


# %%
spans[3].string


# %%
spans[2].string


# %%
spans[2].text


# %%
spans[3].text


# %%
spans[3].string


# %%
spans[3]


# %%
spans[3].children


# %%
spans[3].child


# %%
spans[3].children[0]


# %%
next(spans[3].children)


# %%
next(next(spans[3].children))


# %%
next(spans[3].children)


# %%
it = spans[3].children


# %%
next(it)


# %%
next(it)


# %%
next(it)


# %%
it = spans[3].descendants


# %%
next(it)


# %%
next(it)


# %%
next(it)


# %%
it = spans[3].descendants


# %%
next(it)


# %%
next(it)


# %%
next(it).string


# %%
it = spans[3].descendants


# %%
next(it)


# %%
next(it).string


# %%
it = spans[3].descendants


# %%
next(it).string


# %%
next(it).string


# %%
next(it).string


# %%
next(it).string


# %%
next(it).string


# %%
it = spans[3].descendants


# %%
s = next(it)


# %%
s


# %%
s.string


# %%
spans[0]


# %%
spans[0].string


# %%
spans[0].contents


# %%
spans[0]


# %%
spans[0].text


# %%
spans[0].contents[0].text


# %%
spans[0].contents[0].string


# %%
soup.find_all('span', style='font-family:Verdana, Geneva, sans-serif', string=re.compile('Good things start here'))


# %%
span = soup.find_all('span', style='font-family:Verdana, Geneva, sans-serif', string=re.compile('Good things start here'))[0]


# %%
span.next_sibling


# %%
span.find_next_sibling(style='font-family:Verdana, Geneva, sans-serif')


# %%
span.parent.parent.find_next_sibling(style='font-family:Verdana, Geneva, sans-serif')


# %%
span.parent.parent.parent.find_next_sibling(style='font-family:Verdana, Geneva, sans-serif')


# %%
span.find_next(style='font-family:Verdana, Geneva, sans-serif')


# %%
soup.find_all('span', has_strong_child)


# %%
span


# %%
span.find('lo')


# %%
assert span.find('lo')


# %%
assert span.find('strong')


# %%
def has_strong_child(elem):
    return bool(elem.find('strong'))


# %%
bool(span.find('lo'))


# %%
bool(span.find('string'))


# %%
bool(span.find('strong'))


# %%
soup.find_all('span', has_strong_child)


# %%
soup.find_all(has_strong_child)


# %%
soup.find_all(name='span', has_strong_child)


# %%
soup.find_all(has_strong_child, name='span')


# %%
def has_strong_child(elem):
    return elem.name == 'span' and bool(elem.find('strong'))


# %%
soup.find_all(has_strong_child)


# %%
for e in soup.find_all(has_strong_child):
    print (e.text)


# %%
for e in soup.find_all(has_strong_child):
    print (e.text)


# %%
def has_strong_child(elem):
    return elem.name == 'span' and bool(elem.find('strong'))


# %%
has_strong_child(span)


# %%
spans


# %%
spans[0]


# %%
spans[1]


# %%
has_strong_child(spans[1])


# %%
soup.find_all(has_strong_child)


# %%
soup.find_all(has_strong_child)[0]


# %%
soup.find_all(has_strong_child)[1]


# %%
soup.find_all(has_strong_child)[1]


# %%
soup.find_all(has_strong_child)[10]


# %%
soup.find_all(has_strong_child, name='span')[0].text


# %%
soup.find_all(has_strong_child)[0].text


# %%
soup.name


# %%
soup.contents[0].name


# %%
soup.contents[1].name


# %%
soup.contents[1].name == 'span'


# %%
def has_strong_child(elem):
    return elem.name == 'span' and bool(elem.find('strong'))


# %%
soup.find_all(has_strong_child)


# %%
soup.find_all(has_strong_child)[0]


# %%
soup.find_all(has_strong_child)[1]


# %%
soup.find_all(has_strong_child)[2]


# %%
soup.find_all(has_strong_child)[2].find_next(has_strong_child)


# %%
soup.find_all(has_strong_child)[2].find_next(has_strong_child).find_next


# %%
soup.find_all(has_strong_child)[2].find_next(has_strong_child).find_next(has_strong_child)


# %%
def has_strong_child(elem):
    return elem.name == 'span' and bool(elem.find('strong')) and not bool(elem.find('span'))


# %%
soup.find_all(has_strong_child)[0]


# %%
soup.find_all(has_strong_child)[0].find_next(has_strong_child)


# %%
soup.find_all(has_strong_child)[0].find_next(has_strong_child)


