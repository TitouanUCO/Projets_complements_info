# -*- coding: utf-8 -*-

from MaBase_MIB import *

### Question 1 : quel est l'ensemble des gardiens?
les_gardiens = {gardien.Nom for gardien in BaseGardiens}
les_villes_agents = {agent.Ville for agent in BaseAgents}
triples = { (alien.NoCabine, alien.Nom, gardien.Nom) for alien in BaseAliens  for gardien in BaseGardiens if gardien.NoCabine == alien.NoCabine}

couples={(alien.Nom,cabine.NoAllee) for alien in BaseAliens for cabine in BaseAliens if cabine.NoCabine == alien.NoCabine}
