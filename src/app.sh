#! /bin/bash

SRCDIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
ROOTDIR=$(dirname $SRCDIR)
VENV=$HOME/.python-env/pyrps

CMD="$1"
OPT="$2"

source $HOME/.python-env/pyrps/bin/activate
DB="$SRCDIR/db.sqlite3"
MAINASSETS="$SRCDIR/main/static/main"

## Start app
run(){
  python3 manage.py runserver 8088 --noreload
}

## Start dev server
server(){
  requirements
  python3 "$SRCDIR/app.py" runserver 8088
}

## Build package
build(){
  cd "$SRCDIR"
  pyinstaller manage.py \
  --name "PyRPS" \
  --distpath "$APPDIR/bin/dist" \
  --workpath "$APPDIR/bin/build" \
  --add-data $SRCDIR/*:. \
  --clean \
  --noconfirm \
  --debug noarchive
}

## Convert sound to webm
convert_sound(){
  FILE="$1"
  FILEPATH="$(basename $FILE)"
  FILENAME="${FILEPATH%.*}"
  MUSICDIR="$ROOTDIR/bin/audio/music"
  echo "$FILENAME"
  ffmpeg -i "$FILE" -dash 1 "$MUSICDIR/$FILENAME.webm"
}

## Initialize database
init_db(){
  if [ -f "$DB" ]; then
    mv $SRCDIR/db.sqlite3 $SRCDIR/db.sqlite3.bak
  fi

  cd "$SRCDIR"

  python3 -m pip install --upgrade pip
  python3 -m pip install wheel
  requirements

  find "$SRCDIR" -type d -name migrations -exec sh -c "rm -rf {}/*; touch {}/__init__.py" \;

  migrations
  # python3 "$SRCDIR/app.py" createsuperuser

  # python3 -c "import utils; utils.import_all();"
}

## Migrate db
migrations(){
  python3 "$SRCDIR/app.py" makemigrations
  python3 "$SRCDIR/app.py" migrate
}

## Install requirements
requirements(){
  python3 -m pip install -q -r "$SRCDIR/requirements.txt"
}

## Compile sass
sassc(){
  python3 "$SRCDIR/app.py" sass $MAINASSETS/sass/style.sass $MAINASSETS/css/style.min.css -g -t compressed --watch
}

$CMD
