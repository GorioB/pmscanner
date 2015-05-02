from jinja2 import Environment, FileSystemLoader
import json

def generate_html():
    env = Environment(loader=FileSystemLoader('templates'))

    template = env.get_template("template.html")
    data = []
    with open('..\\..\\output.json','r') as f:
        for line in f:
            data.append(json.loads(line))
    with open('..\\..\\output.html','w') as f:
        text = template.render(data=data)
        f.write(text)
if __name__=="__main__":
    generate_html()