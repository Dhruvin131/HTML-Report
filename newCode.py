import plotly.graph_objs as go
from plotly.offline import plot
import os

# Create an empty HTML file
with open('example.html', 'w') as f:
    pass

# Define the HTML and CSS code
html = """
<!DOCTYPE html>
<html>
<head>
<style>
.container {
    display: flex;
}

.square {
    width: 50%;
    height: 400px;
    padding: 10px;
    border: 1px solid black;
    overflow: auto;
    resize: none;
}

#text {
    height: 400px;
    overflow: auto;
}

</style>
  <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>

<div class="container">
  <div class="square" id="text"></div>
  <div class="square" id="plot"></div>
  <button onclick="loadFile()">Load Report File</button>
  <button onclick="HeavyloadFile()">Load Heavy Report File</button>
</div>

<script>
// Load text file content into the first square
function loadFile(){
    document.getElementById("text").innerHTML = `""" + open(r"D:\RiverEdge\Py\html-mht\fbreport.txt").read().replace('\n', '<br>') + """`;
}
function HeavyloadFile(){
    document.getElementById("text").innerHTML = `""" + open(r"D:\RiverEdge\Py\html-mht\sample1.txt").read().replace('\n', '<br>') + """`;
}

// Generate Plotly plot and display in the second square
var trace = {
  x: [1, 2, 3],
  y: [4, 5, 6],
  type: 'scatter'
};
var data = [trace];
var layout = {
  title: 'My Plot'
};
var fig = {data: data, layout: layout};
Plotly.newPlot('plot', fig);
</script>

</body>
</html>
"""

# Write the HTML and CSS code to the file
with open('example.html', 'w') as f:
    f.write(html)
