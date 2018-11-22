# -*- coding: utf-8 -*-

from MaBase_MIB import *

### Question 1 : quel est l'ensemble des gardiens?
les_gardiens = {gardien.Nom for gardien in BaseGardiens}
les_villes_agents = {agent.Ville for agent in BaseAgents}
triples = { (alien.NoCabine, alien.Nom, gardien.Nom) for alien in BaseAliens  for gardien in BaseGardiens if gardien.NoCabine == alien.NoCabine}

couples = { (alien.Nom, cabine.NoAllee) for alien in BaseAliens for cabine in BaseCabines if cabine.NoCabine == alien.NoCabine}
allee2={ (alien.Nom) for alien in BaseAliens for cabine in BaseCabines if alien.NoCabine == cabine.NoCabine and cabine.NoAllee == '2'}
cabine_pair={alien.Planete for alien in BaseAliens for cabine in BaseCabines if int(alien.NoCabine)%2 == 0}
agent_Terminus={alien.Nom for alien in BaseAliens for cabine in BaseCabines for gardien in BaseGardiens for agent in BaseAgents if alien.NoCabine==gardien.NoCabine and gardien.Nom==agent.Nom and agent.Ville=='Terminus'}
gardien_feminins_bortsch={gardien.Nom for gardien in BaseGardiens for alien in BaseAliens for miam in BaseMiams if alien.NoCabine==gardien.NoCabine and alien.Sexe=='F' and alien.Nom==miam.NomAlien and miam.Aliment=='Bortsch'}
