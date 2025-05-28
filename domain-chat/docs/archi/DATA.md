### 🧠 1. API Centrale : `CorpusApi`

Le système est structuré autour de l’API centrale `CorpusApi`, qui orchestre la gestion des données textuelles en fonction du domaine métier. Elle agit comme point d’entrée unique pour l’alimentation, le traitement et la consultation du corpus, en coordonnant les différents sous-modules.

---

### 📚 2. `BaseCorpus` : Ressources Linguistiques Génériques

Le module `BaseCorpus` centralise les ressources linguistiques transverses, indépendantes du domaine :

* **Glossaire**
* **Dictionnaire de synonymes**
* **Dictionnaire de paraphrases**

Chaque ressource est sauvegardée dans sa forme brute pour garantir sa régénération (ex. multilingue), assurant ainsi la cohérence et la réutilisabilité du corpus dans le temps.

---

### 🏭 3. `DomainCorpus` : Contenus Métier Spécifiques

Le module `DomainCorpus` prend en charge les données textuelles spécifiques à un domaine métier, comme :

* FAQ
* Tickets
* Conversations
* Documents écrits (Word, Markdown, PDF…)
* Documents visuels (PNG, Draw\.io…)
* Spécifications techniques (OpenAPI, etc.)

Il segmente les documents en chunks, gère la traduction et le code-switching, puis génère des embeddings enrichis de métadonnées pour indexation et exploitation intelligente.

---

### 📝 4. `DomainDocument` : Ingestion de Documents Bruts

Les documents bruts sont d’abord enregistrés via le module `DomainDocument`, qui sauvegarde leur contenu avec un identifiant unique. Ces documents sont ensuite repris par `DomainCorpus` pour traitement, structuration et enrichissement.

---

### 🔁 5. Interdépendance et Synergie

Les interactions entre `BaseCorpus` et `DomainCorpus` permettent d’enrichir dynamiquement les contenus métier avec des ressources linguistiques de base, tout en garantissant une infrastructure robuste, extensible et cohérente. Ce design modulaire favorise la scalabilité et la contextualisation précise des réponses via des modèles d’IA ou des moteurs de recherche sémantique.
