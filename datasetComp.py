import sys
import os

# global

DSStrouver = []
ErreurTrouver = 0

def creerListe(source,sortie):
    
    DIR = []
    FILE = []

    DSSdetruit = 0

    try:
        for dirname, _, filenames in os.walk(source):
            DIR.append(dirname)
            for filename in filenames:
                if(filename == ".DS_Store"):
                    DSStrouver.append(os.path.join(dirname, filename))
                elif(filename.find(".icloud") != -1):
                    print("N'utiliser pas de solution cloud. Fin du programme.")
                    sys.exit(0)
                else:
                    FILE.append(os.path.join(dirname, filename))
    except:
        print("Erreur verifier le chemin donne. Attention a ne pas utiliser de solution cloud.")

    for element in DSStrouver:
        try:
            os.remove(element)
            DSSdetruit = DSSdetruit + 1
        except:
            print("! ==> Erreur lors de la suppression du fichier " + element + ". Supprimer la manuellement.")

    if(len(DSStrouver) != 0):
        print("Des fichiers DS_Store ont ete trouver et détruit.\nFichier trouver :" + str(len(DSStrouver)) + "\nFichier detruit :" + str(DSSdetruit))

    print("\nInformation sur le dataset :")
    print("     -> Nombre de dossier :" + str(len(DIR)))
    print("     -> Nomre de fichiers :" + str(len(FILE)))
    print("")

    try:
        with open(sortie,"w") as extrait:
            
            extrait.write("DIR:" + str(len(DIR)) + "\n")
            for element in DIR:
                extrait.write(element + "\n")

            extrait.write("FILE:" + str(len(FILE)) + "\n")
            for element in FILE:
                extrait.write(element + "\n")

            extrait.write("==END")

        print("Fichier creer avec succes.")
    except:
        print("! ==> Erreur lors de l'ecriture du fichier. Verifier le chemin. Le nom et le type du fichier (txt) doivent etre specifier.")

    print("==> Fin du programme.")
    

def usage():
    print("=================================================================================================")
    print("Script permettant de comparer un datasets locale avec un fichier listant les donnes qu'il est cense contenir.\nLe datasets affiche les image en trop dans le datasets local ainsi que les donnes manquante et les erreurs d'architecture.")
    print("Le script peut egalemment generer un fichier txt listant les donnes d'un datasets.")
    print("Utilisation :")
    print("Le script fonctionne selon deux modes.")
    print("1 ) #~python3 datasetComp.py -compare <chemin du datasets a verifier> <chemin du fchier de comparaison> ")
    print("2 ) #~python3 datasetComp.py -extract <chemin du datasets a scanner> <chemin et nom du fichier contenant la liste>")
    print("#~python3 datasetComp.py --help              Affiche ce menu.")
    print("=================================================================================================")

if __name__ == "__main__":

    if(len(sys.argv) < 3):
        if(sys.arv[1] == "--hep"):
            usage()
        else:
            print("Erreur d'utilisation. Tapez --help pour affiche le menu d'aide")
    else:
        if sys.argv[1] == "-compare":
            #compare(sys.argv[2],sys.argv[3])
            print("On construt")
        elif sys.argv[1] == "-extract":
            creerListe(sys.argv[2],sys.argv[3])
        else:
            print("Erreur d'utilisation. Referer vous au menu.")
    