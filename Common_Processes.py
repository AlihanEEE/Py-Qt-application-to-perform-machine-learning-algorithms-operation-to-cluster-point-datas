# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 19:07:32 2023

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

np.random.seed(0)

class Common_Proc():
    
    def __init__(self):
        """
        This constructor contains the all attributes for the project

        Returns
        -------
        None.

        """
        self.text_data = []
        
        self.clusterFromUser = 8
        self.initFromUser = 'k-means++'
        self.maxIterFromUser = 300
        self.algorithmFromUser = 'auto'
        self.Input_scene = None
        self.Output_scene = []
        
        self.next_scene = []
        
    def set_next_scene(self,data):
        """
        This function sets the next_scene attribute 

        Parameters
        ----------
        data : data for assign to next_scene attribute

        Returns
        -------
        None.

        """
        self.next_scene = data
        
    def get_next_scene(self):
        """
        This function returns the next_scene attribute 

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return self.next_scene
    
    def set_text_data(self,data):
        """
        This function sets the text_data attribute 

        Parameters
        ----------
        data : data for assign to text_data attribute

        Returns
        -------
        None.

        """
        
        self.text_data = data
        
    def get_text_data(self):
        """
        This function returns the text_data attribute 

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return self.text_data

    def set_pointsFromUser(self,data):
        """
        This function sets the pointsFromUser attribute 

        Parameters
        ----------
        data : data for assign to pointsFromUser attribute

        Returns
        -------
        None.

        """
        self.pointsFromUser = data
        
    def get_pointsFromUser(self):
        """
        This function returns the pointsFromUser attribute 

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return self.pointsFromUser
    
    def set_initFromUser(self,data):
        """
        This function sets the initFromUser attribute 

        Parameters
        ----------
        data : data for assign to initFromUser attribute

        Returns
        -------
        None.

        """
        self.initFromUser = data
        
    def get_initFromUser(self):
        """
        This function returns the initFromUser attribute 

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return self.initFromUser
    
    def set_clusterFromUser(self,data):
        """
        This function sets the clusterFromUser attribute 

        Parameters
        ----------
        data : data for assign to clusterFromUser attribute

        Returns
        -------
        None.

        """
        self.clusterFromUser = data
        
    def get_clusterFromUser(self):
        """
        This function returns the clusterFromUser attribute 

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return self.clusterFromUser
    
    def set_maxIterFromUser(self,data):
        """
        This function sets the maxIterFromUser attribute 

        Parameters
        ----------
        data : data for assign to maxIterFromUser attribute

        Returns
        -------
        None.

        """
        self.maxIterFromUser = data
        
    def get_maxIterFromUser(self):
        """
        This function returns the maxIterFromUser attribute 

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return self.maxIterFromUser
    
    def set_algorithmFromUser(self,data):
        """
        This function sets the algorithmFromUser attribute 

        Parameters
        ----------
        data : data for assign to algorithmFromUser attribute

        Returns
        -------
        None.

        """
        self.algorithmFromUser = data
        
    def get_algorithmFromUser(self):
        """
        This function returns the algorithmFromUser attribute 

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return self.algorithmFromUser
    
    def set_initialSolution(self,data):
        """
        This function sets the initialSolution attribute 

        Parameters
        ----------
        data : data for assign to initialSolution attribute

        Returns
        -------
        None.

        """
        self.initialSolution = data
    
    def get_initialSolution(self):
        """
        This function returns the initialSolution attribute 

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return self.initialSolution
    
    def Open_File_Read_Text(self):
        """
        This method opens the searchig file window,The selected file assigned the text_data attribute.  The selected file must be *txt extensions

        Returns
        -------
        None.

        """
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Text Files (*.txt)")
        file_dialog.setWindowTitle("Open the Data")
        if file_dialog.exec():
            
            selected_file = file_dialog.selectedFiles()[0] 
            with open(selected_file, 'r') as file:
                for lines in file:
                    coordinates=lines.split()
                    x= float(coordinates[0])
                    y= float(coordinates[1])
                    self.text_data.append((x,y))
                print("after append:",self.text_data)
                
        self.Enable_After_Input()
        self.Show_Input()
        
        
        
    def Show_Input(self):
        """
        This method Shows raw text_data data on the Inıtıal Solution screen

        Returns
        -------
        None.

        """
    
        
        fig = Figure()
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        ax.scatter(*zip(*self.get_text_data()), color="black") 
        ax.set_title("{} dot".format(str(len(self.get_text_data()))))

        canvas.draw()
        
        self.Input_scene = QGraphicsScene()
        self.Input_scene.addWidget(canvas)
        
        print(type(self.Input_scene))
        
        self.init = self.label_Initial_Solution.setScene(self.Input_scene)
           
 
    
    def Show_Output(self):
        """
        This method Shows the manipulated text_data data on the Final Solution screen

        Returns
        -------
        None.

        """
        self.Enable_Saving_Funcs_Output()

          
        if self.Output_scene:
            self.pushButton_Final_Undo.setEnabled(True)
            self.action_Undo_Final_Solution.setEnabled(True)
            self.pushButton_Final_Clear.setEnabled(True)
            self.action_Clear_Final_Solution.setEnabled(True)
            print(type(self.Output_scene[-1]))
            self.label_Final_Solution.setScene(self.Output_scene[-1])
            

        else:
           
            self.Disable_Saving_Funcs_Output()
       
        
       
        
    def clearInput(self):
        """
        This method Clears the Initial Solution screen and Final Solution screen

        Returns
        -------
        None.

        """
        self.label_Initial_Solution.scene().clear()
        self.label_Final_Solution.scene().clear()
        
        self.Output_scene = []
        self.next_scene = []
        self.Input_scene = []
        
        self.Disable_After_Clear_Input()
        
        
    def clearFinal(self):
        """
        This method Clears Final Solution screen

        Returns
        -------
        None.

        """
        
        self.label_Final_Solution.scene().clear()

        self.Output_scene = []
        self.next_scene = []

        
        self.Disable_After_clear_output()
        
        
        
        
    def undoFinalFunction(self):
        """
        This method show the previous output on the screen if there is no previous output, the action and button of the undo are set disabled

        Returns
        -------
        None.

        """
        
        
        self.pushButton_Final_Redo.setEnabled(True)
        self.action_Redo_Final_Solution.setEnabled(True)
        
        temp = self.Output_scene.pop()
        self.next_scene.append(temp)
        
        
        if self.Output_scene:
            pass
            
        else:
            self.pushButton_Final_Undo.setEnabled(False)
            self.action_Undo_Final_Solution.setEnabled(False)
            self.label_Final_Solution.scene().clear()
            
        
    def redoFinalFunction(self):
        """
        This method is Redo method. Redo button or action becomes available when the undo button or action are executed . It shows the next output on the screen if there is no next output, the action and button of the redo are set disabled

        Returns
        -------
        None.

        """
        
        temp = self.next_scene.pop()
        self.Output_scene.append(temp)
        
        if self.next_scene:
            pass
            
        else:
            self.pushButton_Final_Redo.setEnabled(False)
            self.action_Redo_Final_Solution.setEnabled(False)
        
        

    
    
    def closeApplication(self):
        """
        When the exit action triggered closing pop up screen appears

        Returns
        -------
        None.

        """
        reply = QMessageBox.question(
            None, "Message",
            "Are you sure to quit?",
            QMessageBox.Yes | QMessageBox.No,QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            QApplication.quit()
        
    
    
    def Enable_After_Input(self):
        """
        This method enables the necessery buttons and actions on the screen when File selection executed

        Returns
        -------
        None.

        """
        self.pushButton_Initial_Save.setEnabled(True)
        self.pushButton_Initial_Export_As.setEnabled(True)
        self.pushButton_Initial_Clear.setEnabled(True)
        self.pushButton_Cluster_K_Means.setEnabled(True)
        self.pushButton_Cluster_Affinity_Propagation.setEnabled(True)
        self.pushButton_Cluster_Mean_Shift.setEnabled(True)
        self.pushButton__Cluster_Spectral_Clustering.setEnabled(True)
        self.pushButton__Cluster_Hierarchical_Clustering.setEnabled(True)
        self.pushButton__Cluster_DBSCAN.setEnabled(True)
        self.pushButton_Heuristic_Hill_Climbing.setEnabled(True)
        self.pushButton_Heuristic_Simulated_Anneling.setEnabled(True)
        self.action_Save_Initial_Solution.setEnabled(True)
        self.action_Save_Final_Solution.setEnabled(True)
        self.action_Export_As_Initial_Solution.setEnabled(True)
        self.action_Export_As_Final_Solution.setEnabled(True)
        self.action_Clear_Initial_Solution.setEnabled(True)
        self.action_Clear_Final_Solution.setEnabled(True)
        self.action_Clustering_K_Means.setEnabled(True)
        self.action_Clustering_Affinity_Propaganation.setEnabled(True)
        self.action_Clustering_Mean_Shift.setEnabled(True)
        self.action_Clustering_Spectral_Clustering.setEnabled(True)
        self.action_Clustering_Hierarchical_Clustering.setEnabled(True)
        self.action_Clustering_DBSCAN.setEnabled(True)
        self.action_Heuristic_Hill_Climbing.setEnabled(True)
        self.action_Heuristic_Simulated_Anneling.setEnabled(True)
        self.action_Undo_Initial_Solution.setEnabled(True)
        self.action_Undo_Final_Solution.setEnabled(True)
        self.action_Redo_Initial_Solution.setEnabled(True)
        self.action_Redo_Final_Solution.setEnabled(True)
    
    
    def Disable_After_Clear_Input(self):
        """
        This method disables the necessery buttons and actions on the screen when Clean Input executed

        Returns
        -------
        None.

        """
        self.pushButton_Initial_Save.setEnabled(False)
        self.pushButton_Initial_Export_As.setEnabled(False)
        self.pushButton_Initial_Clear.setEnabled(False)
        self.pushButton_Initial_Undo.setEnabled(False)
        self.pushButton_Initial_Redo.setEnabled(False)
        self.pushButton_Final_Save.setEnabled(False)
        self.pushButton_Final_Export_As.setEnabled(False)
        self.pushButton_Final_Clear.setEnabled(False)
        self.pushButton_Final_Undo.setEnabled(False)
        self.pushButton_Final_Redo.setEnabled(False)
        self.pushButton_Cluster_K_Means.setEnabled(False)
        self.pushButton_Cluster_Affinity_Propagation.setEnabled(False)
        self.pushButton_Cluster_Mean_Shift.setEnabled(False)
        self.pushButton__Cluster_Spectral_Clustering.setEnabled(False)
        self.pushButton__Cluster_Hierarchical_Clustering.setEnabled(False)
        self.pushButton__Cluster_DBSCAN.setEnabled(False)
        self.pushButton_Heuristic_Hill_Climbing.setEnabled(False)
        self.pushButton_Heuristic_Simulated_Anneling.setEnabled(False)
        self.action_Save_Initial_Solution.setEnabled(False)
        self.action_Save_Final_Solution.setEnabled(False)
        self.action_Export_As_Initial_Solution.setEnabled(False)
        self.action_Export_As_Final_Solution.setEnabled(False)
        self.action_Clear_Initial_Solution.setEnabled(False)
        self.action_Clear_Final_Solution.setEnabled(False)
        self.action_Clustering_K_Means.setEnabled(False)
        self.action_Clustering_Affinity_Propaganation.setEnabled(False)
        self.action_Clustering_Mean_Shift.setEnabled(False)
        self.action_Clustering_Spectral_Clustering.setEnabled(False)
        self.action_Clustering_Hierarchical_Clustering.setEnabled(False)
        self.action_Clustering_DBSCAN.setEnabled(False)
        self.action_Heuristic_Hill_Climbing.setEnabled(False)
        self.action_Heuristic_Simulated_Anneling.setEnabled(False)
        self.action_Undo_Initial_Solution.setEnabled(False)
        self.action_Undo_Final_Solution.setEnabled(False)
        self.action_Redo_Initial_Solution.setEnabled(False)
        self.action_Redo_Final_Solution.setEnabled(False)
        
        
        
        
        
    
    def Disable_After_Clear_Output(self):
        """
        This method disables the necessery buttons and actions on the screen when there is no output image on the screen

        Returns
        -------
        None.

        """
        
        self.pushButton_Final_Save.setEnabled(False)
        self.pushButton_Final_Export_As.setEnabled(False)
        self.pushButton_Final_Clear.setEnabled(False)
        self.pushButton_Final_Undo.setEnabled(False)
        self.pushButton_Final_Redo.setEnabled(False)
        self.action_Undo_Final_Solution.setEnabled(False)
        self.action_Clear_Final_Solution.setEnabled(False)
        self.action_Redo_Final_Solution.setEnabled(False)
        
       
        
        
    def Enable_Saving_Funcs_Output(self):
        """
        This method enables the necessery buttons and actions on the screen when the output image occurs on the screen

        Returns
        -------
        None.

        """
        self.action_Export_As_Final_Solution.setEnabled(True)
        self.action_Save_Final_Solution.setEnabled(True)
        self.pushButton_Final_Export_As.setEnabled(True)
        self.pushButton_Final_Save.setEnabled(True)
        

    def Disable_Saving_Funcs_Output(self):
        """
        This method disables the necessery buttons and actions on the screen when there is no output image on the screen


        Returns
        -------
        None.

        """
        self.action_Export_As_Final_Solution.setEnabled(False)
        self.action_Save_Final_Solution.setEnabled(False)        
        self.pushButton_Final_Export_As.setEnabled(False)
        self.pushButton_Final_Save.setEnabled(False)
        
        
        
        
        
        