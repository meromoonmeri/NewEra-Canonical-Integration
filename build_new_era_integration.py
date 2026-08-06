import os, json

def build_integration_plan():
    print("--- NEW ERA : PURGE ET INTÉGRATION CANONIQUE (CH 6-10) ---")
    
    plan = {
        "directive": "Supprimer les donjons non-canoniques des Chapitres 6 à 10 et les remplacer par les ressources extraites de PMD-RED-PMDO-PORT et PMD-SKY-PMDO-PORT.",
        
        "purge_targets": [
            "Data/Ground/gloomy_forest*.rsground",
            "Data/Ground/crystal_sanctuary*.rsground",
            "Data/Ground/forgotten_marsh*.rsground",
            "Data/Dungeon/gloomy_forest.xml",
            "Data/Dungeon/crystal_sanctuary.xml",
            "Data/Dungeon/forgotten_marsh.xml"
        ],
        
        "integration_mapping": {
            "Chapitre_6": {
                "arc": "Suaire / Accusation",
                "replacement_dungeon": "Sinister Woods (Bois Sinistre)",
                "actions": [
                    {"src": "PMD-RED-PMDO-PORT/Data/Ground/bois_sinistre_entree.rsground", "dest": "Data/Ground/sinister_woods_entrance.rsground"},
                    {"src": "PMD-RED-PMDO-PORT/Data/Ground/bois_sinistre_fond.rsground", "dest": "Data/Ground/sinister_woods_boss.rsground"},
                    {"src": "PMD-RED-PMDO-PORT/Data/Dungeon/sinister_woods.xml", "dest": "Data/Dungeon/sinister_woods.xml"}
                ]
            },
            "Chapitre_10": {
                "arc": "Crise de la Météorite",
                "replacement_dungeon": "Sky Tower (Tour Céleste)",
                "actions": [
                    {"src": "PMD-RED-PMDO-PORT/Data/Ground/tour_celeste_entree.rsground", "dest": "Data/Ground/sky_tower_entrance.rsground"},
                    {"src": "PMD-RED-PMDO-PORT/Data/Ground/tour_celeste_relais.rsground", "dest": "Data/Ground/sky_tower_midpoint.rsground"},
                    {"src": "PMD-RED-PMDO-PORT/Data/Ground/tour_celeste_sommet.rsground", "dest": "Data/Ground/sky_tower_boss.rsground"},
                    {"src": "PMD-RED-PMDO-PORT/Data/Cinematics/d13p03.lua", "dest": "Data/Script/scene/sky_tower_climax.lua"}
                ]
            }
        },
        "status": "READY_FOR_EXECUTION"
    }
    
    with open('integration_plan.json', 'w', encoding='utf-8') as f:
        json.dump(plan, f, indent=2, ensure_ascii=False)
        
    print("Plan d'intégration généré : integration_plan.json")

if __name__ == "__main__":
    build_integration_plan()
