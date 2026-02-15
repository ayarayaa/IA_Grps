# TP M104 - Analyse Statistique des Performances Étudiantes


## Objectif du TP

Analyser les performances des étudiants dans les matières de mathématiques, lecture et écriture à l'aide de techniques statistiques avancées en utilisant le dataset **StudentsPerformance.csv**.

---

## Structure du TP

```
Nom_Prenom/
│
├── TP_M104_Statistiques_App.html    # Application web interactive
├── StudentsPerformance.csv           # Dataset (deja fournir)
└── TP_NoteBook.ipynb                # Ce document
|__ Readme.md                        # Description
```


## Exercices du TP

### **Exercice 1: Analyse des Tendances Centrales**

- Calculer et comparer la moyenne, la médiane et le mode des scores
- Déduire la distribution des scores selon ces mesures

#### Mesures Calculées
| Mesure | Formule | Signification |
|--------|---------|---------------|
| **Moyenne** | μ = Σx / n | Valeur centrale représentative |
| **Médiane** | Valeur au milieu | Résiste aux valeurs extrêmes |
| **Mode** | Valeur la plus fréquente | Score le plus commun |

#### Interprétations
- **Moyenne ≈ Médiane** → Distribution symétrique
- **Moyenne > Médiane** → Asymétrie positive (queue à droite)
- **Moyenne < Médiane** → Asymétrie négative (queue à gauche)

---

### **Exercice 2: Analyse de la Dispersion**

#### a) Étendue

**Formule:** Étendue = Max - Min

**Question:** Identifiez la matière avec la plus grande étendue. Que cela indique-t-il sur la variabilité des scores ?

**Interprétation:**
- Étendue élevée → Grande variabilité entre les étudiants
- Étendue faible → Scores homogènes

#### b) Variance et Écart-type

**Formules:**
```
Variance (σ²) = Σ(xi - μ)² / n
Écart-type (σ) = √Variance
```

**Question:** Quelle matière présente la plus grande variabilité des scores ?

**Interprétation:**
- σ < 15 → Faible variabilité (scores homogènes)
- σ ≥ 15 → Forte variabilité (scores hétérogènes)

---

### **Exercice 3: Quartiles et IQR**

#### a) Calcul des Quartiles

| Quartile | Position | Signification |
|----------|----------|---------------|
| **Q1** | 25% | 25% des scores sont inférieurs |
| **Q2** | 50% | Médiane |
| **Q3** | 75% | 75% des scores sont inférieurs |

**IQR (Intervalle Interquartile):**
```
IQR = Q3 - Q1
```

#### b) Détection des Valeurs Aberrantes

**Méthode:**
```
Limite inférieure = Q1 - 1.5 × IQR
Limite supérieure = Q3 + 1.5 × IQR
```

**Valeur aberrante:** Toute valeur en dehors de [Limite inf, Limite sup]

**Interprétation:**
- Présence de valeurs aberrantes → Scores extrêmes (très bons ou très mauvais)
- Absence de valeurs aberrantes → Distribution normale

---

### **Exercice 4: Visualisation des Données**

#### a) Graphiques

**Types de graphiques créés:**
1. **Histogrammes** → Distribution des fréquences
2. **Boîtes à moustaches** (Box plots) → Quartiles et valeurs aberrantes
3. **Graphiques en barres** → Comparaisons entre matières

#### b) Analyse de la Forme

**Formes de distribution:**

| Type | Caractéristiques | Moyenne vs Médiane |
|------|------------------|-------------------|
| **Symétrique** | En forme de cloche | Moyenne ≈ Médiane |
| **Asymétrique positive** | Queue à droite | Moyenne > Médiane |
| **Asymétrique négative** | Queue à gauche | Moyenne < Médiane |
| **Bimodale** | Deux pics | Deux modes distincts |

---

### **Exercice 5: Analyse Croisée et Insights**

#### a) Corrélation entre les Scores

**Coefficient de Pearson:**
```
r = Σ((xi - x̄)(yi - ȳ)) / √(Σ(xi - x̄)² × Σ(yi - ȳ)²)
```

**Interprétation du coefficient r:**
| Valeur | Force | Signification |
|--------|-------|---------------|
| 0.7 - 1.0 | **Forte** | Relation très marquée |
| 0.4 - 0.7 | **Modérée** | Relation significative |
| 0.0 - 0.4 | **Faible** | Relation peu marquée |

