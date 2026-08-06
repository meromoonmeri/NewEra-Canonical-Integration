import os, json

def build_integration_plan():
    print("--- NEW ERA : MÀJ INTÉGRATION CANONIQUE (NOMMAGE PLACE POKÉMON) ---")
    
    with open('full_canon_integration.json', 'r', encoding='utf-8') as f:
        plan = json.load(f)
        
    # Correction du nom de la map destination : on retire "_ruines"
    for action in plan['integration_mapping']:
        if action.get('src_ground') == "place_pokemon_ruines":
            action['dest_ground'] = "place_pokemon"
            action['note'] = "Ville active, connectée à Metano Town."
            
    with open('full_canon_integration.json', 'w', encoding='utf-8') as f:
        json.dump(plan, f, indent=2, ensure_ascii=False)
        
if __name__ == "__main__":
    build_integration_plan()
