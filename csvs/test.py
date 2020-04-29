#!/usr/bin/env python
# coding: utf-8

# In[1]:


from stl.mesh import Mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

#get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Create a new plot
figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)


# In[4]:


path = "../Landmarks-Detection/Dataset/Pat1/POD_JR_9060K_Patella.stl"

# Read the STL using numpy-stl
mesh = Mesh.from_file(path)

# Plot the mesh


# In[5]:


axes.add_collection3d(mplot3d.art3d.Poly3DCollection(mesh.vectors))

# Auto scale to the mesh size
scale = mesh.points.flatten('F')
axes.auto_scale_xyz(scale, scale, scale)


# In[8]:


# Show the plot to the screen
pyplot.show();


# In[9]:


#import vtkplotlib as vpl


# In[10]:


# Plot the mesh
# vpl.mesh_plot(mesh)


# In[ ]:


# vpl.show()


# In[ ]:




