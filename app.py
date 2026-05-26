import os
from flask import Flask, render_template, abort
# will import youur scripts and shi
from scripts_storage import LUA_SCRIPTS

app = Flask(__name__)

# list that damn script
SCRIPTS_DATA = {
    "forsaken": {
        "title": "Forsaken script",
        "desc": "idk about this one"
    },
    "bitebynight": {
        "title": "Bite by night script [BETA]",
        "desc": "idk about this too"
    },
    "slapbattles": {
        "title": "Slap Battles script",
        "desc": "now we're talking (I forgot this one, but very op ngl)"
    },
    "monkeybomb": {
        "title": "Monkey Bomb Tag script",
        "desc": "idk about this one"
    }
}

@app.route('/')
def home():
    # will render that front-end, so yeah
    return render_template('index.html', scripts=SCRIPTS_DATA)

@app.route('/script/<script_id>')
def view_script(script_id):
    # dynamic shi that'll act as engine
    if script_id not in SCRIPTS_DATA:
        abort(404)
        
    script_info = SCRIPTS_DATA[script_id]
    
    # python pulls the code out of your ass
    if script_id in LUA_SCRIPTS:
        code_content = LUA_SCRIPTS[script_id]
    else:
        code_content = f"-- Error: Code for '{script_id}' was not found in scripts_storage.py"

    return render_template('notebook.html', title=script_info["title"], code=code_content)

if __name__ == '__main__':
    # will start the local Python web application server
    app.run(debug=True, port=5000)