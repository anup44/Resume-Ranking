from bs4 import BeautifulSoup as bs
import requests
import xlwt
import re
import pandas as pd

book = xlwt.Workbook()
sheet = book.add_sheet('data')

headers_map = {
    'Coles Supermarkets': None, 
    'Coles Liquor': None, 
    'Coles Liquor\xa0Concord': None, 
    'Coles Liquor\xa0Bendigo': None, 
    'Good things start here': 'Good things start here', 
    'About the role': 'About the role', 
    'About Us': 'About the role', 
    'What youll be doing': 'What youll be doing', 
    'Good things youll need': 'Good things youll need', 
    'Good things you need': 'Good things youll need', 
    'What youll need': 'Good things youll need', 
    'Youll also need': 'Good things youll need', 
    'Why Coles': 'Why Coles', 
    'For everyone who shares our passion': 'For everyone who shares our passion', 
    'Wed love to meet you': 'Wed love to meet you', 
    'Wed love to hear from you': 'Wed love to meet you'
    }

url = 'https://careers.colesgroup.com.au/job/Hawthorn-East-Senior-AX-D365-Developer-Consultant-VIC-3123/572996810/'
res = requests.get(url)

jd_data = {}
def has_strong_child(elem):
    # return elem.name == 'span' and bool(elem.find('strong', recursive=False)) and not bool(elem.find('span', recursive=False)) and elem.strong.string.strip()
    # print (elem.text)
    return elem.name == 'span' and bool(elem.find('strong', recursive=False)) and re.sub(r'[^\w\s]', '', elem.strong.text.strip()) and (elem.text.strip() == elem.strong.text.strip() or (elem.strong.next_sibling and elem.strong.next_sibling.name == 'br'))
    # elem.strong.string.strip()

def get_strong_child_with_text(text):
    def get_child(elem):
        # print (text)
        # print (elem.string)
        # return elem.name == 'span' and bool(elem.find('strong')) and not bool(elem.find('span', recursive=False)) and re.compile(text).search(re.sub(r'[^\w\s]', '', elem.strong.string))
        return elem.name == 'span' and bool(elem.find('strong', recursive=False)) and re.compile(text).search(re.sub(r'[^\w\s]', '', elem.strong.text))
    return get_child

def compare_style(stl):
    return stl and re.sub(r'[\s]', '', stl) == 'font-family:Verdana,Geneva,sans-serif'
    # return stl and re.compile('^(font-family:).*(Verdana|sans-serif).*(Verdana|sans-serif)').search(re.sub(r'[\s]', '', stl))
soup = bs(res.content)

job_title = soup.find('h1').span.string.strip()
jd_data['Title'] = job_title

print ([re.sub(r'[^\w\s]', '', x.strong.text.strip()) for x in soup.find_all(has_strong_child)])
keys = [re.sub(r'[^\w\s]', '', x.strong.text.strip()) for x in soup.find_all(has_strong_child)]

for k in keys:
    print ('***********')
    print (k)
    header = headers_map[k]
    if not header:
        continue
    txt = ''''''
    span = soup.find(get_strong_child_with_text(k))
    txt = txt + ' '.join(span.find_all(text=True, recursive=False))
    span_children = span.strong.find_next_siblings('span')
    txt = txt + '\n' + ' '.join([' '.join(x.find_all(text=True)) for x in span_children])
    # print (span)
    span = span.find_next('span', style=compare_style)
    # print (span)
    while (span and not has_strong_child(span)):
        txt = txt + '\n' + ' '.join(span.find_all(text=True, recursive=False))
        span = span.find_next('span', style=compare_style)
        # print ('******************************')
        # print (span)
    txt = txt.strip()
    print (txt)
    if header in jd_data:
        jd_data[header] = jd_data[header] + ' ' + txt
    else:
        jd_data[header] = txt

jd_data['URL'] = url

print (jd_data)
print (jd_data.keys())
try:
    df = pd.read_pickle('data2.pkl')
    print (df)
except:
    df = pd.DataFrame([], columns=jd_data.keys())
    print ('lololoo')
df = df.append(jd_data, ignore_index=True)
print (df)
df.to_excel('data2.xlsx', index=False)
df.to_pickle('data2.pkl')