**Corrélations attendues:**
- **Math ↔ Lecture:** Compétences analytiques communes
- **Math ↔ Écriture:** Logique et expression
- **Lecture ↔ Écriture:** Compétences linguistiques liées

#### b) Facteurs Influents

**Variables à explorer dans le dataset:**
- `parental level of education` → Impact de l'éducation parentale
- `lunch` → Statut socio-économique (standard/free-reduced)
- `test preparation course` → Effet de la préparation
- `gender` → Différences de performance
- `race/ethnicity` → Diversité des performances
--

## Livrables à Soumettre

Vous devez créer un dossier personnel et le pousser sur le dépôt GitHub de la classe.

### Structure Obligatoire du Dossier

```
Nom_Prenom/
│
├── TP_M104_Statistiques_App.html    # Application web interactive
├── Readme.md                        # Description
└── TP_NoteBook.ipynb                # Notebook Jupyter avec analyses
```

### Description des Fichiers

| Fichier | Description | Obligatoire |
|---------|-------------|-------------|
| `TP_M104_Statistiques_App.html` | Application web interactive fournie | Oui |
| `TP_NoteBook.ipynb` | Votre notebook avec analyses et réponses | Oui |

---

## Dépôt GitHub

### URL du Dépôt
```
https://github.com/Kell1000/IA_Grps.git
```

### Instructions Git

#### Cloner le Dépôt

```bash
# Cloner le dépôt
git clone https://github.com/Kell1000/IA_Grps.git

# Accéder au dossier
cd IA_Grps
```

#### Créer Votre Dossier Personnel

```bash
# Créer votre dossier avec votre nom et prénom
mkdir Nom_Prenom

# Exemple : mkdir IDRISSI_Ahmed
```

#### Organiser Vos Fichiers

```bash
# Copier les fichiers dans votre dossier
cp chemin/vers/TP_M104_Statistiques_App.html Nom_Prenom/
cp chemin/vers/StudentsPerformance.csv Nom_Prenom/
cp chemin/vers/TP_NoteBook.ipynb Nom_Prenom/
```

#### Pousser sur GitHub

```bash
# Ajouter vos fichiers
git add Nom_Prenom/

# Créer un commit avec un message clair
git commit -m "Ajout TP M104 - Nom Prenom"

# Pousser vers GitHub
git push origin main
```

### Règles Importantes Git

- **Nommez votre dossier:** `Nom_Prenom` (pas d'espaces, utilisez `_`)
- **Un seul dossier par étudiant**
- **Ne modifiez pas les dossiers des autres étudiants**
- **Vérifiez que tous les fichiers sont présents avant de push**
- **Message de commit clair:** "Ajout TP M104 - Nom Prenom"

---
---

## Bonus: Explorations Avancées

### Graphiques Supplémentaires à Créer

1. **Heatmap de Corrélation**
   - Visualiser toutes les corrélations simultanément
   - Utiliser des couleurs pour l'intensité

2. **Distributions par Groupe**
   - Comparer les performances par genre
   - Analyser l'impact du niveau d'éducation parental

3. **Box Plots Comparatifs**
   - Visualiser les quartiles des 3 matières côte à côte
   - Identifier visuellement les valeurs aberrantes

4. **Scatter Matrix**
   - Matrice de nuages de points pour toutes les paires
   - Détecter les relations non-linéaires

---

## Ressources Complémentaires

### Concepts Statistiques
- **Statistiques descriptives:** Résumer et décrire les données
- **Mesures de tendance centrale:** Identifier le "centre" des données
- **Mesures de dispersion:** Quantifier la variabilité
- **Corrélation:** Mesurer la relation entre variables

### Outils Python (pour aller plus loin)
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données
df = pd.read_csv('StudentsPerformance.csv')

# Statistiques descriptives
df.describe()

# Corrélations
df[['math score', 'reading score', 'writing score']].corr()

# Visualisations
sns.heatmap(df.corr(), annot=True)
plt.show()
```

---

## Contact et Support

**Formateur:** [Mr. KELLA]  
**Module:** M104 - Mathématiques pour le traitement des données  
**Filière:** Intelligence Artificielle

