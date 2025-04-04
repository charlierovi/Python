from flask import Flask, render_template
import markdown

app = Flask(__name__)


@app.route('/')
def index():
    with open("mi_archivo.md", "r", encoding="utf-8") as f:  # Obre el fitxer md
        markdown_content = f.read()
        html_content = markdown.markdown(markdown_content)  # El converteix a html
    return render_template('index.html', content=html_content)


if __name__ == '__main__':
    app.run(debug=True)
