# Segmentation automatique de la matière grise dans la région lombaire 

Ce répertoire présente une comparaison de méthodes basées sur nnU-Net V2 pour segmenter la matière grise dans la région lombaire.

## Contexte
Les images IRM axiales pondérées en T2* permettent de mesurer la section transversale de la matière grise et blanche, fournissant
des métriques quantitatives de l’ampleur d'un traumatisme et aidant les médecins à quantifier précisément l’importance d’une compression médullaire.
La segmentation manuelle de ces tissus par le radiologue est longue, expliquant l’émergence de techniques de segmentation automatique. 

## Résultats 
Figure 1 : Comparaison des méthodes deepseg_gm de la SCT, nnunet 2d et nnunet3d
![comparaison](https://github.com/ivadomed/lumbar-T2star-GMseg/assets/110342907/7a34bf27-d9c4-4be5-ba39-e74c8d4ba9ae)

légende :
- jaune : segmenatation manuelle par l'expert (groundtruth)
- bleu : algorithme deepseg_gm implémenté dans la SCT
- rouge : méthode nnunet 2d testée 
- vert :  méthode nnunet 3d testée
