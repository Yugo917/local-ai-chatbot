### 🧠 1. API Centrale : `DataToolApi`

Le composant `DataToolApi` centralise les opérations de transformation et d’enrichissement des données. Il agit comme une couche d’orchestration qui délègue les traitements à deux modules spécialisés : `DataConverter` pour la transformation des formats et `EmbeddingsCreator` pour la vectorisation sémantique.

---

### 🧱 2. `EmbeddingsCreator` : Génération d’Embeddings

Le module `EmbeddingsCreator` transforme des données textuelles enrichies en vecteurs (embeddings) exploitables par des modèles IA.
Exemples d’entrées :

* `datachunk-to-embeddings`
* `faq-to-embeddings`

Chaque entrée est vectorisée avec des métadonnées riches (document ID, section, langue, tags, timestamp…) pour un usage optimal en moteur de recherche sémantique ou chatbot.

```json
{
  "text": "Assurez-vous que votre ordinateur répond à la configuration minimale...",
  "embedding": [0.123, 0.456, 0.789, ...],
  "metadata": {
    "document_id": "doc-001",
    "chunk_id": "doc-001-chunk-003",
    ...
  }
}
```

---

### 🔁 3. `DataConverter` : Transformation de Données

Ce module a pour rôle de convertir des données brutes (markdown, Word, images, discussions) en segments exploitables (`datachunks` ou FAQ). Il propose aussi la génération de données d’entraînement à partir des mêmes sources.

---

### 🔗 4. Synergie et Pipeline

L’ensemble forme une chaîne fonctionnelle complète :

1. `DataConverter` transforme les sources brutes en `datachunks`.
2. `EmbeddingsCreator` enrichit ces chunks avec des vecteurs et des métadonnées.
3. `DataToolApi` orchestre les appels et garantit la cohérence du pipeline.

Ce découpage garantit une architecture modulaire, réutilisable, et prête à alimenter des systèmes de recherche ou d’interrogation assistée par IA.

