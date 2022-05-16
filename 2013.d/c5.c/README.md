# Mathématiques - 5e - 2013/2014


## 1 -Organisation du dépôt

* **x-nom-du-chapitres** : Les différents chapitres de cours
 
  * **ipython** : Les fichiers IPython pour le notebook et les présentations de cours.
  * **pdf** : Les fichiers pdf pour l'impression et les présentations de cours.
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

### 1.1 Fonctionnement de IPython

*[IPython](http://ipython.org/) est une console alternative principalement tournée vers l'exploration interactive des données.* - [LinuxFr](https://linuxfr.org/news/sortie-d-ipython-en-version-2-0)

Elle possède également  un [notebook](http://ipython.org/notebook.html) : une interface web riche et un [notebook viewer](http://nbviewer.ipython.org/) permettant de l'afficher dans le navigateur.


## Chapitres

1. Enchaînements d'opérations
2. Symétrie centrale
3. Fractions - Présentation
4. Triangles
5. Fractions - Calcul
6. Calcul littéral
7. Droites et triangles
8. Nombres relatifs - Présentation


#### Chapitres restants

9. Angles et parallélisme.
10. Nombres relatifs - Opération
11. Quadrilatères
12. Proportionnalité
13. Prismes droits et cylindre de révolution
14. Statistiques

## License

Le cours est disponible sous la licence [CC-BY-SA](http://creativecommons.org/licenses/by-sa/3.0/legalcode) (sauf contre-indication).
La licence **CC-BY-SA** est une licence libre, copyleft qui impose la **Paternité** -BY et le **Partage des conditions initiales à l'identique** -SA.

#### Contributeurs

* LAFOND Thomas : https://github.com/homeostasie
* *avec tous mes remerciement à C. Favier.*
