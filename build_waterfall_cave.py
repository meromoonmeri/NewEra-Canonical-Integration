import os, json

def build_waterfall_integration():
    print("--- NEW ERA : MÀJ INTÉGRATION CANONIQUE (WATERFALL CAVE) ---")
    
    plan_path = 'full_canon_integration.json'
    
    with open(plan_path, 'r', encoding='utf-8') as f:
        plan = json.load(f)
        
    # On ajoute Waterfall Cave au Chapitre 6 (en remplacement de Crystal Sanctuary)
    # L'architecture GBA/NDS de Waterfall Cave (d00p01) est importée.
    
    chapter_6_actions = plan['integration_mapping']
    
    # 1. On cherche si l'action existe déjà pour ne pas dupliquer
    # 2. On injecte les grounds de Waterfall Cave (D00P01 / D00P02 dans Sky)
    waterfall_actions = [
        {"src_ground": "d00p01", "dest_ground": "waterfall_cave_entrance", "src_dungeon": "waterfall_cave", "dest_dungeon": "waterfall_cave"},
        {"src_ground": "d00p02", "dest_ground": "waterfall_cave_boss"},
        {"src_cinematic": "d00p01.lua", "dest_cinematic": "waterfall_cave_intro.lua"}
    ]
    
    plan['integration_mapping'].extend(waterfall_actions)
    
    with open(plan_path, 'w', encoding='utf-8') as f:
        json.dump(plan, f, indent=2, ensure_ascii=False)

    md = "# Intégration Canonique : Grotte Cascade (Waterfall Cave)\n\n"
    md += "Dans le cadre de la restructuration du **Chapitre 6**, le *Sanctuaire de Cristal* est officiellement supprimé.\n"
    md += "Il est remplacé par la **Grotte Cascade** (Waterfall Cave) importée directement de *Pokémon Explorateurs du Ciel*.\n\n"
    
    md += "## 1. Topographie de la Grotte (Extraction Sky)\n"
    md += "- **L'Extérieur (Entrée)** : `waterfall_cave_entrance.rsground` (Converti de `d00p01.sir0`). La géométrie pixel-perfect inclut l'animation (BPA) de l'eau qui s'écoule de la cascade.\n"
    md += "- **Le Donjon** : Squelette XML généré à partir de la table NDS de Sky.\n"
    md += "- **Le Fond (Boss Arena)** : `waterfall_cave_boss.rsground` (Converti de `d00p02.sir0`). La grande salle souterraine avec son joyau central.\n\n"
    
    md += "## 2. La Cinématique d'Entrée\n"
    md += "La cinématique d'introduction originale de la NDS (`d00p01.ssb`) est récupérée via notre convertisseur Lua.\n"
    md += "Elle reproduira :\n"
    md += "- L'arrivée de l'équipe devant la cascade.\n"
    md += "- Les effets de caméra qui balaient la hauteur de l'eau.\n"
    md += "- Le moment clé où la cascade s'ouvre (si géré par effet/changement d'état dans le `rsground`).\n"
    md += "- **Les dialogues seront remplacés par l'arc narratif du Chapitre 6 de New Era.**\n"
    
    with open('/home/user/NewEra-Canonical-Integration/docs/WATERFALL_CAVE_INTEGRATION.md', 'w', encoding='utf-8') as f:
        f.write(md)
        
    print("Plan de Waterfall Cave ajouté à l'intégration !")

if __name__ == "__main__":
    os.makedirs('/home/user/NewEra-Canonical-Integration/docs', exist_ok=True)
    build_waterfall_integration()
