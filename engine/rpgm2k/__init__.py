import os
import json
import subprocess
import xmltodict

from flask import Blueprint, render_template




# Functions

# ## Import rpgm2k game data
# def import_game(game_dir):
    
#     RPGM2_DB = os.path.join(RPGM2_DIR, DATA + '.ldb')
#     global RPGM2_NAME; RPGM2_NAME = os.path.basename(RPGM2_DIR)

#     global IMPORT_DIR; IMPORT_DIR = CONFIG_DIR + '/' + ENG + '/' + RPGM2_NAME
#     global CSVFILE; CSVFILE = os.path.join(IMPORT_DIR, DATA + '.csv')
#     global JSONFILE; JSONFILE = os.path.join(IMPORT_DIR, DATA + '.json')
#     global XMLFILE; XMLFILE = os.path.join(IMPORT_DIR, DATA + '.edb')


#     # Import RPGM settings

#     ## Move to IMPORT directory
#     if not os.path.exists(IMPORT_DIR):
#         os.makedirs(IMPORT_DIR)
#     os.chdir(IMPORT_DIR)

#     ## LCF2XML

#     ### Convert RPGM database to XML
#     subprocess.run(["lcf2xml", "--2k", RPGM2_DB])

#     ### Convert Saves to XML
#     game_files = os.listdir(RPGM2_DIR)
#     for file in game_files:
#         if file.startswith('Save'):
#             file_loc = os.path.join(RPGM2_DIR, file)
#             subprocess.run(["lcf2xml", "--2k", file_loc])
#             print(file_loc)

#     ## LCGSTRINGS - Export all strings contained in RPGM files to CSV file.
#     LCFSTRINGS = subprocess.run(["lcfstrings", "-s", RPGM2_DB, "utf-8"], capture_output=True)
#     LCFSTRINGS = LCFSTRINGS.stdout
#     csv_file = open(CSVFILE, 'w')
#     csv_file.write(str(LCFSTRINGS.decode('utf-8', 'ignore')))
#     csv_file.close()

#     ## GENCACHE - Create JSON cache.
#     subprocess.run(["gencache", "-p", "-o", JSONFILE, RPGM2_DIR])

#     ## Go back to original directory.
#     os.chdir(SCRIPT_DIR)




# import_game(RPGM2_DIR)


# # Read imported database file
# with open(XMLFILE) as f:
#     DATABASE = xmltodict.parse(f.read())

# actors = DATABASE['LDB']['Database']['actors']['Actor']

# with open(os.path.join(IMPORT_DIR, 'actors.json'), "w") as outfile:
#     json.dump(actors, outfile, indent=2)

# print('RPGM2_NAME: ' + str(RPGM2_NAME))


rpgm2k = Blueprint('rpgm2k', __name__,
  template_folder='templates',
  static_folder='static',
  static_url_path='assets')

@rpgm2k.route('/')
def index():
  return render_template('rpgm2k/index.html')