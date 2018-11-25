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


Lettre_aliment_gardien={(gardien.Nom, miam.Aliment) for gardien in BaseGardiens for alien in BaseAliens for miam in BaseMiams for cabine in BaseCabines if gardien.NoCabine==alien.NoCabine and alien.Nom==miam.NomAlien  and gardien.Nom[0]==miam.Aliment[0] }
def lettre_aliment (gardien,aliment):
    n=0
    if gardien[0]==aliment[0]:
        n=n+1
    return(n)

'''Lettre_aliment_gardien2={r!=0 for gardien in BaseGardiens for alien in BaseAliens for miam in BaseMiams for cabine in BaseCabines if( gardien.NoCabine==alien.NoCabine and alien.Nom==miam.NomAlien  (r=lettre_aliment(gardien.Nom,miam.Aliment)) )}'''

alien_euterpe={print('oui') for alien in BaseAliens if alien.Planete=='Euterpe' }




question_14={print('oui') for alien in BaseAliens for gardien in BaseGardiens for agent in BaseAgents for cabine in BaseCabines for miam in BaseMiams if alien.Nom==miam.NomAlien and alien.Sexe=='M' and alien.Planete=='Trantor' and(miam.Aliment=='Bortsch' or (gardien.Nom==agent.Nom and agent.Ville=='Terminus')  }
