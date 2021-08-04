#!/bin/bash

i=1
while :
do

  if [ "$i" == 1 ];
  then
    clear

    echo "================================================================================================"
    echo "Author: Komal Riddhish Bharadva"
    echo "StudentId: x19213051"
    echo "================================================================================================"
    echo "Running MapReduce to calculate initial centroid points using Priority Queuing Algorithm."
    echo "================================================================================================"

    hdfs dfs -mkdir /user

    hdfs dfs -mkdir /user/hduser

    hdfs dfs -mkdir /user/hduser/kmeans

    hdfs dfs -rm /user/hduser/kmeans/*

    hdfs dfs -rm -r -f /user/hduser/kmeans/dataset.txt

    hdfs dfs -copyFromLocal dataset.txt /user/hduser/kmeans

    hdfs dfs -rm -r -f  /user/hduser/output*

    rm -f centroids.txt

    rm -f labels.txt

    mapred streaming -files ./dataset.txt,./priorityMapper.py,./priorityReducer.py \
     -mapper priorityMapper.py -reducer priorityReducer.py \
     -input /user/hduser/kmeans/ -output /user/hduser/output$i

    hdfs dfs -copyToLocal /user/hduser/output$i/part-00000 centroids.txt

    i=$((i+1))
  fi

  rm -f centroids1.txt

  echo "================================================================================================"
  echo "Running MapReduce program to calculate centroids. This step also involves execution of combiner."
  echo "================================================================================================"

  mapred streaming -files ./dataset.txt,./centroids.txt,./Mapper.py,./Combiner.py,./Reducer.py \
   -mapper Mapper.py -combiner Combiner.py -reducer Reducer.py \
   -input /user/hduser/kmeans/ -output /user/hduser/output$i

  hdfs dfs -copyToLocal /user/hduser/output$i/part-00000 centroids1.txt

  match=`python Reader.py`

  if [ "$match" = 1 ];
  then
    echo "================================================================================================"
    echo "Contents of file: Centroids.txt matches with the content of Centroids1.txt."
    echo "================================================================================================"
    break
  elif [ "$i" == 50 ];
  then
    echo "================================================================================================"
    echo "Maximum allowed iteration limit reached."
    echo "================================================================================================"
    break
  fi

  rm centroids.txt

  hdfs dfs -copyToLocal /user/hduser/output$i/part-00000 centroids.txt

  i=$((i+1))

done

echo "================================================================================================"
echo "Generating Labels file."
echo "================================================================================================"

i=$((i+1))

mapred streaming -files ./centroids1.txt,./labelsMapper.py,./labelsReducer.py \
 -mapper labelsMapper.py -reducer labelsReducer.py \
 -input /user/hduser/kmeans/ -output /user/hduser/output$i

hdfs dfs -copyToLocal /user/hduser/output$i/part-00000 labels.txt

hdfs dfs -rm -r -f  /user/hduser/output*
hdfs dfs -rm -r -f /user/hduser/kmeans*

echo "================================================================================================"
echo "Program has been successfully completed."
echo "================================================================================================"
