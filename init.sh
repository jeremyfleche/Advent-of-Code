#!/bin/sh

# Vérifie les arguments
if [ $# -ne 2 ]; then
    echo "Usage: $0 <jour> <année>"
    exit 1
fi

DAY=$1
YEAR=$2
DIR="$YEAR/$DAY"
INPUT_URL="https://adventofcode.com/$YEAR/day/$DAY/input"
INPUT_FILE="$DIR/input.txt"
PYTHON_FILE="$DIR/$DAY.py"

# Crée le répertoire si nécessaire
mkdir -p "$DIR"

# Crée le fichier Python si inexistant
if [ ! -f "$PYTHON_FILE" ]; then
    cat > "$PYTHON_FILE" <<EOF
import time
from aoc import *

START_TIME = time.time()

texte = read_input("input.txt")



print(f"[{int((time.time()-START_TIME)*1000)}ms]")
EOF
    echo "Fichier Python créé : $PYTHON_FILE"
else
    echo "Le fichier $PYTHON_FILE existe déjà, aucune modification."
fi

# Vérifie le cookie
if [ ! -f ".session" ]; then
    echo "Erreur : le fichier .session est manquant (cookie de session Advent of Code)."
    exit 2
fi

if [ ! -f "$INPUT_FILE" ]; then
    # Télécharge l'input
    curl --fail --silent --show-error \
        --cookie "session=$(cat .session)" \
        "$INPUT_URL" -o "$INPUT_FILE"
    
    if [ $? -eq 0 ]; then
        echo "Input téléchargé dans $INPUT_FILE"
    else
        echo "Erreur lors du téléchargement de l'input."
        exit 3
    fi
else
    echo "L'input existe déjà dans $INPUT_FILE, aucune modification."
fi
