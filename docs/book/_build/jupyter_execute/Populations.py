# Populations

In calculating over weighted survey microdata, we use the Family Resources Survey. This isn't redistributable, but is available to academics. We use the package ```frs``` to convert the source TAB files into OpenFisca-compatible CSV files.

## Prerequisite: install and initialise ```frs```

First, install and initialise the package ```frs``` (via ```pip install frs```):

!frs status

## Using ```PopulationSim```

The helper class ```PopulationSim``` uses the FRS package to load the input data:

from openfisca_uk import PopulationSim

sim = PopulationSim()

This helper class contains an OpenFisca Simulation object in ```sim.model```; the ```PopulationSim``` class provides some functions such as mapping between entity types, effective marginal tax rate calculation and DataFrame generation.

For example, we can generate a DataFrame containing all the variables for the ```person``` entity:

import pandas as pd
person_df = sim.entity_df(entity="person")
person_df.describe()

