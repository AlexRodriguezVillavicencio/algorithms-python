from sys import path

path.append('..\\packages')

import extra.iota

print(extra.iota.funI())

import packages.extra.good.best.sigma
from packages.extra.good.best.tau import funT

print(packages.extra.good.best.sigma.funS())
print(funT())

#usando un alias
import packages.extra.good.best.sigma as sig
import packages.extra.good.alpha as alp

print(sig.funS())
print(alp.funA())