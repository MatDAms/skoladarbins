from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/user')
def world():
   return 'sveiki, user'

@app.route('/admin')
def hello():
   return 'sveiki, admin'
@app.errorhandler(404)
def eror():
   return 'lapa nav eksisteta'

@app.route('/user/<name>')
def sup(name):
   return 'Sveiki   ' + str(name) + '!'

if __name__ == '__main__':
   app.run()