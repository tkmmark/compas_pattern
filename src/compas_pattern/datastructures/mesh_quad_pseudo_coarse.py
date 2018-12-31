from compas_pattern.datastructures.mesh_quad_coarse import CoarseQuadMesh
from compas_pattern.datastructures.mesh_quad_pseudo import PseudoQuadMesh

__author__     = ['Robin Oval']
__copyright__  = 'Copyright 2018, Block Research Group - ETH Zurich'
__license__    = 'MIT License'
__email__      = 'oval@arch.ethz.ch'

__all__ = [
	'CoarsePseudoQuadMesh'
]

class CoarsePseudoQuadMesh(CoarseQuadMesh, PseudoQuadMesh):

	def __init__(self):
		super(CoarsePseudoQuadMesh, self).__init__()


	
# ==============================================================================
# Main
# ==============================================================================

if __name__ == '__main__':

	import compas