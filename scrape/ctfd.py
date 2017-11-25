from lxml import html
import json
import requests

valid_teams = []
for counter in range(1, 13):
    page = requests.get('https://hsf.csaw.io/teams/{}'.format(counter))
    tree = html.fromstring(page.content)
    table = tree.xpath('//table[@id="teamsboard"]/tbody/tr')
    for row in table:
        for team in row.xpath('./td[3]/span/text()'):
            if team.lower() in {"tjhsst", "thomas jefferson high school for science and technology"}:
                valid_teams.append(row.xpath('./td[1]/a/@href')[0])

team_data = []
for team in valid_teams:
    page = requests.get('https://hsf.csaw.io{}'.format(team))    
    if ">place<" not in page.text:        
        continue
    tree = html.fromstring(page.content)    
    team_list = []
    team_list.append(int(tree.xpath('//*[@id="team-place"]/text()')[0].strip()[:-2]))
    team_list.append(tree.xpath('//*[@id="team-id"]/text()')[0])
    team_list.append(int(tree.xpath('//*[@id="team-score"]/text()')[0].strip()))    
    team_data.append(team_list)

print(json.dumps(team_data))