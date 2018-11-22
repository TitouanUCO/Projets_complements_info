# -*- coding: utf-8 -*-

from MaBase_MIB import *

### Question 1 : quel est l'ensemble des gardiens?
les_gardiens = {gardien.Nom for gardien in BaseGardiens}
