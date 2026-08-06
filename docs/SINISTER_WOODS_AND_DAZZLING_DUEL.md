# Intégration Canonique : Forêt Lugubre -> Bois Sinistre (Chapitre 6)

Ce document définit l'implémentation du **Bois Sinistre (Sinister Woods)** en remplacement de l'ancienne Forêt Lugubre (Gloomy Forest) pour le Chapitre 6 de *New Era*.

## 1. Topographie (Extraction Red Rescue Team)
- **L'Entrée** : `bois_sinistre_entree.rsground` remplace `gloomy_forest_entrance.rsground`.
- **Le Fond (Boss Arena)** : `bois_sinistre_fond.rsground` remplace `gloomy_forest_boss.rsground`. C'est là que se tiendra le combat de boss du Chapitre 6.
- **Le Donjon** : Le squelette XML généré à partir de la table GBA de Sinister Woods sera utilisé sous le nom `sinister_woods.xml`.

## 2. Place Pokémon (Metano Plaza) : Le Duel contre la Team Dazzling
La cinématique emblématique de la Place Pokémon (`t01p01`), où la Team Meanies (Ectoplasma, Abo, Charmina) tourmentait le joueur, est **remaniée pour New Era**.
- **Le Décor** : `place_pokemon.rsground` (La place active, avec la Fontaine et les drapeaux animés).
- **Les Entités (Replacement)** :
  - Les coordonnées exactes utilisées par la Team Meanies (Gengar, Ekans, Medicham) dans la GBA seront réutilisées.
  - Mais l'extracteur de cinématiques a remplacé ces entités par celles de la **Team Dazzling**.
- **L'Événement** : Cette scène devient le duel narratif de l'arc entre l'équipe du Héros et la Team Dazzling.
