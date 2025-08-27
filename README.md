# 📊 Professional GeoPandas Tutorial

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![GeoPandas](https://img.shields.io/badge/GeoPandas-0.13+-green.svg)](https://geopandas.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

This project presents a **complete and professional tutorial** on **GeoPandas**, a powerful Python library for geospatial data analysis.

## 🎯 About the Project

GeoPandas is a Pandas extension that adds support for geospatial data, allowing you to work with geographic information in an intuitive and efficient way. This tutorial was developed to demonstrate best practices and advanced features of the library.

## ✨ Features

- 🚀 **Professional Code**: Organized structure and well-documented code
- 📚 **Complete Tutorial**: From basic to advanced concepts
- 🗺️ **Professional Visualizations**: High-quality maps and charts
- 🔍 **Spatial Operations**: Practical demonstrations of functionalities
- 💾 **Multiple Formats**: Export in various file formats
- 🔧 **Best Practices**: Tips for professional use

## 📋 Prerequisites

- **Python 3.7+**
- **Basic knowledge of Pandas**
- **Familiarity with GIS concepts**
- **Python libraries** (installed automatically)

## 🚀 Installation and Usage

### 1. Clone the Repository

```bash
git clone https://github.com/joaoider/geopandas.git
cd geopandas
```

### 2. Run the Tutorial

```bash
python geopandas_tutorial.py
```

### 3. Or Run in Jupyter

```bash
jupyter notebook geopandas_tutorial.py
```

## 📁 Project Structure

```
geopandas/
├── geopandas_tutorial.py    # Main tutorial in Python
├── README.md               # This file
├── .gitignore             # Git ignored files
└── minicurso-geopandas/   # Additional directory (if exists)
```

## 🎓 What You'll Learn

### 📊 **Fundamentals**
- GeoPandas installation and configuration
- Geospatial data structure
- Coordinate reference systems (CRS)

### 🗺️ **Visualization**
- Professional map creation
- Chart customization
- Multiple visualizations in one layout

### 🔍 **Spatial Operations**
- Spatial filtering
- Distance calculations
- Buffer creation and influence areas
- Geospatial statistics

### 💾 **Data Export**
- GeoJSON (web-friendly)
- Shapefile (GIS standard)
- CSV with coordinates
- Parquet (efficient)

### 🔧 **Best Practices**
- Data validation
- Error handling
- Performance optimization
- Code documentation

## 📚 Code Examples

### Creating a GeoDataFrame

```python
import geopandas as gpd
from shapely.geometry import Point

# City coordinates
coordinates = [(-74.006, 40.7128), (-87.6298, 41.8781)]
geometries = [Point(lon, lat) for lon, lat in coordinates]

# City data
data = {
    'city': ['New York', 'Chicago'],
    'population': [8336817, 2693976]
}

# Creating GeoDataFrame
gdf = gpd.GeoDataFrame(data, geometry=geometries, crs='EPSG:4326')
```

### Professional Visualization

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1, figsize=(14, 10))

gdf.plot(
    column='population',
    ax=ax,
    cmap='viridis',
    legend=True,
    markersize=100,
    edgecolor='black'
)

ax.set_title('US Cities', fontsize=16, fontweight='bold')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.grid(True, alpha=0.3)

plt.show()
```

## 🛠️ Dependencies

The tutorial automatically installs the following libraries:

- **GeoPandas**: Geospatial analysis
- **Pandas**: Data manipulation
- **NumPy**: Numerical computation
- **Matplotlib**: Visualizations
- **Shapely**: Spatial geometries

## 📖 Additional Documentation

- [Official GeoPandas Documentation](https://geopandas.org/)
- [Examples and Tutorials](https://geopandas.org/examples/)
- [Community on GitHub](https://github.com/geopandas/geopandas)
- [Quick Start Guide](https://geopandas.org/getting_started.html)

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**AI Assistant** - Developed with ❤️ for the Python community

## 🙏 Acknowledgments

- GeoPandas community
- Project contributors
- Users who tested and provided feedback

## 📞 Support

If you encounter any issues or have questions:

- Open an [Issue](https://github.com/joaoider/geopandas/issues)
- Contact via email: your-email@example.com
- Participate in community discussions

---

⭐ **If this tutorial was helpful, consider giving the project a star!**

*Last updated: December 2024*