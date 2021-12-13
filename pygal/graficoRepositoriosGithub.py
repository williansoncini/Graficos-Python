import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
response = requests.get(url)
statusCode = requests.status_codes

reponseDict = response.json()
repositoiesDicts = reponseDict['items']

names, stars = [],[]
for repositorieDict in repositoiesDicts:
    names.append(repositorieDict['name'])
    stars.append(repositorieDict['stargazers_count'])

myStyle = LS('#333666', base_style=LCS)

myConfig = pygal.Config()
myConfig.x_label_rotation = 45
myConfig.show_legend = False
myConfig.title_font_size = 24
myConfig.label_font_size = 14
myConfig.major_label_font = 18
myConfig.truncate_label = 15
myConfig.show_y_guides = False
myConfig.width = 1000

chart = pygal.Bar(myConfig, style=myStyle)
# chart = pygal.Bar(style=myStyle, x_label_rotation=45, show_legend=False)
chart.title = 'Most starred Python projects on Github'
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('python_repos.svg')
