#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2014 Sandia Corporation.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  This software is distributed under the BSD License.
#  _________________________________________________________________________

from pyomo.core import *

def pysp_boundsetter_callback(ph, scenario_tree, scenario):

   # can be eliminated once Pyomo supports parameters in variable
   # bounds declarations.
   instance = scenario._instance
   for t in instance.Times:
      lb = value(instance.Zlb[t])
      ub = value(instance.Zub[t])
      for e in instance.ExitNodes:
         instance.z[e,t].setlb(lb)
         instance.z[e,t].setub(ub)

   for t in instance.Times:
      lb = 0
      ub = value(instance.Zub[t])
      for (i,j) in instance.AllRoads:
         instance.f[i,j,t].setub(ub)
         instance.f[i,j,t].setlb(lb)

      # formula taken from Fernando's AMPL model. Not sure why the time
      # period is restricted to the first year.
      """
      for (i,j) in instance.AllRoads:
         umax = value(sum(model_instance.A[h] * \
                          model_instance.a[h,"Ano1"] \
                          for h in model_instance.HarvestCells))
         instance.f[i,j,t].setub(umax)
         instance.f[i,j,t].setlb(0.0)
      """
