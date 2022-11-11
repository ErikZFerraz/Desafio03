from flask import Flask, render_template, request

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config.update(
  TEMPLATES_AUTO_RELOAD = True )

@app.route('/')
@app.route('/index')
def home():
  return render_template('index.html')

@app.route('/contato')
def Contato():
  return render_template('contato.html')

@app.route('/quem-somos')
def Quem_Somos():
  return render_template('quem-somos.html')

if __name__ == "__main__":
    app.run(debug=True)