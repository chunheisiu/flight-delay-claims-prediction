## Flight Delay Claims Prediction

### Introduction
The goal of this project is to predict the claim amount for flight delays, using a learning dataset with flight delay claims from Jan 2013 to Jul 2016.

Per the instructions, a higher amount of predicted claim, with the cap of $800, is assigned to high-risk flights to adequately compensate the risk and naturally screen out the high risk flights.
A lower amount of predicted claim, as low as 0, should be assigned to low-risk flights to increase the conversion for a low-risk customer to buy and expand the risk pool.
The optimization of the predictions should result in a very low aggregated absolute error between the expected and actual claims, meaning that the customers are not over or under-charged.

This project is the data scientist take-home technical assessment for GoodNotes and T1.

Part of the PyTorch model training code is adapted from a [notebook](https://github.com/yanneta/deep-learning-with-pytorch/blob/master/lesson2-tabular.ipynb) written by my professor Yannet Interian.
Other parts of the code is written by me.


### Environment Setup
This project is written in Python 3. You need to install Python first. Please follow the guide here for the Python installation steps for your OS: https://docs.python-guide.org/starting/installation

After installing Python, run `python --version` to verify that you have Python 3.7 or above installed.
Then, run `./create_venv.sh` to create a Python virtual environment and install the necessary packages used in this project.
Finally, run `source ./venv/bin/activate` to activate the virtual environment.

Note that you need to place the source `flight_delays_data.csv` file in the `/data` directory in order for the model training to function.


### Project Structure
- Both the EDA and modeling processes were done using Jupyter notebooks. They are located under the `/notebooks` directory.
- Model-related files such as the save models and helper files are located under the `/models` directory.
- The data files should be located under the `/data` directory.

To view and run the Jupyter notebooks, run `jupyter notebook` or `jupyter lab` and navigate to the `/notebooks` directory.

To run the prediction script, modify the variables under _Configure variables_ in the Model Prediction notebook and execute the notebook.


### Technical Choices
- Jupyter notebooks are used for EDA and modeling because notebooks allow easy editing and straightforward visualizations.
- PyTorch Neural Network is used as the model of choice because it is a technique that I have learned recently and would like to apply it to real-world scenarios.


### Trade-offs and Possible Improvements
- I have jumped straight to a neural network-based model without first experimenting with a linear or tree-based model. I could spend some time with those models and see if there are any improvements to the model performance.
- The model I have trained can only produce validation R-squared values at around 0.36, which is relatively low compare to the standard 0.8 or above.
- There are possibly other ways to store model files, but for the sake of time and easy sharing, I have saved them as individual files on disk.
- Although I have mentioned the possibility of imbalanced dataset in the EDA notebook, I never got around to implement an upsampling procedure during my model training process.
- It is possible to use Python scripts (.py) rather than Jupyter Notebooks, but the changes in Python scripts are more difficult to realize and to debug. 
- In the HKO Weather Data, there is a column of wind speed and wind direction but I did not include it in the list of features due to difficulties in parsing. Including that feature might improve model performance.
