### 🧠 1. Agent Central : `OptimizedAgent`

`OptimizedAgent` est l'orchestrateur principal chargé de répondre aux requêtes utilisateurs. Il suit une logique d’optimisation des appels aux modèles de langage en s’appuyant sur deux stratégies :

* **Réutilisation de réponses validées** via un cache vectoriel (`CachedAgentResponse`)
* **Enrichissement de la requête** via la génération de pré-prompts (`PrepromptEnhancer`)

---

### 🧾 2. `PrepromptEnhancer` : Générateur de Pré-prompts Contextuels

Ce module est activé si aucune réponse pertinente n’est trouvée dans le cache. Il :

* Récupère la requête originale
* Identifie les `k` chunks les plus pertinents (par similarité cosinus) dans le `DomainCorpus`
* Structure un prompt enrichi avec du contexte métier

Exemple de structuration de prompt :

```plaintext
You are an expert in [domain].
Here are the relevant documents:
[chunk_1]
[chunk_2]
[chunk_3]
Question: [user_query]
Respond clearly and precisely.
```

Ce préprompt est ensuite soumis au modèle LLM sélectionné pour générer une réponse optimisée.

---

### 🗃️ 3. `CachedAgentResponse` : Mémoire de Réponses Validées

Ce module agit comme un cache vectoriel des réponses précédemment validées. Il :

* Cherche des similarités de requête pour réutiliser une réponse existante
* Stocke les nouvelles réponses validées avec leurs embeddings

Ce mécanisme améliore la réactivité du système et évite des appels coûteux ou redondants au modèle LLM.

---

### 🔄 4. Pipeline Global et Intelligence Adaptative

1. L'utilisateur envoie une requête (`ask`)
2. `OptimizedAgent` vérifie l’existence d’une réponse similaire dans `CachedAgentResponse`
3. Si aucune réponse satisfaisante n’est trouvée :

   * Il active `PrepromptEnhancer` pour créer un prompt enrichi
   * Le prompt est soumis à un modèle choisi
   * La réponse peut être validée et sauvegardée via `validate-response`
4. Les réponses validées sont vectorisées et ajoutées au cache pour de futures similarités

