#!/bin/bash
mkdir -p data

kaggle datasets download -d gabrielluizone/us-domestic-flights-delay-prediction-2013-2018 -p data --unzip

# keep only years you want
find data -type f ! -name "*2017*" ! -name "*2018*" -delete