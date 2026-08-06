import os, json

def build_full_canon_integration():
    print("--- NEW ERA : INJECTION TOTALE DES DONJONS ET GROUNDS CANONIQUES ---")
    
    # Nous construisons le mapping pour TOUS les donjons canoniques de PMD Red
    # qui ont une importance narrative dans l'histoire (ou qui ont été recréés).
    
    plan = {
        "directive": "Intégrer absolument tous les Grounds et Donjons canoniques convertis de PMD Red vers l'architecture New Era PMDO.",
        
        "integration_mapping": [
            # 1. Bois Petit (Tiny Woods)
            {"src_ground": "bois_petit_entree", "dest_ground": "bois_petit_entree", "src_dungeon": "tiny_woods", "dest_dungeon": "tiny_woods"},
            {"src_ground": "bois_petit_fond", "dest_ground": "bois_petit_fond"},
            
            # 2. Grotte Éclair (Thunderwave Cave)
            {"src_ground": "grotte_eclair_entree", "dest_ground": "grotte_eclair_entree", "src_dungeon": "thunderwave_cave", "dest_dungeon": "thunderwave_cave"},
            {"src_ground": "grotte_eclair_fond", "dest_ground": "grotte_eclair_fond"},
            
            # 3. Mont Acier (Mt. Steel)
            {"src_ground": "mont_acier_entree", "dest_ground": "mont_acier_entree", "src_dungeon": "mt_steel", "dest_dungeon": "mt_steel"},
            {"src_ground": "mont_acier_sommet", "dest_ground": "mont_acier_sommet"},
            
            # 4. Bois Sinistre (Sinister Woods) -> Ch 6
            {"src_ground": "bois_sinistre_entree", "dest_ground": "sinister_woods_entrance", "src_dungeon": "sinister_woods", "dest_dungeon": "sinister_woods"},
            {"src_ground": "bois_sinistre_fond", "dest_ground": "sinister_woods_boss"},
            
            # 5. Ravin Silencieux (Silent Chasm)
            {"src_ground": "ravin_silencieux_entree", "dest_ground": "ravin_silencieux_entree", "src_dungeon": "silent_chasm", "dest_dungeon": "silent_chasm"},
            {"src_ground": "ravin_silencieux_fond", "dest_ground": "ravin_silencieux_fond"},
            
            # 6. Mont Foudre (Mt. Thunder)
            {"src_ground": "mont_foudre_entree", "dest_ground": "mont_foudre_entree", "src_dungeon": "mt_thunder", "dest_dungeon": "mt_thunder"},
            {"src_ground": "mont_foudre_relais", "dest_ground": "mont_foudre_relais"},
            {"src_ground": "mont_foudre_sommet", "dest_ground": "mont_foudre_sommet"},
            
            # 7. Grand Canyon (Great Canyon)
            {"src_ground": "grand_canyon_entree", "dest_ground": "grand_canyon_entree", "src_dungeon": "great_canyon", "dest_dungeon": "great_canyon"},
            {"src_ground": "colline_anciens", "dest_ground": "colline_anciens"}, # T01P01 -> Colline
            
            # ARC FUGITIF (Chapitre 12)
            # 8. Grotte Lapis (Lapis Cave)
            {"src_ground": "grotte_lapis_entree", "dest_ground": "grotte_lapis_entree", "src_dungeon": "lapis_cave", "dest_dungeon": "lapis_cave"},
            {"src_ground": "grotte_lapis_fond", "dest_ground": "grotte_lapis_fond"},
            
            # 9. Mont Brasier (Mt. Blaze)
            {"src_ground": "mont_brasier_entree", "dest_ground": "mont_brasier_entree", "src_dungeon": "mt_blaze", "dest_dungeon": "mt_blaze"},
            {"src_ground": "mont_brasier_relais", "dest_ground": "mont_brasier_relais"},
            {"src_ground": "mont_brasier_sommet", "dest_ground": "mont_brasier_sommet"},
            
            # 10. Forêt Givrée (Frosty Forest)
            {"src_ground": "foret_givree_entree", "dest_ground": "foret_givree_entree", "src_dungeon": "frosty_forest", "dest_dungeon": "frosty_forest"},
            {"src_ground": "foret_givree_relais", "dest_ground": "foret_givree_relais"},
            {"src_ground": "foret_givree_fond", "dest_ground": "foret_givree_fond"},
            
            # 11. Mont Gel (Mt. Freeze)
            {"src_ground": "mont_gel_entree", "dest_ground": "mont_gel_entree", "src_dungeon": "mt_freeze", "dest_dungeon": "mt_freeze"},
            {"src_ground": "mont_gel_relais", "dest_ground": "mont_gel_relais"},
            {"src_ground": "mont_gel_sommet", "dest_ground": "mont_gel_sommet"},
            
            # LE CLIMAX (Chapitre 10 / Tour Céleste)
            # 12. Caverne Magma (Magma Cavern)
            {"src_ground": "caverne_magma_entree", "dest_ground": "caverne_magma_entree", "src_dungeon": "magma_cavern", "dest_dungeon": "magma_cavern"},
            {"src_ground": "caverne_magma_relais", "dest_ground": "caverne_magma_relais"},
            {"src_ground": "caverne_magma_fond", "dest_ground": "caverne_magma_fond"},
            
            # 13. Tour Céleste (Sky Tower)
            {"src_ground": "tour_celeste_entree", "dest_ground": "sky_tower_entrance", "src_dungeon": "sky_tower", "dest_dungeon": "sky_tower"},
            {"src_ground": "tour_celeste_relais", "dest_ground": "sky_tower_midpoint"},
            {"src_ground": "tour_celeste_sommet", "dest_ground": "sky_tower_boss"},
            
            # HUBS (Villes / Bases)
            {"src_ground": "base_equipe_sauvetage", "dest_ground": "base_equipe_sauvetage"},
            {"src_ground": "place_pokemon_ruines", "dest_ground": "place_pokemon_ruines"},
            {"src_ground": "dojo_makuhita_ruines", "dest_ground": "dojo_makuhita_ruines"}
        ]
    }
    
    with open('full_canon_integration.json', 'w', encoding='utf-8') as f:
        json.dump(plan, f, indent=2, ensure_ascii=False)
        
    print("Base d'intégration totale générée : full_canon_integration.json")

if __name__ == "__main__":
    build_full_canon_integration()
