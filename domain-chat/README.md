# 🧠 GenAI Corpus Suite – Système modulaire de gestion et d’exploitation de corpus métier pour l’IA

Ce dépôt propose une architecture complète pour **structurer**, **transformer**, **vectoriser**, **interroger** et **personnaliser** des données métier en vue de les exploiter avec des modèles de langage (LLM).
L’ensemble est conçu de façon **modulaire** pour faciliter la scalabilité, la maintenabilité et l’adaptation à différents cas d’usage.

---

## 🏗️ Architecture globale – Un pipeline complet pour exploiter l’IA métier

1. 📥 Ingestion et structuration des documents : `CorpusApi`
2. 🔄 Conversion et vectorisation des données : `DataToolApi`
3. 🧪 Personnalisation du modèle : `LLMApi`
4. 💬 Réponse intelligente : `OptimizedAgent`

Chaque brique peut fonctionner **indépendamment** ou en **synergie** avec les autres.

![Archi](docs/archi/archi.png)

---

## ✨ Avantages clés

✅ Architecture **modulaire** et **extensible**
☁️ Compatible avec des modèles LLM **locaux ou cloud**
⚙️ Optimisation des ressources via **embeddings**, **cache** et **fine-tuning allégé**
🧩 Conçu pour les cas d’usage métiers : **support client**, **recherche documentaire**, **agents conversationnels**…

---

## 🤖 1. `OptimizedAgent` – Agent intelligent avec mémoire et contexte

Conçu pour répondre aux requêtes utilisateur de manière rapide et pertinente :

* 🗃️ Recherche dans un **cache vectoriel** (`CachedAgentResponse`) pour réutiliser des réponses validées.
* 🧠 Génération de **pré-prompts enrichis** (`PrepromptEnhancer`) si aucune réponse pertinente n’est trouvée.

📈 Le système s’adapte dynamiquement et **optimise les appels LLM**.

📄 [Voir la documentation détaillée](docs/archi/GEN_AI.md)

---

## 📚 2. `CorpusApi` – Gestion centralisée du corpus métier

Ce module pilote l’organisation des données textuelles en deux volets :

* 📖 **`BaseCorpus`** : ressources linguistiques génériques (glossaire, synonymes, paraphrases).
* 🧩 **`DomainCorpus`** : prise en charge des documents métier (FAQ, tickets, documents visuels ou techniques), segmentation en chunks, enrichissement, vectorisation.
* 🗂️ **Sauvegarde des documents bruts** : permet la **reprise**, la **régénération future**, et l’**ajout de liens directs** vers les sources dans les réponses IA.

📄 [Voir la documentation détaillée](docs/archi/DATA.md)

---

## 🧰 3. `DataToolApi` – Transformation et vectorisation de données

Cette API orchestre deux modules essentiels :

* 🔄 **`DataConverter`** : convertit des fichiers bruts (Markdown, Word, images, discussions...) en **datachunks** ou **FAQ** exploitables.
* 📐 **`EmbeddingsCreator`** : génère des **vecteurs sémantiques** enrichis de métadonnées pour chaque segment.

🔍 Ce pipeline prépare les données pour une **indexation intelligente** ou une **exploitation conversationnelle**.

📄 [Voir la documentation détaillée](docs/archi/TOOLS.md)

---

## 🧪 4. `LLMApi` – Fine-tuning efficace de modèles de langage

Ce composant permet d’adapter un LLM à un cas métier donné avec un minimum de ressources :

* 🧠 **`PETFGenerator`** : génère des configurations de fine-tuning allégé (LoRA, QLoRA, AdaLoRA...).
* 🛠️ **`FineTunedModelGenerator`** : applique ces configurations pour produire un **modèle personnalisé**.

💡 Idéal pour créer des modèles **spécialisés**, sans lourde charge computationnelle.

📄 [Voir la documentation détaillée](docs/archi/LLM.md)
