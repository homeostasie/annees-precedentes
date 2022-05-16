# Mathématiques - Première année de bts STS ET - 2014/2015


## 1 -Organisation du dépôt

* **x-nom-du-chapitres** : Les différents chapitres de cours
  * **sources** : Les images servant à la génération des documents
  * **tex** : Les sources tex des documents.
  * *Makefile* : Pour automatiser la génération.

* *README.md* : Ce document de présentations.
* *LICENCE* : La licence de ce dépôt. (voir partie licence ci-dessous)
* *.gitignore* : Pour ignorer les fichiers indésirables dans le dépôts.

### 1.0 Prérequis logiciel.

- [LaTeX](http://www.latex-project.org/) : Générer les documents .tex.
- [Ipe](http://ipe7.sourceforge.net/) : Générer les images des documents.
- [Make](https://www.gnu.org/software/make/) : Automatiser la génération des documents.

### 1.1 Fonctionnement du makefile.

Chaque chapitre possède un fichier makefile permettant d'automatiser la génération des documents. Il prend un certains nombres de paramètres :

```bash
make img # génère les images ipe avec ipetoipe -pdf
make poly # génère le polycopié de cours
make pres # génère le beamer de cours
make ie # génère l'interrogation écrite
make dm # génère le devoir maison
make exo1 # génère l'exercice 1
make proper  # néttoye le dossier tex des résidus de compilation.
make # réalise tous les makes précédents dans l'ordre
```

### Programme officiel

http://maths.ac-orleans-tours.fr/fileadmin/user_upload/maths/Rubrique_institutionnelle/Programmes__documents_ressources/STS/BTS_ProgrammeMathematiques.pdf

## License

Le code source est disponible sous la licence [CC-BY-SA](http://creativecommons.org/licenses/by-sa/3.0/legalcode). License **CC-BY-SA** est copyleft avec **Attribution** -BY *(un bout de moi)* et **ShareAlike** -SA *(à redistribuer sous la même forme)*.

#### Contributeurs

* LAFOND Thomas : https://github.com/homeostasie
