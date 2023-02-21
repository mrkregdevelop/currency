from jinja2 import Template

template = """
for i in range({{ num }}): print('{{ text }}')
"""

context = {
    "text": "Hello world",
    "num": 10
}

j2_template = Template(template)


with open('examples/example_render.py', 'w') as file:
    file.write(j2_template.render(context))

