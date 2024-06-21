from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
import pymysql
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'incubadoradei'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin@localhost/incubadora'
app.config['MAIL_SERVER'] = 'smtp.techtalentusm.cl'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'postulaciones@techtalentusm.cl'
app.config['MAIL_PASSWORD'] = 'JT6paGp53Yb9865KUe7w'

mail = Mail(app)
db = SQLAlchemy(app)

class Postulacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apellidoPaterno = db.Column(db.String(100))
    apellidoMaterno = db.Column(db.String(100))
    rut = db.Column(db.String(12))
    edad = db.Column(db.Integer)
    genero = db.Column(db.String(10))
    email = db.Column(db.String(100))
    curso = db.Column(db.String(20))
    institucion = db.Column(db.String(100))
    tipoColegio = db.Column(db.String(50))
    ciudad = db.Column(db.String(50))
    comuna = db.Column(db.String(50))
    # Campos adicionales para la segunda parte
    postulacion = db.Column(db.String(20), nullable=True)
    nombre1 = db.Column(db.String(100), nullable=True)
    apellidoPaterno1 = db.Column(db.String(100), nullable=True)
    apellidoMaterno1 = db.Column(db.String(100), nullable=True)
    nombre2 = db.Column(db.String(100), nullable=True)
    apellidoPaterno2 = db.Column(db.String(100), nullable=True)
    apellidoMaterno2 = db.Column(db.String(100), nullable=True)
    profesor = db.Column(db.String(10), nullable=True)
    nombreProfesor = db.Column(db.String(100), nullable=True)
    apellidoPaternoProfesor = db.Column(db.String(100), nullable=True)
    apellidoMaternoProfesor = db.Column(db.String(100), nullable=True)
    robotica = db.Column(db.Integer, nullable=True)
    prototipado = db.Column(db.Integer, nullable=True)
    aplicacionesMoviles = db.Column(db.Integer, nullable=True)
    creatividadEmprendimientoInnovacion = db.Column(db.Integer, nullable=True)
    telecomunicaciones = db.Column(db.Integer, nullable=True)
    extracurricular = db.Column(db.String(10), nullable=True)
    extracurricularTalleres = db.Column(db.String(255), nullable=True)
    extracurricularOtro = db.Column(db.String(255), nullable=True)
    problemaDefinido = db.Column(db.String(10), nullable=True)
    descripcionProblema = db.Column(db.Text, nullable=True)
    afectados = db.Column(db.Text, nullable=True)
    solucion = db.Column(db.Text, nullable=True)
    desafioDesarrolloSostenible = db.Column(db.Text, nullable=True)
    token = db.Column(db.String(36), unique=True, nullable=False, default=str(uuid.uuid4()))

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formulario1', methods=['GET', 'POST'])
def formulario1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidoPaterno = request.form['apellidoPaterno']
        apellidoMaterno = request.form['apellidoMaterno']
        rut = request.form['rut']
        edad = request.form['edad']
        genero = request.form['genero']
        email = request.form['email']
        curso = request.form['curso']
        institucion = request.form['institucion']
        tipoColegio = request.form['tipoColegio']
        ciudad = request.form['ciudad']
        comuna = request.form['comuna']
        
        postulacion = Postulacion(
            nombre=nombre,
            apellidoPaterno=apellidoPaterno,
            apellidoMaterno=apellidoMaterno,
            rut=rut,
            edad=edad,
            genero=genero,
            email=email,
            curso=curso,
            institucion=institucion,
            tipoColegio=tipoColegio,
            ciudad=ciudad,
            comuna=comuna
        )
        db.session.add(postulacion)
        db.session.commit()

        # Personalizar el saludo según el género
        if genero.lower() == 'masculino':
            saludo = 'Estimado'
        elif genero.lower() == 'femenino':
            saludo = 'Estimada'
        else:
            saludo = 'Estimado/a'

        # Asunto personalizado
        asunto = f'{nombre} Completa la segunda parte del formulario'

        # Enviar correo con la segunda parte del formulario
        msg = Message(asunto, 
                      sender='postulaciones@techtalentusm.cl', 
                      recipients=[email])
        msg.body = f"""
        {saludo} {nombre} {apellidoPaterno} {apellidoMaterno},

        Por favor, completa la segunda parte del formulario accediendo al siguiente enlace:
        {url_for('formulario2', token=postulacion.token, _external=True)}
        """
        mail.send(msg)
        return '', 200  # Responder con éxito para la solicitud AJAX

    return render_template('formulario1.html')


@app.route('/formulario2/<token>', methods=['GET', 'POST'])
def formulario2(token):
    postulacion = Postulacion.query.filter_by(token=token).first_or_404()
    if request.method == 'POST':
        print(request.form)
        postulacion.postulacion = request.form['postulacion']
        postulacion.nombre1 = request.form.get('nombre1')
        postulacion.apellidoPaterno1 = request.form.get('apellidoPaterno1')
        postulacion.apellidoMaterno1 = request.form.get('apellidoMaterno1')
        postulacion.nombre2 = request.form.get('nombre2')
        postulacion.apellidoPaterno2 = request.form.get('apellidoPaterno2')
        postulacion.apellidoMaterno2 = request.form.get('apellidoMaterno2')
        postulacion.profesor = request.form['profesor']
        postulacion.nombreProfesor = request.form.get('nombreProfesor')
        postulacion.apellidoPaternoProfesor = request.form.get('apellidoPaternoProfesor')
        postulacion.apellidoMaternoProfesor = request.form.get('apellidoMaternoProfesor')
        postulacion.robotica = request.form['robotica']
        postulacion.prototipado = request.form['prototipado']
        postulacion.aplicacionesMoviles = request.form['aplicacionesMoviles']
        postulacion.creatividadEmprendimientoInnovacion = request.form['creatividadEmprendimientoInnovacion']
        postulacion.telecomunicaciones = request.form['telecomunicaciones']
        postulacion.extracurricular = request.form['extracurricular']
        
        # Manejar los talleres seleccionados
        talleres = request.form.getlist('talleres[]')
        postulacion.extracurricularTalleres = ','.join(talleres)
        
        postulacion.extracurricularOtro = request.form.get('extracurricularOtro')
        postulacion.problemaDefinido = request.form['problemaDefinido']
        postulacion.descripcionProblema = request.form.get('descripcionProblema')
        postulacion.afectados = request.form.get('afectados')
        postulacion.solucion = request.form.get('solucion')
        postulacion.desafioDesarrolloSostenible = request.form.get('desafioDesarrolloSostenible')

        db.session.commit()
        flash('Se ha completado la segunda parte del formulario.', 'success')
        return redirect(url_for('confirmacion', token=postulacion.token))
    return render_template('formulario2.html', postulacion=postulacion)

@app.route('/confirmacion/<token>', methods=['GET', 'POST'])
def confirmacion(token):
    postulacion = Postulacion.query.filter_by(token=token).first_or_404()
    if request.method == 'POST':
        # Expirar el token
        postulacion.token = None
        db.session.commit()
        flash('Tu postulación ha sido completada y el token ha expirado.', 'success')
        return redirect('https://techtalentusm.cl/')
    return render_template('confirmacion.html', postulacion=postulacion)


@app.errorhandler(403)
@app.errorhandler(404)
@app.errorhandler(500)
def handle_error(error):
    return render_template('error.html'), error.code
if __name__ == '__main__':
    app.run(debug=True)
