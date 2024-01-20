from flask import Flask, render_template, request

app = Flask(__name__)

usuarios = {
    "juan": "admin",
    "pepe": "user"
}



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])

        precio_tarro = 9000
        total_sin_descuento = tarros * precio_tarro

        descuento = 0

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        total_con_descuento = total_sin_descuento * (1 - descuento)
        descuento_total=total_sin_descuento*(descuento)

        return render_template('Ejercicio1.html',
                               nombre=nombre,
                               total_sin_descuento=total_sin_descuento,
                               descuento_total=descuento_total,
                               total_con_descuento=total_con_descuento)

    return render_template('Ejercicio1.html')

@app.route('/Ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = ""

    if request.method == 'POST':
        nombre = request.form['nombre']
        contraseña = request.form['contraseña']

        if nombre.lower() in usuarios and contraseña == usuarios[nombre.lower()]:
            if nombre.lower() == "juan" and contraseña.lower() == "admin":
                mensaje = "Bienvenido administrador Juan"
            elif nombre.lower() == "pepe" and contraseña.lower() == "user":
                mensaje = "Bienvenido usuario Pepe"
        else:
            mensaje = "Usuario o contraseña incorrectos"

        return render_template('Ejercicio2.html', mensaje=mensaje)
    return render_template('Ejercicio2.html')


if __name__ == '__main__':
    app.run()
