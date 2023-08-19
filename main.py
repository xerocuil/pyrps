import os
import base64
import json

from flask import Flask, render_template, request, url_for, flash, redirect
# from flask import render_template
from flask_table import *

from lib.config import Config
import lib.utils as Utils

import engine.dnd5 as dnd5

char_dir = os.path.join(Config.CHARACTERS)
char_file = os.path.join(char_dir, Config.ENGINE + '.json')

# print('char_file: ' + char_file)


# def load_json(file):
#   f = open(file)
#   l = json.load(f)
#   return l




# if os.path.exists(char_file):
#   characters = load_json(char_file)
# else:
#   characters = []


print('dnd5.CHARACTERS')
print(dnd5.CHARACTERS)

# Init Flask App
app = Flask(__name__)
app.config['SECRET_KEY'] = Config.KEY


# Routes

## Home
@app.route('/')
def index():
    return render_template('dnd/characters.html', characters=dnd5.CHARACTERS)



# ## DND: Add char
# @app.route('/dnd/add/char', methods=('GET', 'POST'))
# def dnd_add_char():
#   if request.method == 'POST':
#     name = request.form['name']
#     level = request.form['level']
#     char_class = request.form['char_class']
#     strength = request.form['strength']
#     dexterity = request.form['dexterity']
#     constitution = request.form['constitution']
    
#     msg = []
#     data = {
#       "name": name,
#       "level": level,
#       "char_class": char_class,
#       "strength": strength,
#       "dexterity": dexterity,
#       "constitution": constitution,
#     }
#     msg = [data]

#     print(msg)

#     if not name:
#       flash('Name is required!')
#     elif not level:
#       flash('Level is required!')
#     else:
#       msg.append(data)

#       if not os.path.exists(char_file):
#         os.makedirs(char_dir)
#         with open(char_file, "w") as outfile:
#           json.dump(msg, outfile, indent=2)
#       else:
#         # characters = load_json(char_file)
#         characters.append(data)
#         with open(char_file, 'w') as outfile:
#           json.dump(characters, outfile, indent=2)


#       return redirect(url_for('index'))

#   return render_template('test2.html', characters=characters)



# ## DND: Characters
# @app.route('/dnd/characters')
# def characters():
#   return  render_template('dnd/characters.html', players=players, profileUrl=profileUrl)

# ## DND: Char. classes
# @app.route('/classes')
# def charClasses():
#   return  render_template('dnd/classes.html')

# ## DND: Char. sheet
# @app.route('/dnd/csheet/<char_id>', methods=['GET', 'POST'])
# def charSheet(char_id):
#   character = {}
#   for c in players:
#     if c['id'] == char_id:
#       character = c
#       print(type(character))
#   return  render_template('dnd/csheet.html', character=character)







# Run App
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8088, debug=True)