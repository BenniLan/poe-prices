# Path of Exile Currency Price Prediction

Can the future price of in-game currency in Path of Exile be predicted from
its past prices? This project compares simple time-series models against a
naive baseline, using historical league data, and collects fresh hourly data
from the current league for further training.

> Work in progress

## Approach

- **Data:** historical currency prices from previous leagues, from
  [poe.ninja](https://poe.ninja/poe1/data) <
- **Models:**
  - Naive baseline: the next price equals the current price
  - AR(1) model: the next price depends linearly on the previous one
  - One-variable linear rule 
- **Analysis:** Spearman rank correlation to measure how strongly past and
  future price movements are related

## Results so far

The models showed a slight edge over the naive baseline at league start.

Big issue is that things learned from one league dont apply well to the other because of patchnotes

Beating a naive baseline is hard for price data, since in a liquid market the
current price already carries most of the available information. A small but
consistent edge is a meaningful result, but more data is needed to confirm it.

## Ongoing: data collection for league 3.30

To test whether the edge holds up, this repo collects **hourly** price data
from the current league. 
## Next steps

- Retrain and evaluate the models on the new hourly data
- Compare models trained on old leagues against the new league


## Tech stack

Python · Jupyter · pandas · numpy 
## Use of AI
Used to write the code to allow quick testing of diffrent models
Helped setting up the data collector
Helped writing the README
