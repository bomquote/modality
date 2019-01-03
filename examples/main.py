# -*- coding: utf-8 -*-

from pyuml2.standard import Model, Package
from pyuml2.uml import Profile, Actor
# from modality.sysml14 import

model = Model()

struct_pkg = Package('Structure')


bob = Actor()
bob.name = 'bob'


print(attrs)