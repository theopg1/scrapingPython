# ScrappingPython de MyAnimeList
Projet d'initiation à BeautifulSoup4 ayant pour but de récupérer les données des animes et des mangas de MyAnimeList afin de faire de l'analyse de ses dernières ainsi que d'enrichir la base de donnée du projet Animangas : https://github.com/theopg1/Animangas

# Versions du projet

## v0 :
Le dossier V0 contient les Jupyter Notebook qui ont servis de base au projet. L'un récupère les animes l'autre les mangas. La récupération se fait avec un id en brut dans l'url puis toutes les informations importantes concernants l'oeuvre sont prints.

Initialisation: </br>
`Exécuter les nodes Jupyter permettront d'afficher les données.`

## v1 :
Le dossier V1 contient les version python (py) des jupyters notebook de la version V0 (ipynb). Ces derniers excecutes les mêmes commandes mais les données ne sont pas print dans la console mais envoyé dans une base de donnée SQLite3.

Pour initialiser la base de donnée il suffit de lancer le ficher database.py, un fichier animangas.db sera alors créée.

De plus un fichier jupyter notebook dataAnalyseAnime.ipynb et un futur dataAnalyseManga.ipynb existent afin de faire de l'analyse des données stockées dans la base de donnée.

Initialisation: </br>
1. Se positionner dans le dossier v1, et initialiser la base de données </br>
</t>`scrapingPython\v1> python .\database.py`
2. Toujours dans le dossier v1, exécuter le script de scrapping </br>
</t> `scrapingPython\v2> python .\AnimeScraping.py` </br>
ou </br>
</t> `scrapingPython\v2> python.\MangaScraping.py`
3. Pour lancer les analyses de données </br>
`Exécuter les nodes Jupyter permettront d'afficher les graphiques.`

## v2 :
Le dossier V2 contient la version objet du projet. Ce dernier possède les fichier de création de la base de donnée et les jupyter d'analyse de données comme pour la V1.<br>
Il possède également les fichier scraping.py ainsi que main.py. Le premier contient la class Scraping qui possède les méthodes de scrap pour la page anime et manga.<br>
Le tout lancé depuis le fichier main afin de récupérer les informations si elles n'existent pas déjà dans la base ainsi que d'afficher ces dernières sous forme de tableau.<br>
De plus le résultat de la requête dépend des arguments initialisés dans la commande grâce à argparse.

Initialisation: </br>
1. Se positionner dans le dossier v2, et initialiser la base de données </br>
</t>`scrapingPython\v2> python .\database.py`
2. Toujours dans le dossier v2, exécuter le main en précisant l'id de l'oeuvre ainsi que si c'est un anime ou manga. </br>
`scrapingPython\v2> python .\main.py` suivi d'un des arguments suivants:  
    1. `-i` ou `--id` 'valeur' afin de spécifier l'id de l'oeuvre
    </br>puis 
    1. `-a` ou `--anime` récupèrera les données associées aux top laners
    </br>ou 
    2. `-m` ou `--manga` récupèrera les données associées aux junglers   
3. Pour lancer les analyses de données </br>
`Exécuter les nodes Jupyter permettront d'afficher les graphiques.`

exemples :  
1. `python .\main.py -i 41467 -a`
2. `python .\main.py --id 2 --manga` 

## v3 :
Le dossier V3 possède les mêmes fonctions que la V2, mis à part qu'au lieu de rechercher un anime ou manga à partir d'un id, il va itérer sur cet id vers l'infinie (sauf si arrêt de la commande avec CTRL+C ou fermeture de la cmd). </br>
Ainsi la base de donnée se retrouvera enrichie par le plus d'oeuvres possibles afin de les ajoutés à la bd du site Animangas.

Initialisation: </br>
1. Se positionner dans le dossier v2, et initialiser la base de données </br>
</t>`scrapingPython\v2> python .\database.py`
2. Toujours dans le dossier v2, exécuter le main en précisant l'id de l'oeuvre ainsi que si c'est un anime ou manga. </br>
`scrapingPython\v2> python .\main.py` suivi d'un des arguments suivants:  
    1. `-i` ou `--id` 'valeur' afin de spécifier l'id de l'oeuvre
    </br>puis 
    1. `-a` ou `--anime` récupèrera les données associées aux top laners
    </br>ou 
    2. `-m` ou `--manga` récupèrera les données associées aux junglers   
3. Pour lancer les analyses de données </br>
`Exécuter les nodes Jupyter permettront d'afficher les graphiques.`

exemples :  
1. `python .\main.py -i 41467 -a`
2. `python .\main.py --id 2 --manga` 

## v4 :
Le dossier V4 est la suite du projet qui sera faite dans le futur, cet dernière permettra la conteneurisation du projet avec sa version V3 sur docker afin de le déployé sur une vm azure, aws ou autre.

# Strucutre du projet

```bash
scrapingPython 
├── V0
│   ├── AnimeScraping.ipynb
│   ├── MangaScraping.ipynb
├── V1
│   ├── AnimeScraping.py
│   ├── dataAnalyseAnime.ipynb
│   ├── database.py
│   └── MangaScraping.py
├── V2
│   ├── dataAnalyseAnime.ipynb
│   ├── database.py
│   ├── main.py
│   └── scraping.py
├── V3
│   ├── dataAnalyseAnime.ipynb
│   ├── database.py
│   ├── main.py
│   └── scraping.py
├── V4
│   ├── dataAnalyseAnime.ipynb
│   ├── database.py
│   ├── dockerfile
│   ├── main.py
│   └── scraping.py
```
