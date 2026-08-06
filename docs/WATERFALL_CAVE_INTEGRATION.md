# Intégration Canonique : Grotte Cascade (Waterfall Cave)

Dans le cadre de la restructuration du **Chapitre 6**, le *Sanctuaire de Cristal* est officiellement supprimé.
Il est remplacé par la **Grotte Cascade** (Waterfall Cave) importée directement de *Pokémon Explorateurs du Ciel*.

## 1. Topographie de la Grotte (Extraction Sky)
- **L'Extérieur (Entrée)** : `waterfall_cave_entrance.rsground` (Converti de `d00p01.sir0`). La géométrie pixel-perfect inclut l'animation (BPA) de l'eau qui s'écoule de la cascade.
- **Le Donjon** : Squelette XML généré à partir de la table NDS de Sky.
- **Le Fond (Boss Arena)** : `waterfall_cave_boss.rsground` (Converti de `d00p02.sir0`). La grande salle souterraine avec son joyau central.

## 2. La Cinématique d'Entrée
La cinématique d'introduction originale de la NDS (`d00p01.ssb`) est récupérée via notre convertisseur Lua.
Elle reproduira :
- L'arrivée de l'équipe devant la cascade.
- Les effets de caméra qui balaient la hauteur de l'eau.
- Le moment clé où la cascade s'ouvre (si géré par effet/changement d'état dans le `rsground`).
- **Les dialogues seront remplacés par l'arc narratif du Chapitre 6 de New Era.**
