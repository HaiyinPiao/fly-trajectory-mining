import scipy
import scipy.cluster.hierarchy as sch
from scipy.cluster.vq import vq, kmeans, whiten
import numpy as np
import matplotlib.pylab as plt
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist
from mpl_toolkits.mplot3d import Axes3D

# import data
#traj = np.loadtxt('trial-data.txt')
traj = np.loadtxt('mts-air-maneuvering-samples-1000-txt-form.txt')
print( traj.shape )

#10 time steps for current flight dataset.
TIME_STEP=10

#delete nlf and time info
traj=np.delete( traj, [3,4], axis=1 )
print( traj.shape )

traj_scat = traj

traj=np.reshape( traj, (-1,TIME_STEP*traj.shape[1]) )
print( traj.shape )

# plt.figure()
# plt.scatter(traj[:, 0], traj[:, 1], traj[:, 2])
# plt.show()

# 1 hierachical clustering by AGNES algorithm
#生成点与点之间的距离矩阵,这里用的manhattan L-1距离:  
dist = sch.distance.pdist( traj, "cityblock" )
#进行层次聚类:  
z = sch.linkage( dist, method='average' )

# c, coph_dists = cophenet(z, pdist(dist))
# print( c )

p = sch.dendrogram( z )

# plt.figure(figsize=(40, 30), dpi=150)
plt.figure()
plt.title('Flight Trajectory Hierarchical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance')
sch.dendrogram(z, leaf_rotation=90.)
# plt.show()
plt.savefig( 'plot_dendrogram.png' )


#根据linkage matrix Z得到聚类结果:  
# cluster = sch.fcluster( z, t=1, criterion='inconsistent' )
cluster = sch.fcluster( z, 2500, criterion='distance' )


print ( 'Original cluster by hierarchy clustering:\n', cluster )
print ( cluster.size )
print('hello agnes')

# show clustering resuts in 2d scatter gram.
# fig = plt.figure(figsize=(30, 30), dpi=150)
fig = plt.figure()
plt.title('Flight Trajectory Cluster 2D Scatter Plot')
plt.xlabel('x east / m ')
plt.ylabel('y north/ m ')
total_clust = np.repeat( cluster, TIME_STEP, axis=0 )
plt.scatter(traj_scat[:, 0], traj_scat[:, 1], s=2, c=total_clust, cmap='prism' )
# legend(loc='upper left')
# plt.show()
plt.savefig( '2d_traj_scatter.png' )

# show clustering resuts in 3d scatter gram.
# fig = plt.figure( figsize=(30, 20), dpi=150 )
fig = plt.figure()
plt.title('Flight Trajectory Cluster 3D Scatter Plot')
plt.xlabel('x east / m ')
plt.ylabel('y north / m ')
plt.ylabel('z up / m ')
ax3D = fig.add_subplot( 111, projection='3d' )
ax3D.scatter( traj_scat[:, 0], traj_scat[:, 1], traj_scat[:, 2], s=2, c=total_clust, cmap='prism' )
plt.savefig( '3d_traj_scatter.png' )