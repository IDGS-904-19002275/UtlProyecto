from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", page_name = "Inicio", pagestyle = '')

@app.route('/oferta', methods=['GET'])
def oferta():
    return render_template("oferta.html", page_name = "Oferta Educativa", pagestyle = 'normal')

@app.route('/aulavirtual', methods=['GET'])
def aulavirtual():
    return render_template("aulavirtual.html", page_name = "Aula Virtual", pagestyle = 'normal')

@app.route('/carreras/<carrera>', methods=['GET'])
def ofertacarrera(carrera):
    tarjetas = [
        {
            'titulo': 'TSU EN TI ÁREA ENTORNOS VIRTUALES Y NEGOCIOS DIGITALES',
            'imagen': 'https://www.aulaplaneta.com/sites/default/files/styles/article_detail/public/articles/images/shutterstock_153636422.jpeg?itok=4xtGz6FH'
        },
        {
            'titulo': 'TSU EN TI ÁREA DESARROLLO DE SOFTWARE MULTIPLATAFORMA',
            'imagen': 'https://www.becas-santander.com/content/dam/becasmicrosites/blog/metodolog%C3%ADas-de-desarrollo-de-software.jpg'
        },
        {
            'titulo': 'TSU EN TI ÁREA INFRAESTRUCTURA DE REDES DIGITALES',
            'imagen': 'https://tecnologiasuth.com/wp-content/uploads/2020/02/slider-beside-area-TI-RD-2.jpg'
        }
    ]

    tarjetas2 = [
        {
            'titulo': 'INGENIERÍA EN ENTORNOS VIRTUALES Y NEGOCIOS DIGITALES',
            'imagen': 'https://www.aulaplaneta.com/sites/default/files/styles/article_detail/public/articles/images/shutterstock_153636422.jpeg?itok=4xtGz6FH'
        },
        {
            'titulo': 'INGENIERÍA EN DESARROLLO Y GESTIÓN DE SOFTWARE',
            'imagen': 'https://www.becas-santander.com/content/dam/becasmicrosites/blog/metodolog%C3%ADas-de-desarrollo-de-software.jpg'
        },
        {
            'titulo': 'INGENIERÍA EN REDES INTELIGENTES Y CIBERSEGURIDAD 2',
            'imagen': 'https://tecnologiasuth.com/wp-content/uploads/2020/02/slider-beside-area-TI-RD-2.jpg'
        }
    ]

    tarj = []

    if carrera == 'tsu':
        tarj = tarjetas
    else:
        tarj = tarjetas2

    return render_template("carreras.html", page_name = "Carreras " + carrera, pagestyle = 'normal', carreras = carrera, tarjetas = tarj)

@app.route('/centroinfo', methods=['GET'])
def centroinfo():
    return render_template("centroinfo.html", page_name = "Centro de Informacion", pagestyle = 'normal')

@app.route('/centromedico', methods=['GET'])
def centromedico():
    return render_template("centromedico.html", page_name = "Centro Medico", pagestyle = 'normal')

@app.route('/becas', methods=['GET'])
def becas():
    return render_template("becas.html", page_name = "Becas y ayudas", pagestyle = 'normal')

if __name__ == "__main__":
    app.run(debug = True, port=3000)