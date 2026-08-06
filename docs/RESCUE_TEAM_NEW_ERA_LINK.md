# Intégration de la Place Pokémon (Rescue Team) à Metano Town

Ce document définit l'architecture pour relier géographiquement et narrativement l'ancienne Place Pokémon (Rescue Team) au monde moderne de *New Era: Abyss to Ascension*.

## 1. Connexion Spatiale (Géographie 30 ans plus tard)
La Place Pokémon est toujours florissante et animée. C'est une métropole connectée au reste du monde.

- **Metano Town (Origine)** : Le joueur doit emprunter la sortie **Est** de la ville.
- **Transition** : Une longue route ou l'Étang Barbicha sert de jonction.
- **Destination** : La Place Pokémon (`place_pokemon_active.rsground`), restaurée et animée.

## 2. Le Monde Vivant (TownVoices & Système de Temps)
La Place Pokémon hérite des systèmes dynamiques de *New Era* :
1.  **TownVoices.lua** : Le script de la Place Pokémon sera câblé sur `TownVoices` pour gérer l'évolution des dialogues selon le Chapitre en cours.
2.  **Cycle Jour/Nuit** : Le système météorologique et horaire s'applique.
3.  **Les Raids** : La Place Pokémon intègre le système d'Alerte de Raid (Fédération).

## 3. Remplacement Narratif et Liens Familiaux (Les 30 ans de la Place)
La ville est toujours un pôle d'activité majeur. Les PNJ sont liés à ceux de Metano Town :
- **Frères Kecleon (Marché)** : Ils sont les frères des Kecleon qui opèrent à Metano Town. Le réseau marchand est toujours actif.
- **Kangourex (Stockage)** : Elle est la mère du Kangourex qui tient le stockage de Metano Town (et de Treasure Town). **L'inventaire de la boîte est partagé entre toutes les villes.**
- **Persian (Banque)** : La banque est toujours ouverte. **Le solde de Poképièces est global et partagé avec Metano Town.**
- **Gloupti (Lien)** : Son ancien stand de fusion de capacités est devenu un stand de références historiques/archives.

## 4. Partage des Données (Gameplay PMDO)
Pour que les banques et le stockage fonctionnent, il n'y a pas besoin de scripter des transferts complexes :
Dans PMDO, les services comme la Banque Persian ou le Stockage Kangourex appellent les objets natifs `UI:BankMenu()` et `UI:StorageMenu()`. L'argent et les objets appartiennent au profil du joueur, donc les villes partageront naturellement le même solde, tant que les PNJ appellent la même fonction UI.
