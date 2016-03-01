This system now enables you to deconstruct a node network from UE4 and build the individual OpenSCAD models. 
These can then be processed by Slic3r or MakerBot etc.to print the modes in 3D.

The modes can be printed in one of three ways - this mode is chosen by selecting a different starting module;
1. BuildCompactNodes - create 3D models consisting of a base with text/Braille attached to it.
2. BuildExplodedNodes - create 3D modes consisting of the text/Braille strips.
3. BuildExlodedLegoNodes - same as 2, but with the addition of Lego connectors.

NB The exploded modes can use the Basexxx models to produce bases to the 3D strips to be placed on.

The target node is currently specified in ExtractNodes via the INPUT_FILENAME variable. 
This node network will be broken down into individual nodes, which are placed in a temporary folder.
Each node in this folder is then processed by BuildNode, which uses the Processxxxxxx modules to build the normalised models.
These models use the Node and Pin modules to save the normalised format. 
Once the whole node is processed, the Node is written to the GeneratedCode directory.
Node and Pin each have separate modules to write out the normalised node in each of the different modes 
- i.e. Compact, Exloded or ExplodedLego.

Phase1 is the initial version which converts individual nodes to the OpenScad format.

Phase2xxxx are works in progress.
