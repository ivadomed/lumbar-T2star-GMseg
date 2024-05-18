import os
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np

def plot_box_plots(xml_folders,method_labels, output_folder):
    # List of metrics calculated by Anima
    metrics = ['Jaccard', 'Dice', 'Sensitivity', 'Specificity', 'PPV', 'NPV', 
               'RelativeVolumeError', 'HausdorffDistance', 'ContourMeanDistance', 'SurfaceDistance']

    metric_values = {metric: [] for metric in metrics}

    for xml_folder in xml_folders:
        method_data = {metric: [] for metric in metrics}
        index = xml_folders.index(xml_folder)
        method_label = method_labels[index]

        for filename in os.listdir(xml_folder):
            if filename.endswith(".xml"):
                xml_path = os.path.join(xml_folder, filename)
                tree = ET.parse(xml_path)
                root = tree.getroot()

                for metric in metrics:
                    metric_node = root.find(f"./measure[@name='{metric}']")
                    if metric_node is not None:
                        metric_value = float(metric_node.text)
                        method_data[metric].append(metric_value)
        
        for metric in metrics:
            metric_values[metric].append(method_data[metric])

    #Plotting the Boxplots
    for metric in metrics:
        plt.figure(figsize=(12, 12))
        plt.boxplot(metric_values[metric], patch_artist=True, labels=method_labels, widths = 0.5)
        plt.title(f"Comparaison des méthodes pour {metric}", fontsize=20) 
        plt.ylabel("Valeur",fontsize=25)
        plt.xlabel("Méthodes testées", fontsize=25)
        plt.grid(True)
        plt.xticks(rotation=20,ha='right',fontsize=18)
        plt.subplots_adjust(wspace=0.5)  
        plt.subplots_adjust(bottom=0.2)
        plt.savefig(os.path.join(output_folder, f"{metric}_comparison_boxplot.png"))  
        plt.close()

if __name__ == "__main__":
    xml_folders = []
    method_labels = []
    n = int(input("Combien de méthodes à comparer ? "))

    for i in range(n):
        folder_path = input(f"chemin vers le dossier contenant les fichiers XML pour la méthode {i+1}: ")
        label = input(f"nom de la méthode {i+1}: ")
        xml_folders.append(folder_path)
        method_labels.append(label)

    output_folder = input("chemin vers le dossier de sortie pour les graphiques: ")
    os.makedirs(output_folder, exist_ok=True)

    plot_box_plots(xml_folders, method_labels, output_folder)
    print("Les diagrammes en boîte ont été enregistrés avec succès.")   
 
