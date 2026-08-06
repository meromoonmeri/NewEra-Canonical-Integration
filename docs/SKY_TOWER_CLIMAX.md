# Intégration Canonique : La Tour Céleste (Sky Tower)

Ce document définit l'implantation canonique de la Tour Céleste dans l'histoire de *New Era*.

## 1. Topographie de la Tour
La Tour Céleste est le climax du jeu. Elle se compose des Maps générées pixel-perfect depuis la GBA :
- **Entrée (Entrance)** : `sky_tower_entrance.rsground` (Base de la tour qui s'enfonce dans les nuages).
- **Donjon** : Squelette XML généré à l'étape précédente (étages générés via RogueElements).
- **Relais (Midpoint)** : `sky_tower_midpoint.rsground`.
- **Sommet (Boss Arena)** : `sky_tower_boss.rsground` (L'arène brisée au-dessus de l'atmosphère).

## 2. Le Script Climax : La Météorite et l'Ultralaser
Sur la map `sky_tower_boss.rsground`, au moment où l'équipe approche de l'autel, le script extrait de la GBA (`d13p03.lua` rebaptisé `sky_tower_climax.lua`) se déclenche :
1. Apparition de Rayquaza (hors champ de caméra).
2. Mouvements de caméra rapides pour inspecter le ciel (Météorite).
3. **VFX d'Impact** : Flashs blancs massifs (`GAME:FadeOut(true)`) couplés à des `SCREEN_SHAKE` (Son de rugissement + WaitFrames) pour simuler la destruction apocalyptique.

## 3. Adaptation New Era
La seule modification apportée au script original de Chunsoft est narrative : 
Le texte d'époque (les dialogues de Rayquaza) a été purgé de la cinématique. À la place, l'événement lira tes propres chaînes de textes situées dans le dictionnaire `strings.fr.resx` de New Era.
