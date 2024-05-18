import os

# Chemin vers le dossier contenant les masques de segmentation
dossier_masques = "chemin/labelsTs"
dossier_sortie = "chemin/resultats_fusion"

# Parcours de tous les fichiers dans le dossier
for fichier in os.listdir(dossier_masques):
    if fichier.endswith("_SC.nii.gz"):
        # Construction du chemin vers le fichier GM correspondant
        fichier_gm = fichier.replace("_SC.nii.gz", "_GM.nii.gz")
        chemin_sc = os.path.join(dossier_masques, fichier)
        print(f"chemin sc {chemin_sc}")
        chemin_gm = os.path.join(dossier_masques, fichier_gm)
        print(f"chemin gm {chemin_gm}")
        # Vérification de l'existence du fichier GM correspondant
        if os.path.exists(chemin_gm):
            # Construction de la commande pour fusionner les masques SC et GM
            commande = f"python chemin/add_mask_to_seg.py  -i {chemin_sc} -seg {chemin_gm} -o {dossier_sortie} -val 2"
            
            # Exécution de la commande
            os.system(commande)
            print(f"Fusion effectuée pour {fichier}")

        else:
            print(f"Attention: Aucun fichier GM correspondant trouvé pour {fichier}")

