#!/usr/bin/env python3


#Created: 06.12.18 - Alexander Wailan
import os

import sys
import argparse
import subprocess
import numpy as np
from pathlib import Path

try:
	import dendropy
except:
	print("Unable to import dendropy")
	sys.exit()


print("You are cleared for dependencies mate. \n")	 


##########################################
# Function to Get command line arguments #
##########################################

def getargv():
    usage = 'potplant.py tree [options]'
    description='Run PotPlant.py A program to root and collpase branches of zero length.'
    parser = argparse.ArgumentParser(usage=usage, description=description)

    parser.add_argument('tree', action="store", help='The tree file in newick format.', metavar='FILE', type=str, nargs='?')
    parser.add_argument('-r',	'--root', action="store", dest="root", help='The isolate for rooting the tree.', metavar='FILE', type=str, nargs='+')
    parser.add_argument('-p',	'--prefix', action="store", dest="prefix", help='The prefix for the output.', metavar='PREFIX', type=str, nargs='+',default='sapling')
    parser.add_argument('-d',    '--dirpath',  action="store",dest="pdir", help='Input directory containing the tree. End with a forward slash. Eg. /temp/fasta/', metavar='N', type=str, nargs='?', default=os.getcwd()+'/')
    parser.add_argument('-o',    '--outdir', action="store", dest="odir", help='Output directory. End with a forward slash. Eg. /temp/fasta/; Default to use current directory.', metavar='N', type=str, nargs='?', default=os.getcwd()+'/')
    return parser.parse_args()


args = getargv()

################
# Main program #
################


#############################################################################################
#
#      Parse/ check the arguements
#
#############################################################################################


##the project directory that holds the samples
pdir = args.pdir

##the project directory that holds the output
odir = args.odir

#read in tree
tree_p = Path(pdir+args.tree)

tree = dendropy.Tree.get(
    path=tree_p,
    schema='newick')

#read in the root isolate name

if args.root is not None:
	root = args.root[0]

#Output prefix

if args.prefix is not 'sapling':
	prefix = args.prefix[0]
else:
	prefix = args.prefix

#####################
# Tree Manipulation #
#####################

#Root the tree with a selected outgroup
if 'root' in locals(): #If root was defined by the user - root the tree
	try:
		print('Rooting the tree with %s.'%root)
		outgroup_node = tree.find_node_with_taxon_label(root)
		tree.to_outgroup_position(outgroup_node, update_bipartitions=False)
		print('Rooting complete. \n')
	except AttributeError:
		print("Outgroup stated cannot be found.")
		

# Collapse the internal edges which are zero.
print('Preparing your sapling by collapsing branches. \n')
tree.collapse_unweighted_edges(threshold=0.5, update_bipartitions=False) #threshold is 0.5 to caputure zero length branches

#Output new tree
sapling = str(prefix+'.tre')
tree.write(path= odir + sapling, schema ="newick")

print('Pot plant preparation complete. Its name is: %s'%sapling)
