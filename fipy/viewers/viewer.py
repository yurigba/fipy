#!/usr/bin/env python

## -*-Pyth-*-
 # ###################################################################
 #  FiPy - Python-based finite volume PDE solver
 # 
 #  FILE: "viewer.py"
 #                                    created: 11/10/03 {2:48:25 PM} 
 #                                last update: 3/4/05 {6:07:54 PM} 
 #  Author: Jonathan Guyer <guyer@nist.gov>
 #  Author: Daniel Wheeler <daniel.wheeler@nist.gov>
 #  Author: James Warren   <jwarren@nist.gov>
 #    mail: NIST
 #     www: http://www.ctcms.nist.gov/fipy/
 #  
 # ========================================================================
 # This software was developed at the National Institute of Standards
 # and Technology by employees of the Federal Government in the course
 # of their official duties.  Pursuant to title 17 Section 105 of the
 # United States Code this software is not subject to copyright
 # protection and is in the public domain.  FiPy is an experimental
 # system.  NIST assumes no responsibility whatsoever for its use by
 # other parties, and makes no guarantees, expressed or implied, about
 # its quality, reliability, or any other characteristic.  We would
 # appreciate acknowledgement if the software is used.
 # 
 # This software can be redistributed and/or modified freely
 # provided that any derivative works bear some notice that they are
 # derived from it, and any modified versions bear some notice that
 # they have been modified.
 # ========================================================================
 #  See the file "license.terms" for information on usage and  redistribution
 #  of this file, and for a DISCLAIMER OF ALL WARRANTIES.
 #  
 #  Description: 
 # 
 #  History
 # 
 #  modified   by  rev reason
 #  ---------- --- --- -----------
 #  2003-11-10 JEG 1.0 original
 # ###################################################################
 ##

class Viewer:
    def __init__(self, vars, limits = None, title = None):
        """
        :Parameters:
          - `vars`: a `Variable` or tuple of `Variable` objects to plot
          - `limits`: a dictionary with possible keys `xmin`, `xmax`, 
                      `ymin`, `ymax`, `zmin`, `zmax`, `datamin`, `datamax`.
                      A 1D Viewer will only use `xmin` and `xmax`, a 2D viewer 
                      will also use `ymin` and `ymax`, and so on. 
                      All viewers will use `datamin` and `datamax`. 
                      Any limit set to a (default) value of `None` will autoscale.
          - `title`: displayed at the top of the Viewer window
        """
        if type(vars) not in [type([]), type(())]:
            vars = [vars]
        self.vars = vars
        
        self.limits = limits
        
        if title is None and len(self.vars) == 1:
            title = self.vars[0].getName()
        else:
            title = ''

        self.title = title
        
    def setLimits(self, limits):
        for key in limits.keys():
            self.limits[key] = limits[key]
        
    def getLimit(self, key):
        if self.limits and self.limits.has_key(key):
            limit = self.limits[key]
        else:
            limit = None
            
        return limit

