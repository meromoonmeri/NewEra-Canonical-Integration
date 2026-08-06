import os, json

def document_rescue_team_hub_integration():
    md = "# Intégration de la Place Pokémon (Rescue Team) à Metano Town\n\n"
    md += "Ce document définit l'architecture pour relier géographiquement et narrativement l'ancienne Place Pokémon (Rescue Team) au monde moderne de *New Era: Abyss to Ascension* (Metano Town).\n\n"

    md += "## 1. Connexion Spatiale (Géographie 30 ans plus tard)\n"
    md += "La Place Pokémon n'est plus le centre du monde. C'est devenu une zone en retrait, accessible via une nouvelle route sortant de Metano Town.\n\n"
    md += "- **Metano Town (Origine)** : Le joueur doit emprunter la sortie **Est** de la ville (qui mène actuellement aux vieilles friches).\n"
    md += "- **Transition** : L'Étang Barbicha (`etang_barbicha.rsground`). L'étang asséché ou envahi sert de sas entre les deux hubs.\n"
    md += "- **Destination** : La Place Pokémon (`place_pokemon_ruines.rsground`), et la Base de l'Équipe (`base_equipe_sauvetage.rsground`).\n\n"

    md += "## 2. Le Monde Vivant (TownVoices & Système de Temps)\n"
    md += "La Place Pokémon hérite du système central de *New Era* :\n"
    md += "1.  **TownVoices.lua** : Le script de la Place Pokémon sera câblé sur `TownVoices` pour gérer l'évolution des dialogues des PNJ selon l'arc en cours (Chapitre 6, 7, etc.).\n"
    md += "2.  **Cycle Jour/Nuit** : Le système météorologique et horaire s'applique. Nous devrons générer une variante `place_pokemon_ruines_nuit.rsground` (via `pmd_palette.py`) ou appliquer un filtre crépuscule via le Lua de la zone.\n"
    md += "3.  **Les Raids** : La Place Pokémon, étant éloignée, est une zone vulnérable. Le système d'Alerte de Raid (Fédération ou autre) peut s'y déclencher.\n\n"

    md += "## 3. Remplacement Narratif des PNJ (Les survivants)\n"
    md += "Les anciens PNJ sont re-câblés. Ils ne vendent plus les mêmes objets et racontent l'histoire de la décadence des guildes :\n"
    md += "- **Kecleon** : Gère un marché noir ou un stand de reliques.\n"
    md += "- **Persian (Banque)** : Remplacé ou fermé, le bâtiment sert d'abri à des fugitifs.\n"
    md += "- **Gloupti (Lien)** : Transformé en historien du Link Cable.\n"
    md += "- **Kangourex (Stockage)** : Le comptoir est abandonné, c'est là que l'on trouve des indices sur la disparition des anciennes équipes.\n\n"

    md += "## 4. Plan d'Implémentation Lua\n"
    md += "Dans `Data/Script/halcyon/ground/place_pokemon_ruines/init.lua` :\n"
    md += "```lua\n"
    md += "local place_pokemon_ruines = {}\n"
    md += "local MapStrings = \"\"\n"
    md += "function place_pokemon_ruines.Init(map)\n"
    md += "  DEBUG.EnableDbgCoro() -- Activer le débogage\n"
    md += "  MapStrings = COMMON.AutoLoadLocalizedStrings()\n"
    md += "  -- Injection du Monde Vivant New Era\n"
    md += "  COMMON.TownVoices_Init(map)\n"
    md += "end\n\n"
    md += "function place_pokemon_ruines.Enter(map)\n"
    md += "  -- Gestion Jour/Nuit\n"
    md += "  COMMON.ApplyTimeOfDay(map)\n"
    md += "  -- Musique de mélancolie\n"
    md += "  GAME:PlayBGM(\"Melancholy\", true)\n"
    md += "end\n"
    md += "```\n"

    with open('/home/user/NewEra-Canonical-Integration/docs/RESCUE_TEAM_NEW_ERA_LINK.md', 'w', encoding='utf-8') as f:
        f.write(md)
    print("Document d'architecture généré.")

if __name__ == "__main__":
    os.makedirs('/home/user/NewEra-Canonical-Integration/docs', exist_ok=True)
    document_rescue_team_hub_integration()
