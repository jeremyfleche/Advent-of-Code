if [ $# -ne 2 ]; then
    echo "Usage : ./init day year"
    exit 1
fi

day=$1
annee=$2
url="https://adventofcode.com/$annee/day/$day/input"
destination="./$annee/$day/input.txt"
cookie="session=53616c7465645f5f694bcddb7db208b66bfa129100b26cc80feec03e83d4d06003b55c7a15bceae1d393b206fc28557b043c7d9b05c0fd8520b9938d24d09bf8"

if ! wget --header="Cookie: $cookie" --tries=10 --timeout=10 -q -O "$destination" "$url"; then
    echo "Erreur : Le téléchargement a échoué après 10 tentatives."
    echo "URL : $url"
    echo "Peut-être qu'il n'y a juste pas d'input aujourd'hui !"
    exit 1
else
    echo "Téléchargement de input.txt réussi."
fi
