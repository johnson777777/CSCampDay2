from flask import Flask, render_template, request, redirect
import html
import os

app = Flask(__name__, template_folder="./", static_folder="./assets") 
data_path = os.path.join(os.path.dirname(__file__), 'data.txt')
open(data_path, 'a+', encoding='utf8')

def display():
    messages_html = ""
    with open(data_path, 'r', encoding='utf8') as f:
        for line in f:
            messages_html += f"<p>{html.escape(line.strip())}</p>"
    return render_template("index.html") + messages_html

@app.route('/') 
def index(): 
    return display()
     
@app.route('/submit', methods = ['POST']) 
def get_data(): 
    name = request.form['name']
    message = request.form['message']
    if request.method == 'POST': 
        with open(data_path, 'a+', encoding='utf8') as f:
            f.write(f'{str(name)}: {str(message)}\n')
    return redirect('/')

     
if __name__ == '__main__': 
    app.run('0.0.0.0', debug = True) 