# Delaunay
Transform an input image thanks to Delaunay triangulation

## Execution
```
python3.5 delaunay.py FileName.png -k int [-o resultFileName]
```
This command computes the k + 16 triangulation of the given image and saves it in the result file.  The +16 is due to the addition of points on the border to avoid grey areas.

## Results
Here some results on the testing image :  

With k = 5  
![5-5](https://raw.githubusercontent.com/Jeanselme/Delaunay/master/Images/10.png)  

With k = 10  
![10-10](https://raw.githubusercontent.com/Jeanselme/Delaunay/master/Images/100.png)  

With k = 50  
![50-50](https://raw.githubusercontent.com/Jeanselme/Delaunay/master/Images/1000.png)  

With k = 100  
![100-100](https://raw.githubusercontent.com/Jeanselme/Delaunay/master/Images/10000.png)  

## Libraries
Needs numpy, scipy and sys. Compiled with python3.5
