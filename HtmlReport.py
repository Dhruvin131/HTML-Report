import os
import matplotlib.pyplot as plt
import mpld3
import plotly.graph_objs as go
from plotly.offline import plot
import codecs

html_data = """
                <html>
                    <head>
                        <title>My Html Report </title>
                    </head>
                    <body>
            """

if os.path.exists("FBreport.txt"):
    
    with open("FBreport.txt") as report_file:
        reportData = report_file.read()

    html_data += f"<div> {reportData} </div>"
     

else:
     html_data += f"<div> File Not Found </div>" 


# Matplotlib.Pyplot
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
html_fig = mpld3.fig_to_html(fig)
html_data += f"<div>{html_fig} </div>"


trace = go.Scatter(x=[1, 2, 3], y=[4, 5, 6])
data = [trace]
layout = go.Layout(title='My Plot')
fig = go.Figure(data=data, layout=layout)

html_fig = plot(fig, output_type='div')
html_data += f"<div> {html_fig} </div>"

html_data += "</body> </html>"

with open("Report.html","w", encoding='utf-8') as report:
    report.write(html_data)

