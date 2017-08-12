# fly-trajectory-mining
A fighter fly out trajectory time series data mining demo, I use agnes and k-means to clustering the flyout data samples into left, straight and right categories. This app includes a fly out trajectory generation program which was developed by matlab and simulink 


1.To dude Sun Yang:
______________________________

'mts-air-maneuvering-samples-1000-txt-form.txt' time series data description.
 we have 1000 time series, each serie have 0-9 sample points by every second, so 1000*10=10000, then the data set have 10000 rows.
 each record in 1 second was composed as below:
 
 x | y | z | y_global_load_factor | time_in_seconds

You could generate more time series samples by using my matlab program 'run.m' and simulink model 'maneuver_generator.slx'



2.Clustering Algorithm adopted by haiyin piao
______________________________

2.1
time series dictance metric by convolution operator.
![](https://raw.githubusercontent.com/HaiyinPiao/fly-trajectory-mining/master/res/TS-distance-principle.png)

2.2
AGNES algorithm.
![](https://raw.githubusercontent.com/HaiyinPiao/fly-trajectory-mining/master/res/agnes-principle.jpg)



3.Clustering Results seems good. 
______________________________
Flight Trajectory Hierarchical Clustering Dendrogram
![](https://raw.githubusercontent.com/HaiyinPiao/fly-trajectory-mining/master/res/plot_dendrogram.png)

Flight Trajectory Cluster 2D Scatter Plot
![](https://raw.githubusercontent.com/HaiyinPiao/fly-trajectory-mining/master/res/2d_traj_scatter.png)

Flight Trajectory Cluster 3D Scatter Plot
![](https://raw.githubusercontent.com/HaiyinPiao/fly-trajectory-mining/master/res/3d_traj_scatter.png)
