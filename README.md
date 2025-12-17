# 🤖 Agent de Recherche IA

Un assistant de recherche intelligent basé sur l'IA qui utilise LangChain, OpenAI et Tavily pour répondre aux questions en recherchant des informations en temps réel sur le web.

## 📋 Description

Ce projet implémente un agent de recherche IA capable de :
- Répondre aux questions en recherchant des informations récentes sur internet
- Fournir des sources vérifiables pour chaque réponse
- Maintenir un historique de conversation
- Fonctionner via une interface web (Streamlit) ou en ligne de commande

## ✨ Fonctionnalités

- 🔍 **Recherche en temps réel** : Utilise Tavily pour rechercher des informations actuelles sur le web
- 💬 **Interface conversationnelle** : Chat interactif avec historique des conversations
- 📚 **Sources citées** : Affiche les sources utilisées pour chaque réponse
- 🌐 **Interface web** : Application Streamlit intuitive et moderne
- 💻 **Version CLI** : Agent utilisable en ligne de commande
- 🧠 **IA avancée** : Utilise GPT-4o-mini pour des réponses précises et contextuelles

## 🛠️ Technologies Utilisées

- **LangChain 1.2.0+** : Framework pour créer des applications LLM
- **OpenAI GPT-4o-mini** : Modèle de langage pour la génération de réponses
- **Tavily** : Moteur de recherche optimisé pour l'IA
- **Streamlit** : Framework pour créer l'interface web
- **Python 3.12+** : Langage de programmation

## 📦 Prérequis

- Python 3.12 ou supérieur
- Compte OpenAI avec clé API
- Compte Tavily avec clé API

## 🚀 Installation

1. **Cloner le dépôt** (ou naviguer vers le dossier du projet)

2. **Créer un environnement virtuel** :
```bash
python3 -m venv venv
```

3. **Activer l'environnement virtuel** :
```bash
# Sur macOS/Linux
source venv/bin/activate

# Sur Windows
venv\Scripts\activate
```

4. **Installer les dépendances** :
```bash
pip install -r requirements.txt
```

5. **Créer un fichier `.env`** à la racine du projet :
```env
OPENAI_API_KEY=votre_clé_openai_ici
TAVILY_API_KEY=votre_clé_tavily_ici
```

## 🔑 Obtenir les Clés API

### OpenAI API Key
1. Visitez [OpenAI Platform](https://platform.openai.com/)
2. Créez un compte ou connectez-vous
3. Allez dans "API Keys" et créez une nouvelle clé
4. Copiez la clé dans votre fichier `.env`

### Tavily API Key
1. Visitez [Tavily](https://tavily.com/)
2. Créez un compte gratuit
3. Obtenez votre clé API depuis le dashboard
4. Copiez la clé dans votre fichier `.env`

## 📖 Utilisation

### Interface Web (Streamlit)

Lancez l'application web avec :
```bash
streamlit run app.py
```

L'application s'ouvrira automatiquement dans votre navigateur à l'adresse `http://localhost:8501`

**Fonctionnalités de l'interface web :**
- Chat interactif avec historique
- Affichage des sources consultées
- Interface moderne et intuitive

### Version Ligne de Commande

Utilisez l'agent en ligne de commande :
```bash
python my_search_agent.py
```

Tapez vos questions et appuyez sur Entrée. Tapez `quit` ou `exit` pour quitter.

### Tester les Outils de Recherche

Testez directement l'outil de recherche Tavily :
```bash
python tools_test.py
```

### Test Simple du LLM

Testez la connexion avec OpenAI :
```bash
python main.py
```

## 📁 Structure du Projet

```
ai-search-agent/
├── app.py                 # Application Streamlit (interface web)
├── my_search_agent.py     # Agent en ligne de commande
├── tools_test.py          # Test de l'outil Tavily
├── main.py                # Test simple du LLM
├── requirements.txt       # Dépendances Python
├── .env                   # Variables d'environnement (à créer)
├── .gitignore            # Fichiers à ignorer par Git
└── README.md             # Ce fichier
```

## 🎯 Exemples d'Utilisation

### Questions que vous pouvez poser :
- "Quel est le prix actuel de l'action Apple (AAPL) ?"
- "Quelles sont les dernières nouvelles sur l'intelligence artificielle ?"
- "Qui a gagné le dernier match de football ?"
- "Quelles sont les tendances technologiques en 2024 ?"

## 🔧 Configuration Avancée

### Modifier le Modèle OpenAI

Dans `app.py` ou `my_search_agent.py`, changez le modèle :
```python
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
# Options : "gpt-4o-mini", "gpt-4o", "gpt-4", etc.
```

### Modifier le Nombre de Résultats de Recherche

Ajustez le paramètre `k` dans l'initialisation de Tavily :
```python
search_tool = TavilySearchResults(k=3)  # Changez 3 par le nombre souhaité
```

### Personnaliser le Prompt Système

Modifiez le `system_prompt` dans les fichiers pour changer le comportement de l'agent.

## 🐛 Dépannage

### Erreur : "ModuleNotFoundError"
- Assurez-vous que l'environnement virtuel est activé
- Réinstallez les dépendances : `pip install -r requirements.txt`

### Erreur : "API Key not found"
- Vérifiez que le fichier `.env` existe à la racine du projet
- Vérifiez que les clés API sont correctement formatées (sans espaces, sans guillemets)

### Erreur : "Rate limit exceeded"
- Vous avez atteint la limite d'utilisation de l'API OpenAI ou Tavily
- Attendez quelques minutes ou vérifiez votre quota

## 📝 Notes

- Le projet utilise LangChain 1.2.0+ avec la nouvelle API `create_agent`
- L'historique de conversation est maintenu dans la session Streamlit
- Les sources sont automatiquement extraites des résultats de recherche Tavily

## 📄 Licence

Ce projet est fourni à des fins éducatives et de démonstration.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.

## 📧 Support

Pour toute question ou problème, veuillez ouvrir une issue sur le dépôt du projet.

---

**Développé avec ❤️ en utilisant LangChain, OpenAI et Tavily**

