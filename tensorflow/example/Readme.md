To run this example, you must first replace the beginning of the paths
in val.txt and train.txt with the paths to your dataset.

For instance, if this is an entry in val.txt:

/home/esteva/ThrunResearchReserves/skindata2/atlas/images/2676.jpg 2

And your copy of skindata is in folder path/to/folder, then run the
following commands from this folder:

sed -i -- 's/\/home\/esteva\/ThrunResearchReserves\/skindata2/path\/to\/folder' val.txt
sed -i -- 's/\/home\/esteva\/ThrunResearchReserves\/skindata2/path\/to\/folder' train.txt
