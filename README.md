# Segmentation automatique de la matière grise dans la région lombaire 

Ce répertoire présente une comparaison de méthodes basées sur nnU-Net V2 pour segmenter la matière grise dans la région lombaire.

## Contexte
Les images IRM axiales pondérées en T2* permettent de mesurer la section transversale de la matière grise et blanche, fournissant
des métriques quantitatives de l’ampleur d'un traumatisme et aidant les médecins à quantifier précisément l’importance d’une compression médullaire.
La segmentation manuelle de ces tissus par le radiologue est longue, expliquant l’émergence de techniques de segmentation automatique. 

## Résultats 

### Résultats qualitatifs
Figure 1 : Comparaison des méthodes deepseg_gm de la SCT, nnunet 2d et nnunet3d
![comparaison](https://github.com/ivadomed/lumbar-T2star-GMseg/assets/110342907/7a34bf27-d9c4-4be5-ba39-e74c8d4ba9ae)

légende :
- jaune : segmentation manuelle par l'expert (groundtruth)
- bleu : algorithme deepseg_gm implémenté dans la SCT
- rouge : méthode nnunet 2d testée 
- vert :  méthode nnunet 3d testée

Figure 2 : Comparaison des méthodes deepseg_gm de la SCT, nnunet 2d et 3d basées sur les régions (region based)
![comparaison_regionBased](https://github.com/ivadomed/lumbar-T2star-GMseg/assets/110342907/bb7c17f9-8305-4662-b1d9-867d6dba0a62)
légende :
- gris : segmentation manuelle par l'expert de la matière grise (groundtruth)
- blanc : segmentation manuelle par l'expert de la matière blanche (groundtruth)
- rouge : segmentation de la matière blanche par la méthode nnunet 3d basée sur les régions testée 
- vert : segmentation de la matière grise par la méthode nnunet 3d basée sur les régions testée

### Résultats quantitatifs
# Résultats

Diagrammes en boîte :

| Diagramme 1           | Diagramme 2           | Diagramme 3           |
|-----------------------|-----------------------|-----------------------|
| ![Diagramme 1](https://github.com/ivadomed/lumbar-T2star-GMseg/assets/110342907/3cd6cf5e-49c3-4fd2-b6e0-a377cd539798) | ![Diagramme 2](https://github.com/ivadomed/lumbar-T2star-GMseg/assets/110342907/59730646-8ea2-4231-bbcd-a15ad80e02d7) | ![Diagramme 3](https://github.com/ivadomed/lumbar-T2star-GMseg/assets/110342907/c953f2dc-0a7c-4661-989e-b676ac656501) |
| **Distance de surface moyenne**     | **Indice de Dice**     | **Distance de Hausdorff**     |

| Diagramme 4           | Diagramme 5           | Diagramme 6           |
|-----------------------|-----------------------|-----------------------|
| ![Diagramme 4](https://github.com/ivadomed/lumbar-T2star-GMseg/assets/110342907/edcf5119-9116-48c3-a5c8-449b73ee71ad) | ![Diagramme 5](https://github.com/ivadomed/lumbar-T2star-GMseg/assets/110342907/a941b63d-d1bb-4c61-b668-20c0df3633c7) | ![Diagramme 6](https://github.com/ivadomed/lumbar-T2star-GMseg/assets/110342907/f2158060-4368-484e-96d1-f15e8c97daa5) |
| **Indice de Jaccard**     | **Erreur relative sur le volume**     | **Sensibilité**     |

Temps d'inférence sur CPU:
![temps_inference](https://github.com/ivadomed/lumbar-T2star-GMseg/assets/110342907/4c2d8db4-4f63-499a-a358-da9e07d28176)

## Méthodologie
### Méthode de segmentation de la matière grise 
1. Convertir le jeu de données du format BIDS vers le format nnunet: https://github.com/ivadomed/utilities/blob/main/dataset_conversion/convert_bids_to_nnUNetV2.py

2. Entrainer le modèle :
a) vérifier l'intégrité du jeu de données\n
nnUNetv2_plan_and_preprocess -d DATASET_ID --verify_dataset_integrity -c 2d 3d_fullres 3d_lowres\n
b) lancer l'entrainement sur GPU\n
CUDA_VISIBLE_DEVICES=X nnUNetv2_train DATASET_ID CONFIG FOLD\n

3. Cacluler des métriques avec ANIMA : https://github.com/ivadomed/model_seg_sci/blob/main/testing/compute_anima_metrics.py

4. Tracer des diagrammes en boîte : Utiliser le script boxplot_comparison.py

### Méthode de segmentation de la matière grise et blanche basée sur les régions (region based)
Des modifications ont été aportées aux scripts pour la méthode basée sur les régions

1. Convertir le jeu de données du format BIDS vers le format nnunet: Utiliser le script convert_bids_to_nnUNetV2_region_based.py. Il faudra ensuite fusionner les labels SC et GM.

2. Fusionner les labels SC et GM à l'aide du script : fusion_labels_GM_SC.py

3. Penser à modifier le fichier dataset.json pour indiquer a nnunet qu'on souhaite travailler avec des régions:

{
    "channel_names": {
        "0": "background"
    },
    "labels": {
        "background": 0,
        "SC": [1,2],
	      "GM": [2]
    },
    "regions_class_order":[1,2],
    "numTraining": 41,
    "file_ending": ".nii.gz",
    "overwrite_image_reader_writer": "SimpleITKIO"
}


4. Lancer l'entrainement
   
5ß. Calculer les métriques avec le script 



