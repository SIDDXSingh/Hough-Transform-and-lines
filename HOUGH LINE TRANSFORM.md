# HOUGH LINE TRANSFORM
* **This algorithm is used to detect lines in the image** 
* **This code implements hough line from scratch by numpy module, OpenCV and python**
the procedure is as follows:
### GRADIENT DETECTION
* Edge pixels are determined using ```np.gradient``` and the image is thresholded to convert it into binary form.
* Separate arrays for x-gradient,y-gradient are defined for further calculation.
* This avoids unnecesary iterations to occur as we deal only with the strong edge pixels and not with the whole image.

### THE HOUGH SPACE
* We know that equation of a line is y=mx+c. If m and c are defined then we can have infinte points on the line, and can plot it. 
* On the other hand if we are provided with a specific point then we can pass infinite lines through it.
* So for a certain slope we need a certain intercept to fulfill the condition, given we have the point fixed.
* If we plot m and c on y and x axes respectively then we will get a line having the equation m=(-c/x)+y/x.
* This space is called the "Hough space". Every line would have some certain equation if we consider a point on the image as the origin and proceed further.

### THE NORMAL EQUATION
* Now to identify a line we need to fetch the data of each bright pixel obtained after thresholding.
* Each pixel will represent a line in the hough space. So if we have 'n' lines if we have 'n' pixels.
* These lines would produce some intersection points and by them we can identify if those accessed set of points belong to a line or not.
* The difference is instead of using the slope-intercept form we use the normal equation ```D=(x*cos(theta))+(y*sin(theta))``` and do the necessary calculations to fetch enough data of a pixel to wide range of values of 'd' that is distance of line from the origin.
* As we have two parametres 'd' and 'theta' we choose a range of thetas with equal difference between them and hence calculate corresponding 'd' values and store them in a two 2-D array.
* For each pixel we have the set of both the parametres. What we need to find is the intersection of all these lines.

### HOUGH ACCUMALTOR ARRAY
* We define couple of 1-D array for 'D' and 'theta', the size of arrays is the no. of bins we want and they are asigned with the 'D' and 'theta' values evenly.
* Now we convert the values of the D and theta into their bin numbers with the formula ```(x*(no.of bins))/x_max``` where x is the variable.
* This results in 2 2-D arrays with the bin numbers alloted w.r.t to the values in it.
* Both these arrays are flatten to make 1-D arrays and are iterated to fetch couple of numbers from their respective indices at a time.
* A 2-D hough accumalator array having the shape of these two bin numbers is incremented as the iteration hit a certain position of that array.
* A threshold value is set up so as to avoid arbitrary lines getting detected.
* Another feature of minimum distance required is demanded by the code from the user.
* The values of D having difference less than the required value are omitted.

### DRAWING THE LINES 
* Now we know the indices of the point where intersection is maximum which is the bin number of corresponding parametres.
* After recognizing such points we calculate the values required to draw on the image.
* From the obtained values of parametres we acquire the intercepts and use the ```cv.line``` drawing function by feeding both the intercepts resulting in the ouput image.

NOTE: **The top left corner of the image is considered as origin and hence the image is in 4th quadrant. Assuming 'D' vary from +d to -d where d is the length of the diagonal of the image with theta restricting from -90 to +90** 
