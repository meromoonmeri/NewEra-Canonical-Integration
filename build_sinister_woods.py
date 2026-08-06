import os, json

def build_sinister_woods_integration():
    print("--- NEW ERA : MÀJ INTÉGRATION BOIS SINISTRE (CHAPITRE 6) ---")
    
    plan_path = 'full_canon_integration.json'
    
    with open(plan_path, 'r', encoding='utf-8') as f:
        plan = json.load(f)
        
    # Vérification et mise à jour de la documentation pour le Bois Sinistre
    md = "# Intégration Canonique : Forêt Lugubre -> Bois Sinistre (Chapitre 6)\n\n"
    md += "Ce document définit l'implémentation du **Bois Sinistre (Sinister Woods)** en remplacement de l'ancienne Forêt Lugubre (Gloomy Forest) pour le Chapitre 6 de *New Era*.\n\n"
    
    md += "## 1. Topographie (Extraction Red Rescue Team)\n"
    md += "- **L'Entrée** : `bois_sinistre_entree.rsground` remplace `gloomy_forest_entrance.rsground`.\n"
    md += "- **Le Fond (Boss Arena)** : `bois_sinistre_fond.rsground` remplace `gloomy_forest_boss.rsground`. C'est là que se tiendra le combat de boss du Chapitre 6.\n"
    md += "- **Le Donjon** : Le squelette XML généré à partir de la table GBA de Sinister Woods sera utilisé sous le nom `sinister_woods.xml`.\n\n"
    
    md += "## 2. Place Pokémon (Metano Plaza) : Le Duel contre la Team Dazzling\n"
    md += "La cinématique emblématique de la Place Pokémon (`t01p01`), où la Team Meanies (Ectoplasma, Abo, Charmina) tourmentait le joueur, est **remaniée pour New Era**.\n"
    md += "- **Le Décor** : `place_pokemon.rsground` (La place active, avec la Fontaine et les drapeaux animés).\n"
    md += "- **Les Entités (Replacement)** :\n"
    md += "  - Les coordonnées exactes utilisées par la Team Meanies (Gengar, Ekans, Medicham) dans la GBA seront réutilisées.\n"
    md += "  - Mais l'extracteur de cinématiques a remplacé ces entités par celles de la **Team Dazzling**.\n"
    md += "- **L'Événement** : Cette scène devient le duel narratif de l'arc entre l'équipe du Héros et la Team Dazzling.\n"
    
    with open('/home/user/NewEra-Canonical-Integration/docs/SINISTER_WOODS_AND_DAZZLING_DUEL.md', 'w', encoding='utf-8') as f:
        f.write(md)
        
    print("Documentation d'intégration du Bois Sinistre et du Duel Team Dazzling générée.")

if __name__ == "__main__":
    build_sinister_woods_integration()
