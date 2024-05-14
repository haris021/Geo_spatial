#!/usr/bin/env python
# coding: utf-8

# In[8]:


import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
from matplotlib_scalebar.scalebar import ScaleBar
from shapely.geometry import Point  


# In[9]:


cd D:\medium\geo_spatial


# In[10]:


from pyproj import Proj, transform

# This function converts from epsg 4362 to 3857

def convert(lon, lat):
    P3857 = Proj(init='epsg:3857')
    P4326 = Proj(init='epsg:4326')
    x,y = transform(P4326, P3857, lon, lat)
    return (x,y)


# In[11]:


shapefile = gpd.read_file("E:\hybas_lake_as_lev04_v1c\hybas_lake_as_lev04_v1c.shp").to_crs(epsg=3857)

# the HYBAS id for indus and kabul
required_ids = [4040648310, 4040648320]

Kabul_shapefile = shapefile.loc[shapefile.HYBAS_ID == required_ids[0]]
Indus_shapefile = shapefile.loc[shapefile.HYBAS_ID == required_ids[1]]


# In[12]:


fig, ax = plt.subplots(figsize=(12, 8), dpi=200)

Kabul_shapefile.plot(ax=ax, alpha=0.3, color='slateblue')
Kabul_shapefile.boundary.plot(ax=ax, color='slateblue', linewidth=2, label='Kabul')

Indus_shapefile.plot(ax=ax, alpha=0.3, color='m')
Indus_shapefile.boundary.plot(ax=ax, color='m', linewidth=2, label='Indus')

ctx.add_basemap(ax)

scale_bar = ScaleBar(1.0, units="m", location="lower left")
fig.gca().add_artist(scale_bar)


# The text for the annotation
bbox = dict(boxstyle="round", fc='white')


# Nowshera coordinates (72, 34)
Nowshera_coordinates = convert(72, 34)
Nowshera_point = Point(Nowshera_coordinates[0], Nowshera_coordinates[1])
Nowshera_gpd = gpd.GeoDataFrame({'Name': ['Nowshera'], 'geometry': [Nowshera_point]})

Nowshera_gpd.apply(lambda x: ax.annotate(text=x.Name, xy=x.geometry.centroid.coords[0], ha='center', fontsize=8, xytext = (10,25), textcoords='offset pixels',color='k', bbox=bbox),axis=1)
Nowshera_gpd.plot(ax=ax, color='k', marker = '^', markersize=120, zorder=2)

# Tarbela coordinates (72.8050,34.16)
Tarbela_coordinates = convert(72.8050,34.16)
Tarbela_point = Point(Tarbela_coordinates[0], Tarbela_coordinates[1])
Tarbela_gpd = gpd.GeoDataFrame({'Name': ['Tarbela'], 'geometry': [Tarbela_point]})

Tarbela_gpd.apply(lambda x: ax.annotate(text=x.Name, xy=x.geometry.centroid.coords[0], ha='center', fontsize=8, xytext = (10,25), textcoords='offset pixels',color='k', bbox=bbox),axis=1)
Tarbela_gpd.plot(ax=ax, color='k', marker = '^', markersize=120, zorder=2)

ax.legend(fontsize=14)
plt.savefig('study_area.pdf', bbox_inches='tight')
plt.show()


# In[ ]:




