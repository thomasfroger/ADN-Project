from random import *
#bibliotheque pour prendre de manière aléatoire
def ADN(): 
    adn=open("ADN.txt","w")#création du fichier texte / le "w" est pour write
    nuc2=["A","T","G","C"]# liste nucléotide simple
    nuc=["A=T\n","T=A\n","G=C\n","C=G\n"]
    for i in range(0,1000):#boucle de 0 a 1000 choisit la liste en fonction du nombre 
        nombre=randint(0,20)#tire un nombre aléatoire entre 1 et 20
        if nombre==1: 
            adn.write(choice(nuc2)+"="+choice(nuc2)+"\n") 
            
        else:#sinon il va se passer : on choisit la 2 eme liste
            adn.write(choice(nuc)) 
            
    adn.close() #on ferme la fonction adn

def count_ADN():
    comp=0
    adn=open("ADN.txt","r")
    for i in range (0,1000):
        line=adn.readline()#lire la ligne dans le ADN.txt
        if line == "A=T\n" or line == "T=A\n" or line == "C=G\n" or line == "G=C\n" : #si la ligne est = a nananana alors
            i=i+1
        else:
            comp=comp+1
            print(line)#on affiche la ligne avec l'erreur
            i=i+1
    print(comp)#on affiche le compteur de ligne fausses 
    adn.close()

def repair_ADN():
    perfadn=open("ADN_perfect.txt","w")#perf est une boite a outil pour ecrire executer et analyser des points de reperes
    adn=open("ADN.txt","r")
    for i in range(0,1000):
        line=adn.readline(i)
        if line == "A=T\n" or line=="T=A\n" or line=="G=C\n" or line=="C=G\n":
            perfadn.write(line)#la boite a outil va ecrire dans les lignes
            i=i+1
        else:
            i=i+1
    adn.close()
    perfadn.close()
    
def transcription():
    adn = open("ADN_perfect.txt", "r")
    arn_m = open("ARNm.txt", "w") 
    f=open ("ADN_perfect.txt", "r")
    num=0
   

    bases = adn.readlines()   #bases va lire les lignes de adn              

    for i in range(0, num):#pour i allant de 0 a la valeur de num
        if bases[i][0] == "C": #matrice avec i readline et 0 colonne
            arn_m.write("G") #arn_m ecris G

        elif bases[i][0] == "A": 
            arn_m.write("U")

        elif bases[i][0] == "G":
            arn_m.write("C")

        elif bases[i][0] == "T":
            arn_m.write("A")

    adn.close()
    arn_m.close()


def prot():
    prot=open("proteines.txt","w")#on crée le fichier proyéine et on ecrit dedans
    molecule="" #molecule prend chaine de caractère                          
    with open("ARNm.txt","r") as arn:
        mol=arn.readline() #on lit les lignes de arn               
        for i in range(0,len(mol)-(len(mol)%3),+3): #len c est la taille / %3 c est pour dire qu on les prend par groupe de 3 et +3 qu on laisse un ecart de 3 proteine definit par 3
            proteine=""
            for j in range(3):
                proteine += mol[i+j] #proteine prend un rang en plus dans la molecule
                if (proteine=="UUU" or proteine=="UUC") and molecule !="": #si prot = x ou y ou z et molecule est different de chaine de caractere alors
                    molecule += "Phe-"
                elif (proteine=="UUA" or proteine=="UUG" or proteine=="CUU" or proteine=="CUC" or proteine=="CUA" or proteine=="CUG") and molecule !="":
                    molecule += "Leu-"
                elif (proteine=="AUU" or proteine=="AUC" or proteine=="AUA") and molecule !="":
                    molecule += "Ile-"#+= c est prendre un rang de plus 
                elif (proteine=="AUG"):
                    molecule += "Met-"
                elif (proteine=="GUU" or proteine=="GUC" or proteine=="GUA" or proteine=="GUG") and molecule !="":
                    molecule += "Val-"
                elif (proteine=="UCU" or proteine=="UCC" or proteine=="UCA" or proteine=="UCG") and molecule !="":
                    molecule += "Ser-"
                elif (proteine=="CCU" or proteine=="CCC" or proteine=="CCA" or proteine=="CCG") and molecule !="":
                    molecule += "Pro-"
                elif (proteine=="ACU" or proteine=="ACC" or proteine=="ACA" or proteine=="ACG") and molecule !="":
                    molecule += "Thr-"
                elif (proteine=="GCU" or proteine=="GCC" or proteine=="GCA" or proteine=="GCG") and molecule !="":
                    molecule += "Ala-"
                elif (proteine=="UAU" or proteine=="UAC") and molecule !="":
                    molecule += "Tyr-"
                elif (proteine=="UAA" or proteine=="UAG" or proteine=="UGA") and molecule !="":
                    molecule += "Stop\n"
                    prot.write(molecule)#proteine ecris dans la molecule
                    molecule=""
                elif (proteine=="CAU" or proteine=="CAC") and molecule !="":
                    molecule += "His-"
                elif (proteine=="CAA" or proteine=="CAG") and molecule !="":
                    molecule += "Gln-"
                elif (proteine=="AAU" or proteine=="AAC") and molecule !="":
                    molecule += "Asn-"
                elif (proteine=="AAA" or proteine=="AAG") and molecule !="":
                    molecule += "Lys-"
                elif (proteine=="GAU" or proteine=="GAC") and molecule !="":
                    molecule += "Asp-"
                elif (proteine=="GAA" or proteine=="GAG") and molecule !="":
                    molecule += "Glu-"
                elif (proteine=="UGU" or proteine=="UGC") and molecule !="":
                    molecule += "Cys-"
                elif (proteine=="UGG") and molecule !="":
                    molecule += "Trp-"
                elif (proteine=="CGU" or proteine=="CGC" or proteine=="CGA" or proteine=="CGG") and molecule !="":
                    molecule += "Arg-"
                elif (proteine=="AGU" or proteine=="AGC") and molecule !="":
                    molecule += "Ser-"
                elif (proteine=="AGA" or proteine=="AGG") and molecule !="":
                    molecule += "Arg-"
                elif (proteine=="GGU" or proteine=="GGC" or proteine=="GGA" or proteine=="GGG") and molecule !="":
                    molecule += "Gly-"
    prot.close()#on appelle la fonction proteine

ADN()# on appelle la fnnction ADN
count_ADN()
repair_ADN()
transcription()
prot()
