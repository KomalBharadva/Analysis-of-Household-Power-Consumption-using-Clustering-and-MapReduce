In order to run the programs, please follow the steps as below:

1) Run "DataPrep.py". This file can be run in any directory.
	This will generate "dataset.txt" file which will be required to run MapReduce program of priority queue.
	This file requires "household_power_consumption.txt" to generate above mentioned file.
	Please use command: "python DataPrep.py" in command prompt to run the program.

2) Copy "dataset.txt", "priorityMapper.py", "priorityReducer.py", "Mapper.py", "Combiner.py", "Reducer.py", "runForSingleNode.sh"
	and "runForMultiNode.sh" in hadoop environment. Please copy these files in home directory of hadoop.
	Note: 1) "runForSingleNode.sh" is required when running the program on local single node.
	      2) "runForMultiNode.sh" is required when running the program on multi node hadoop cluster.

3) Execute the file "runForSingleNode.sh" or "runForMultiNode.sh" as per your environment.
	Please use command: "./filename.sh" to run the program.
	Note: In case you are facing permission related issues, please use "chmod 755 filename.sh" and try again.

4) After successful execution of step 3, program will generate "centroids1.txt" and "labels.txt". Copy these files to your local
	machine for further analysis.

5) Execute "Analysis.ipynb" file for visualisation. This file will require "centroids1.txt", "labels.txt"
	and "household_power_consumption.txt" to perform visualisation.

Note: I have also included a copy of above output files for the reference.
