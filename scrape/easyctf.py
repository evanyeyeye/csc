from lxml import html
import json
import requests

data = {
    'login-username': '',
    'login-password': '',
}

s = requests.session()

# Login
page = s.get('https://www.easyctf.com/users/login')
tree = html.fromstring(page.content)
data['login-csrf_token'] = tree.xpath('//*[@id="login-csrf_token"]')[0].get('value')
s.post('https://www.easyctf.com/users/login', data)

# Scrape info
team_data = []
page = s.get('https://www.easyctf.com/scoreboard')
tree = html.fromstring(page.content)
table = tree.xpath('//table[@class="table table-hover"]/tbody/tr')
for row in table:
    school = row[2].text
    if school and school.lower() in {"tjhsst", "thomas jefferson high school for science and technology"}:
        team_data.append([int(row[0][1].text), row[1][0].text, int(row[3].text)])

print(json.dumps(team_data))