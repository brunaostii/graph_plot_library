# Graph's Plot Library 
#### Author: Bruna Almeida Osti


<p> This library generates a figure through an adjacency matrix, this being only a plot, or counting on: 2, 3, 4 or 6 subplots in the same figure.</p>
You can import through the code below:


**from Graph import Adjacency**

First, we must send to the object the number of vertices we will use, as in the example below: <p>
**Object = Adjacency(qt_nodes)** </p>

The next step is to choose the amount of subplots in the figure, the library suports 1, 2, 3, 4, or 6 subplots in the same figure.Where, the signatures of the methods will always have the structure below: <p>
**Object.Plot_Graph1(adjacency_matrix, 'title')**</p>

<p>The only thing that changes is that in the signature of the method the number changes according to quantity.</p>
<p>Obs: The *title* it's not mandatory. For example, for the 2's plot:</p>

**Object.Plot_Graph2(adjacency_matrix1, adjacency_matrix2, 'title1', 'title2')**

FIGURES:
- 2's Plot:
![PLOT 2](https://github.com/brunaostii/Lib_Plot_Graph/blob/master/Px_pais2.png)

- 3's Plot:
![PLOT 3](https://github.com/brunaostii/Lib_Plot_Graph/blob/master/particoes_PX_pais5.png)
