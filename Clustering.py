# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 19:39:07 2023

@author: Aliha
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPlainTextEdit
from PyQt5.QtWidgets import QLabel, QPushButton, QMessageBox, QFileDialog,QGraphicsScene
from PyQt5.QtGui import QImage, QPixmap
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


import numpy as np
from sklearn.datasets import make_blobs
import time
from sklearn.cluster import KMeans, AffinityPropagation, MeanShift,SpectralClustering, AgglomerativeClustering, DBSCAN
from sklearn.metrics.pairwise import euclidean_distances

from Common_Processes import Common_Proc


import matplotlib.pyplot as plt
# from kneed import KneeLocator
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

class Clustering(Common_Proc):
    
    
    def __init__(self):
        """
        Contructor of Clustering class

        Returns
        -------
        None.

        """
        super().__init__()
       
           
    def hierarchicalClustering(self):
        """
        
        This function operates Hierarchical Clustering algorithm
        
        Returns
        -------
        None.

        """
        points = np.array(self.get_text_data())
        linkage_type = 'ward'
        distance_threshold = None
        hierarchical_clustering = AgglomerativeClustering(linkage=linkage_type, distance_threshold=distance_threshold)
        labels = hierarchical_clustering.fit_predict(points)

        # Calculate cluster centers
        cluster_centers = []
        for label in np.unique(labels):
            cluster_points = points[labels == label]
            cluster_center = np.mean(cluster_points, axis=0)
            cluster_centers.append(cluster_center)
        centroids = np.array(cluster_centers)

        # Calculate objective function
        objective_function = 0
        max_distance = 0
        for i, center_i in enumerate(centroids):
            farthest_distance_i = np.max(euclidean_distances(points[labels == i], [center_i]))
            max_distance = max(max_distance, farthest_distance_i)

            for j, center_j in enumerate(centroids):
                if i == j:
                    continue
                farthest_distance_j = np.max(euclidean_distances(points[labels == j], [center_j]))
                distance_ij = np.linalg.norm(center_i - center_j)
                objective_function_ij = farthest_distance_i + 0.75 * distance_ij + farthest_distance_j
                objective_function = max(objective_function, objective_function_ij)

        # Plotting
        fig = Figure()
        canvas = FigureCanvas(fig)
        
        ax = fig.add_subplot(111)
        ax.scatter(*zip(*points), c=labels, cmap='coolwarm')
        ax.scatter(*zip(*centroids), color='black', marker='*', s=100)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_title("Hierarchical Clustering")
        canvas.draw()
        current_scene = QGraphicsScene()
        current_scene.addWidget(canvas)
        self.Output_scene.append(current_scene)
        
        
    def K_Means(self):
        """
        
        This function operates K-Means algorithm 

        Returns
        -------
        None.

        """
    
        points = np.array(self.get_text_data())

        scaler = StandardScaler()
        scaled_features = scaler.fit_transform(points)
        
        kmeans = KMeans(
            init=self.get_initFromUser(),
            n_clusters=self.get_clusterFromUser(),
            n_init=10,
            max_iter=self.get_maxIterFromUser(),
           random_state=42,
           algorithm = self.get_algorithmFromUser()
       )
        
        
        kmeans.fit(points)
        centroids = kmeans.cluster_centers_
        labels = kmeans.labels_
        

        fig = Figure()
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        ax.scatter(*zip(*points), c=labels, cmap='coolwarm')
        ax.scatter(*zip(*centroids), color='black', marker='*', s=100)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_title("K-means Clustering")
        canvas.draw()
        current_scene = QGraphicsScene()
        current_scene.addWidget(canvas)
        self.Output_scene.append(current_scene)
    
   
        
    def affinityPropagation(self):
        """
        This function operates Affinity Propagation

        Returns
        -------
        None.

        """
        
        points = np.array(self.get_text_data())
        damping = 0.5
        max_iter = self.get_maxIterFromUser()
        
                
        
        af = AffinityPropagation(damping=damping, max_iter=max_iter).fit(points)
        cluster_centers = af.cluster_centers_
        cluster_centers_indices = af.cluster_centers_indices_
        labels = af.labels_
        
        n_clusters_ = len(cluster_centers_indices)
        print (n_clusters_)
        
        fig = Figure()
        canvas = FigureCanvas(fig)
        plt = fig.add_subplot(111)
        
  
        plt.scatter(*zip(*points), c=labels, cmap='coolwarm')
        plt.scatter(*zip(*cluster_centers), color='black', marker='*', s=100)

        plt.set_ylabel("X")
        plt.set_ylabel("Y")
        plt.set_title("Affinity Propagation")
        canvas.draw()
        current_scene = QGraphicsScene()
        current_scene.addWidget(canvas)
        
        self.Output_scene.append(current_scene)
        
    def DBSCAN(self):
        """
        This function operates DBSCAN algorithm

        Returns
        -------
        None.

        """
        
        points = np.array(self.get_text_data())
        eps = 0.5
        min_samples = 5
        dbscan = DBSCAN(eps=eps, min_samples=min_samples)
        labels = dbscan.fit_predict(points)

        cluster_centers = []
        valid_labels = np.unique(labels)
        for label in valid_labels:
            cluster_points = points[labels == label]
            if len(cluster_points) == 0:
                continue
            cluster_center = np.mean(cluster_points, axis=0)
            cluster_centers.append(cluster_center)
        centroids = np.array(cluster_centers)

        # Calculate objective function
        objective_function = 0
        max_distance = 0
        for i, center_i in enumerate(centroids):
            cluster_i_points = points[labels == valid_labels[i]]
            farthest_distance_i = np.max(euclidean_distances(cluster_i_points, [center_i]))
            max_distance = max(max_distance, farthest_distance_i)

            for j, center_j in enumerate(centroids):
                if i == j:
                    continue
                cluster_j_points = points[labels == valid_labels[j]]
                farthest_distance_j = np.max(euclidean_distances(cluster_j_points, [center_j]))
                distance_ij = np.linalg.norm(center_i - center_j)
                objective_function_ij = farthest_distance_i + 0.75 * distance_ij + farthest_distance_j
                objective_function = max(objective_function, objective_function_ij)

        # Plotting
        fig = Figure()
        canvas = FigureCanvas(fig)
        
        ax = fig.add_subplot(111)
        ax.scatter(*zip(*points), c=labels, cmap='coolwarm')
        ax.scatter(*zip(*centroids), color='black', marker='*', s=100)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_title("DBSCAN Clustering")
        canvas.draw()
        
        current_scene = QGraphicsScene()
        current_scene.addWidget(canvas)
        self.Output_scene.append(current_scene)    
    
    def Mean_Shift(self):
         """
        This function operates Mean Shift algorithm

        Returns
        -------
        None.

        """
         points = np.array(self.get_text_data())
         bandwidth = None
         mean_shift = MeanShift(bandwidth=bandwidth)
         mean_shift.fit(points)
         cluster_centers = mean_shift.cluster_centers_
         labels = mean_shift.labels_

         fig = Figure()
         canvas = FigureCanvas(fig)
   
         ax = fig.add_subplot(111)
         ax.scatter(*zip(*points), c=labels, cmap='coolwarm')
         ax.scatter(*zip(*cluster_centers), color='black', marker='*', s=100)
         ax.set_xlabel("X")
         ax.set_ylabel("Y")
         ax.set_title("Mean Shift ")
         canvas.draw()

         current_scene = QGraphicsScene()
         current_scene.addWidget(canvas)
         self.Output_scene.append(current_scene)
    
    def spectralClustering(self):
        """
        This function operates Spectral Clustering algorithm

        Returns
        -------
        None.

        """
        
        Data = np.array(self.get_text_data())
        spectral_clustering = SpectralClustering(n_clusters=self.get_clusterFromUser())
        labels = spectral_clustering.fit_predict(Data)

        # Calculate cluster centers
        cluster_centers = []
        valid_labels = np.unique(labels)
        for label in valid_labels:
            cluster_points = Data[labels == label]
            cluster_center = np.mean(cluster_points, axis=0)
            cluster_centers.append(cluster_center)
        centroids = np.array(cluster_centers)

        # Calculate objective function
        objective_function = 0
        max_distance = 0
        for i, center_i in enumerate(centroids):
            cluster_i_points = Data[labels == valid_labels[i]]
            farthest_distance_i = np.max(euclidean_distances(cluster_i_points, [center_i]))
            max_distance = max(max_distance, farthest_distance_i)

            for j, center_j in enumerate(centroids):
                if i == j:
                    continue
                cluster_j_points = Data[labels == valid_labels[j]]
                farthest_distance_j = np.max(euclidean_distances(cluster_j_points, [center_j]))
                distance_ij = np.linalg.norm(center_i - center_j)
                objective_function_ij = farthest_distance_i + 0.75 * distance_ij + farthest_distance_j
                objective_function = max(objective_function, objective_function_ij)

        # Plotting
        fig = Figure()
        canvas = FigureCanvas(fig)
        
        ax = fig.add_subplot(111)
        ax.scatter(*zip(*Data), c=labels, cmap='coolwarm')
        ax.scatter(*zip(*centroids), color='black', marker='*', s=100)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_title("Spectral Clustering")
        canvas.draw()

        current_scene = QGraphicsScene()
        current_scene.addWidget(canvas)
        self.Output_scene.append(current_scene)
        
 
    