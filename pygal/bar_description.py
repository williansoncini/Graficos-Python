import pygal
from pygal import style
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

myStyle = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=myStyle, x_label_rotation=45, show_legend=False)

chart.title = 'Python projects'
chart.x_labels = ['httpie', 'django', 'flask']

plotDicts = [
    {'value':16101, 'label': 'Httpie'},
    {'value':15028, 'label': 'Django'},
    {'value':18547, 'label': 'Flask'}
]

chart.add('', plotDicts)
chart.render_to_file('barDescription.svg')