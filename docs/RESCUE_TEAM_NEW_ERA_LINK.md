# Intégration de la Place Pokémon (Rescue Team) à Metano Town

Ce document définit l'architecture pour relier géographiquement et narrativement l'ancienne Place Pokémon (Rescue Team) au monde moderne de *New Era: Abyss to Ascension* (Metano Town).

## 1. Connexion Spatiale (Géographie 30 ans plus tard)
La Place Pokémon n'est plus le centre du monde. C'est devenu une zone en retrait, accessible via une nouvelle route sortant de Metano Town.

- **Metano Town (Origine)** : Le joueur doit emprunter la sortie **Est** de la ville (qui mène actuellement aux vieilles friches).
- **Transition** : L'Étang Barbicha (`etang_barbicha.rsground`). L'étang asséché ou envahi sert de sas entre les deux hubs.
- **Destination** : La Place Pokémon (`place_pokemon_ruines.rsground`), et la Base de l'Équipe (`base_equipe_sauvetage.rsground`).

## 2. Le Monde Vivant (TownVoices & Système de Temps)
La Place Pokémon hérite du système central de *New Era* :
1.  **TownVoices.lua** : Le script de la Place Pokémon sera câblé sur `TownVoices` pour gérer l'évolution des dialogues des PNJ selon l'arc en cours (Chapitre 6, 7, etc.).
2.  **Cycle Jour/Nuit** : Le système météorologique et horaire s'applique. Nous devrons générer une variante `place_pokemon_ruines_nuit.rsground` (via `pmd_palette.py`) ou appliquer un filtre crépuscule via le Lua de la zone.
3.  **Les Raids** : La Place Pokémon, étant éloignée, est une zone vulnérable. Le système d'Alerte de Raid (Fédération ou autre) peut s'y déclencher.

## 3. Remplacement Narratif des PNJ (Les survivants)
Les anciens PNJ sont re-câblés. Ils ne vendent plus les mêmes objets et racontent l'histoire de la décadence des guildes :
- **Kecleon** : Gère un marché noir ou un stand de reliques.
- **Persian (Banque)** : Remplacé ou fermé, le bâtiment sert d'abri à des fugitifs.
- **Gloupti (Lien)** : Transformé en historien du Link Cable.
- **Kangourex (Stockage)** : Le comptoir est abandonné, c'est là que l'on trouve des indices sur la disparition des anciennes équipes.

## 4. Plan d'Implémentation Lua
Dans `Data/Script/halcyon/ground/place_pokemon_ruines/init.lua` :
```lua
local place_pokemon_ruines = {}
local MapStrings = ""
function place_pokemon_ruines.Init(map)
  DEBUG.EnableDbgCoro() -- Activer le débogage
  MapStrings = COMMON.AutoLoadLocalizedStrings()
  -- Injection du Monde Vivant New Era
  COMMON.TownVoices_Init(map)
end

function place_pokemon_ruines.Enter(map)
  -- Gestion Jour/Nuit
  COMMON.ApplyTimeOfDay(map)
  -- Musique de mélancolie
  GAME:PlayBGM("Melancholy", true)
end
```
