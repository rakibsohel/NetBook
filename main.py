from   tracking.directory import Monitoring
from   bdd.sqlite         import Database
from   outils.filtre      import Git
from   outils.filtre      import Scenario
import time
import re
import os

def formatDate(date):
    """
    -Cette fonction prend en paramètre la date du PV
    -Retourne la date avec un format exploitable par la base de donnée.
    """
    tmpDate = date.split("/")
    return(tmpDate[2]+"-"+tmpDate[1]+"-"+tmpDate[0])

def main():

    #Git
    """
    ModuleGit = Git("C:/GitHub/Test")
    print(ModuleGit.sha)
    print(ModuleGit.date)
    print(ModuleGit.auteur)
    print(ModuleGit.mail)
    print(ModuleGit.description)
    """

    #Scénario
    programme = Scenario()

    
    # Création des threads.
    thread1 = Monitoring("C:/GitHub/testB")
    thread2 = Monitoring("C:/GitHub/testA")

    thread1.freqMonitoring = 2
    thread2.freqMonitoring = 2
    
    thread1.reqFicExt      = "psc"
    thread2.reqFicExt      = "psc" 

    # Lancement des threads.
    thread1.start()
    thread2.start()

    #Execution
    while 1 :

        #Attente d'une détection d'ajout de fichier dans un répertoire.
        while (thread1.flagAdd == False) and (thread2.flagAdd == False):
            time.sleep(1)

        #Détection d'ajout de fichier dans le répertoire du thread1.
        if(thread1.flagAdd == True):

            #Récupération et affichage de la liste des fichier ajoutés.
            for fic in thread1.lst_diffFiles :
                
                programme.update(fic)

                print(programme.nomFichier)
                print(programme.numProg)
                print(programme.nomProg)    
                print(programme.date)
                print(programme.auteur)
                print(programme.indice)
                print(programme.description)

                print("")
            
                            
            #Initialisation du flag de détection.
            thread1.flagAdd = False

        #Détection d'ajout de fichier dans le répertoire du thread2.
        if(thread2.flagAdd == True):

            #Récupération et affichage de la liste des fichier ajoutés.
            for fic in thread2.lst_diffFiles :
                
                programme.update(fic)

                print(programme.nomFichier)
                print(programme.numProg)
                print(programme.nomProg)    
                print(programme.date)
                print(programme.auteur)
                print(programme.indice)
                print(programme.description)

                print("")            #Initialisation du flag de détection.
            thread2.flagAdd = False        

    #Attente de la fin terminaison des threads.
    thread1.join()
    thread2.join()

    bdd.close()

if __name__=='__main__':
    main()
