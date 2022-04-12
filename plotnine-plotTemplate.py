from plotnine import *
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from math import log

    # Figure Properties
xScale, yScale = [0, 10], [150, 1500]

    # Load dataset
print("Enter CSV file path: ")
dataPath = input()
apex3Ddf = pd.read_csv(dataPath)
plotTitle = "DTMS Map"

    # Define Variables
x, y, z, xyRatio = list(apex3Ddf["m_z"]), list(apex3Ddf["mobility"]*0.16), list(apex3Ddf["area"]), list(apex3Ddf["m_z"]/apex3Ddf["mobility"])
xError, yError, zError = list(apex3Ddf["errMzPPM"]), list(apex3Ddf["errArea"]), list(apex3Ddf["errMobility"])
plotdf = pd.DataFrame(zip(x, y, z, xError, yError, zError), columns = ["m/z", "DT", "Area", "m/z Error", "DT Error", "Area Error"])

    # Plotnine points
cMapRange = np.log(z)
p9point = (
    ggplot(plotdf) 
    + geom_point(aes(x="m/z", y="DT", color = cMapRange, size = "Area", alpha=0.50))
    # + coord_flip()
    + labs(title = "Plot Title", x="m/z", y="DT (ms)")
)

    # Export and Save
print(p9point)
ggplot.save(p9point, plotTitle+".png")