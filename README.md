# Delaunay
Transform an input image thanks to Delaunay triangulation

## Execution
```
python3.5 delaunay.py FileName.png -k int [-o resultFileName]
```
This command computes the k + 16 triangulation of the given image and saves it in the result file.  The +16 is due to the addition of points on the border to avoid grey areas.

## Results
Here some results on the testing image :  

With k = 10  
![10](https://raw.githubusercontent.com/Jeanselme/Delaunay/master/Images/10.jpeg)  

With k = 100  
![100](https://raw.githubusercontent.com/Jeanselme/Delaunay/master/Images/100.jpeg)  

With k = 1000  
![1000](https://raw.githubusercontent.com/Jeanselme/Delaunay/master/Images/1000.jpeg)  

With k = 10000  
![10000](https://raw.githubusercontent.com/Jeanselme/Delaunay/master/Images/10000.jpeg)  

## Libraries
Needs numpy, scipy and sys. Compiled with python3.5
