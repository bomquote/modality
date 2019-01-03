# -*- coding: utf-8 -*-
"""Definition of meta model 'sysml14'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *


name = "sysml14"
nsURI = "http://www.eclipse.org/papyrus/sysml/1.4/SysML"
nsPrefix = "SysML"

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)
Dummy = EEnum("Dummy", literals=[])
