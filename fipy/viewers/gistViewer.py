#!/usr/bin/env python

## -*-Pyth-*-
 # ###################################################################
 #  FiPy - Python-based finite volume PDE solver
 # 
 #  FILE: "gistViewer.py"
 #                                    created: 11/10/03 {2:48:25 PM} 
 #                                last update: 11/2/04 {5:06:55 PM} { 2:45:36 PM}
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

import Numeric

import os
try:
    import gist
    import colorbar
except:
    print "Unable to load gist"

class GistViewer:
    
    id=0
    
    def __init__(self, minVal = None, maxVal = None, title = '', palette = 'heat.gp', grid = 1, limits = None, dpi = 75):

	self.minVal = minVal
        self.maxVal = maxVal
	self.title = title
        self.id = GistViewer.id 
	GistViewer.id += 1
        self.palette = palette
        self.grid = grid
        self.limits = limits
        gist.window(self.id, wait = 1, dpi = dpi, display = '')
        
    def plot(self, minVal = None, maxVal = None, fileName = None):
	array = self.getArray()
        
        gist.window(self.id, wait = 1)
##        gist.window(self.id, wait = 1, dpi = dpi)
	gist.pltitle(self.title)
        gist.animate(1)
        gist.palette(self.palette)
	gist.gridxy(self.grid)
        if self.limits != None:
            gist.limits(self.limits[0], self.limits[1], self.limits[2], self.limits[3])
	
	if minVal is None:
	    if self.minVal is None:
		minVal = Numeric.minimum.reduce(array.flat)
	    else:
		minVal = self.minVal
                
	if maxVal is None:
	    if self.maxVal is None:
		maxVal = Numeric.maximum.reduce(array.flat)
	    else:
		maxVal = self.maxVal

	if maxVal == minVal:
	    maxVal = minVal + 0.01

        self._plot(array, minVal, maxVal)
             
	colorbar.color_bar(minz = minVal, maxz = maxVal, ncol=240, zlabel = 'fred')

        if fileName is not None:
            gist.hcp_file(fileName)
            gist.hcp()
            gist.hcp_finish()

        gist.fma()

    def _plot(self, array, minVal, maxVal):
        gist.pli(array, cmin = minVal, cmax = maxVal)

    def getArray(self):
        pass
        
