# PotPlant

## Introduction
A program to root and collpase branches of zero length. Simply a clean up setup prior to analysis.

## Dependecany
Potplant requires dendropy

## Usage
```
usage: potplant.py tree [options]

Run PotPlant.py A program to root and collpase branches of zero length.

positional arguments:
  FILE                  The tree file in newick format.

optional arguments:
  -h, --help            show this help message and exit
  -r FILE [FILE ...], --root FILE [FILE ...]
                        The isolate for rooting the tree.
  -p PREFIX [PREFIX ...], --prefix PREFIX [PREFIX ...]
                        The prefix for the output.
  -d [N], --dirpath [N]
                        Input directory containing the tree. End with a
                        forward slash. Eg. /temp/fasta/
  -o [N], --outdir [N]  Output directory. End with a forward slash. Eg.
                        /temp/fasta/; Default to use current directory.

```

## Etymology
A potplant is a plant that is kept and grown indoors. After growing a tree sometimes you just need to take a tree home. Potplant is your mini tree to take home, after growing your phylogenetic tree.
