from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", page_name = "Inicio", pagestyle = '')

@app.route('/oferta', methods=['GET'])
def oferta():
    return render_template("oferta.html", page_name = "Oferta Educativa", pagestyle = 'normal')

if __name__ == "__main__":
    app.run(debug = True, port=3000)