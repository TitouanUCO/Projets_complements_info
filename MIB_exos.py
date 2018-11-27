# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 10:46:04 2018

@author: titou
"""
# -*- coding: utf-8 -*-

from MaBase_MIB import *
from fonctions_MIB import*


### Question 1 : quel est l'ensemble des gardiens?
les_gardiens = {gardien.Nom for gardien in BaseGardiens}
les_villes_agents = {agent.Ville for agent in BaseAgents}
triples = { (alien.NoCabine, alien.Nom, gardien.Nom) for alien in BaseAliens  for gardien in BaseGardiens if gardien.NoCabine == alien.NoCabine}

couples = { (alien.Nom, cabine.NoAllee) for alien in BaseAliens for cabine in BaseCabines if cabine.NoCabine == alien.NoCabine}

allee2={ (alien.Nom) for alien in BaseAliens for cabine in BaseCabines if alien.NoCabine == cabine.NoCabine and cabine.NoAllee == '2'}

cabine_pair={alien.Planete for alien in BaseAliens for cabine in BaseCabines if int(alien.NoCabine)%2 == 0}

agent_Terminus={alien.Nom for alien in BaseAliens for cabine in BaseCabines for gardien in BaseGardiens for agent in BaseAgents if alien.NoCabine==gardien.NoCabine and gardien.Nom==agent.Nom and agent.Ville=='Terminus'}

gardien_feminins_bortsch={gardien.Nom for gardien in BaseGardiens for alien in BaseAliens for miam in BaseMiams if alien.NoCabine==gardien.NoCabine and alien.Sexe=='F' and alien.Nom==miam.NomAlien and miam.Aliment=='Bortsch'}

Terminus_ou_filles={gardien.NoCabine for cabine in BaseCabines for gardien in BaseGardiens for agent in BaseAgents for alien in BaseAliens if alien.NoCabine==gardien.NoCabine and gardien.Nom==agent.Nom and (agent.Ville=='Terminus'or alien.Sexe=='F')}

#question 10 :
def lettre_aliment ():
    lettre_aliment_gardien={ miam.Aliment for gardien in BaseGardiens for alien in BaseAliens for miam in BaseMiams for cabine in BaseCabines if gardien.NoCabine==alien.NoCabine and alien.Nom==miam.NomAlien  and gardien.Nom[0]==miam.Aliment[0] }
    if len(Lettre_aliment_gardien)!=0:
        return("il existe des aliments qui commencent par la même lettre que le nom du gardien qui surveille l'alien qui les mange")
    else: 
        return('non')

# question 11 : existe t'il alien d'eurterpe

def alien_euterpe() :
    n=0
    for alien in BaseAliens :
            if alien.Planete =='Euterpe':
                n=n+1
    if n!=0 :
        print("il existe des aliens venant d'Euterpe")
                                          
                           

#question 12 :
alien_x={nom_x(alien.Nom) for alien in BaseAliens}   #ensemble des aliens ayant un x dans leur nom
def existence_alien_x() :
    alien_x={nom_x(alien.Nom) for alien in BaseAliens}
    noms={alien.Nom for alien in BaseAliens}
    if(len(alien_x)!=len(noms)):
        return("tous les aliens n'ont pas de x dans leurs noms")
    else: 
        return("tous les aliens ont un x dans leurs noms")
    
    

question_13={agent_Terminus.issubset(alien_x) for alien in BaseAliens }  
question_14={alien.Nom for alien in BaseAliens for gardien in BaseGardiens for agent in BaseAgents for cabine in BaseCabines for miam in BaseMiams if alien.Nom==miam.NomAlien and alien.Sexe=='M' and alien.Planete=='Trantor' and ( miam.Aliment=='Bortsch' or (gardien.Nom==agent.Nom and agent.Ville=='Terminus') ) } #bouger les parentheses en fonction de l'interpretation de la question




