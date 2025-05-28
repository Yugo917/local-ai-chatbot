### 🧠 1. API Centrale : `LLMApi`

Le cœur de ce module est l’API `LLMApi`, responsable de la coordination des opérations de fine-tuning sur des modèles de langage (LLM). Elle agit comme un point d’accès unifié pour déclencher des processus de personnalisation de modèles, que ce soit via des approches classiques ou des méthodes efficaces en paramètres (PETF).

---

### 🧪 2. `PETFGenerator` : Parameter-Efficient Fine-Tuning

Le module `PETFGenerator` est spécialisé dans la génération de fine-tunings légers pour les modèles LLM, en s'appuyant sur les techniques dites "parameter-efficient" :

* **LoRA**
* **QLoRA**
* **D-LoRA**
* **AdaLoRA**

Ces techniques permettent d’adapter un modèle de fond (base LLM) à des cas d’usage spécifiques, en utilisant des embeddings comme données d’entraînement, tout en réduisant considérablement les ressources nécessaires (temps, mémoire, coût).

---

### 🛠️ 3. `FineTunedModelGenerator` : Génération de Modèle Spécifique

Ce composant utilise une configuration fine-tunée générée par le module `PETFGenerator` pour produire un **modèle LLM personnalisé**. Il applique la méthode choisie (ex. QLoRA) à un modèle de base en intégrant le jeu d'entraînement fourni, afin d'obtenir un modèle prêt à l’usage dans un contexte métier précis (chatbot, moteur de recherche, etc.).

---

### 🔗 4. Synergie et Cas d’Usage

Le pipeline complet fonctionne ainsi :

1. Les embeddings métier sont générés en amont.
2. `PETFGenerator` crée un adaptateur fin-tuné pour un LLM cible à partir de ces embeddings.
3. `FineTunedModelGenerator` applique cet adaptateur au modèle pour produire un LLM prêt à l'emploi.

Ce design permet d’industrialiser la personnalisation de modèles LLM tout en restant efficace, modulaire et adapté à des contextes variés (domaines métiers, langues, tonalités, etc.).

