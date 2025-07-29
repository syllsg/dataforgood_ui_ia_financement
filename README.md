# Customisation d'une app streamlit afin qu'elle ressemble à la maquette figma désignée.

Dans le cadre de la saison 13 de Data For Good, des bénévoles développent une solution d'IA générative afin d'assister la réponse des associations aux appels à projets des bailleurs de fonds publics et privés, une source clé de financement de leurs initiatives d'intérêt général.
Open source et accessible à toutes les associations dans le besoin, la solution va leur permettre de se concentrer sur les aspects stratégiques et qualitatifs de leur activité, en automatisant les tâches les plus chronophages et en facilitant le reste.
Le projet est sur ce repo : <br>
https://github.com/dataforgoodfr/13_ia_financement

Une maquette a été désignée par notre association partenaire et ici est déployée une application streamlit qui reproduit uniquement le "front" de la future application. Les boutons ne renvoient nulle part et c'est normal, il s'agit de s'assurer de la conformité du design de l'application avant de l'intégrer à la solution développée dans le repo cité plus haut. La maquette est déployée à cette adresse : 
https://dataforgood13uiiafinancement.streamlit.app/

Pour modifier le style de base de streamlit, j'ai choisi d'utiliser un ficher css contenant les infos de style et de tagger les éléments avec une key pour modifier leur style. Celà fonctionne pour beaucoup d'éléments excepté les link_button qui ne possèdent pas d'attributs key.

Pour lancer l'appli en local en cli :
Utiliser UV pour installer les dépendances avec `uv sync`

Puis dans le root folder : <br>
`source .venv/bin/activate` <br>
`streamlit run app_ia_financement.py`






