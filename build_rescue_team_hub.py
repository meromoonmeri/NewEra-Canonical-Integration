import os, json

def document_rescue_team_hub_integration():
    md = "# Intégration de la Place Pokémon (Rescue Team) à Metano Town\n\n"
    md += "Ce document définit l'architecture pour relier géographiquement et narrativement l'ancienne Place Pokémon (Rescue Team) au monde moderne de *New Era: Abyss to Ascension*.\n\n"

    md += "## 1. Connexion Spatiale (Géographie 30 ans plus tard)\n"
    md += "La Place Pokémon est toujours florissante et animée. C'est une métropole connectée au reste du monde.\n\n"
    md += "- **Metano Town (Origine)** : Le joueur doit emprunter la sortie **Est** de la ville.\n"
    md += "- **Transition** : Une longue route ou l'Étang Barbicha sert de jonction.\n"
    md += "- **Destination** : La Place Pokémon (`place_pokemon.rsground`), restaurée et animée.\n\n"

    md += "## 2. Remplacement Narratif et Liens Familiaux (Les 30 ans de la Place)\n"
    md += "La ville est toujours un pôle d'activité majeur. Les PNJ sont liés à ceux de Metano Town :\n"
    md += "- **Frères Kecleon (Marché)** : Ils sont les frères des Kecleon qui opèrent à Metano Town. Le réseau marchand est toujours actif.\n"
    md += "- **Kangourex (Stockage)** : Elle est la mère du Kangourex qui tient le stockage de Metano Town (et de Treasure Town). L'inventaire de la boîte est partagé.\n"
    md += "- **Persian (Banque Monétaire)** : La banque est toujours ouverte. **Persian partage la même fonction de stockage monétaire que Cornèbre à Metano Town.** Le solde de Poképièces est global.\n"
    md += "- **Gloupti (Lien)** : Son ancien stand de fusion de capacités est devenu un stand de références historiques/archives.\n\n"

    md += "## 3. Le Monde Vivant (TownVoices & Système de Temps)\n"
    md += "La Place Pokémon hérite des systèmes dynamiques de *New Era* :\n"
    md += "1.  **TownVoices.lua** : Le script de la Place Pokémon sera câblé sur `TownVoices` pour gérer l'évolution des dialogues selon le Chapitre en cours.\n"
    md += "2.  **Cycle Jour/Nuit** : Le système météorologique et horaire s'applique.\n"
    md += "3.  **Les Raids** : La Place Pokémon intègre le système d'Alerte de Raid (Fédération).\n\n"

    md += "## 4. Partage des Données (Gameplay PMDO)\n"
    md += "Pour que la banque de Persian et de Cornèbre partagent le même compte en banque, leurs deux scripts PNJ feront appel à la même interface native :\n"
    md += "`UI:BankMenu()`.\n"

    with open('/home/user/NewEra-Canonical-Integration/docs/RESCUE_TEAM_NEW_ERA_LINK.md', 'w', encoding='utf-8') as f:
        f.write(md)
        
def document_sky_tower_integration():
    md = "# Intégration Canonique : La Tour Céleste (Sky Tower)\n\n"
    md += "Ce document définit l'implantation canonique de la Tour Céleste dans l'histoire de *New Era*.\n\n"
    
    md += "## 1. Topographie de la Tour\n"
    md += "La Tour Céleste est le climax du jeu. Elle se compose des Maps générées pixel-perfect depuis la GBA :\n"
    md += "- **Entrée (Entrance)** : `sky_tower_entrance.rsground` (Base de la tour qui s'enfonce dans les nuages).\n"
    md += "- **Donjon** : Squelette XML généré à l'étape précédente (étages générés via RogueElements).\n"
    md += "- **Relais (Midpoint)** : `sky_tower_midpoint.rsground`.\n"
    md += "- **Sommet (Boss Arena)** : `sky_tower_boss.rsground` (L'arène brisée au-dessus de l'atmosphère).\n\n"
    
    md += "## 2. Le Script Climax : La Météorite et l'Ultralaser\n"
    md += "Sur la map `sky_tower_boss.rsground`, au moment où l'équipe approche de l'autel, le script extrait de la GBA (`d13p03.lua` rebaptisé `sky_tower_climax.lua`) se déclenche :\n"
    md += "1. Apparition de Rayquaza (hors champ de caméra).\n"
    md += "2. Mouvements de caméra rapides pour inspecter le ciel (Météorite).\n"
    md += "3. **VFX d'Impact** : Flashs blancs massifs (`GAME:FadeOut(true)`) couplés à des `SCREEN_SHAKE` (Son de rugissement + WaitFrames) pour simuler la destruction apocalyptique.\n\n"
    
    md += "## 3. Adaptation New Era\n"
    md += "La seule modification apportée au script original de Chunsoft est narrative : \n"
    md += "Le texte d'époque (les dialogues de Rayquaza) a été purgé de la cinématique. À la place, l'événement lira tes propres chaînes de textes situées dans le dictionnaire `strings.fr.resx` de New Era.\n"
    
    with open('/home/user/NewEra-Canonical-Integration/docs/SKY_TOWER_CLIMAX.md', 'w', encoding='utf-8') as f:
        f.write(md)

if __name__ == "__main__":
    os.makedirs('/home/user/NewEra-Canonical-Integration/docs', exist_ok=True)
    document_rescue_team_hub_integration()
    document_sky_tower_integration()
    print("Documents générés.")
