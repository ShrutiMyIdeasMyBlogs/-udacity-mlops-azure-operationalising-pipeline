# Operationalizing Machine Learning Project-2
This project can be divided into two parts:
1. First section involves the model creation for the banking marketing data.It uses the AutoML functionality of Azure Machine learning i.e no/low code platform.
2. In the second part of the project, the python SDK has be used for pipeline creation for model training on the same dataset which has been used in part1.

Once the model is trained,the model has been deployed in the form of rest API so that it can be consumed from anywhare.


## Architectural Diagram
![image](https://user-images.githubusercontent.com/16042155/203629277-800eba74-c105-482b-90d4-05c8d38dd545.png)


## Key Steps
1. Performing Authentication:This has been done using the azure cli and defining the role as owner in Azure Active Directory. 
2. Running Automated ML Experiment:The experiment has been created and ran succesfully using automl.The following step has been performed:
  a)Reading and registering the dataset:The data that will be used in the project has been loaded and registered The screenshot is attached for the same.  
  ![reading_bankingdata](https://user-images.githubusercontent.com/16042155/203637037-e9883751-02c2-4937-a9bc-057ef326ffc8.png)
  b)Experiment Run and Completition
  The below image shows the automl-experiment creation,the later image depicts the completition of the experiment
  ![Experiment_run](https://user-images.githubusercontent.com/16042155/203637601-97e6a7d7-9318-482b-b973-89ad9b61b98f.png)
  ![image](https://user-images.githubusercontent.com/16042155/203715354-0966f01f-55a0-40ce-a75f-d7f4a70ac2b8.png)
  c)Best Model Selection
  The model with the best desired metric has been selected for the deployment
  ![image](https://user-images.githubusercontent.com/16042155/203716309-8f7ab323-f48b-4439-86da-6bd038b021a3.png)
  d) Model Deployment
  In the below image,the best model has been deployed successfully
  ![image](https://user-images.githubusercontent.com/16042155/203716006-1b97d70d-b0d3-402d-b86e-9ee263072172.png)
  e)Model Consumption
  The model is ready for the consumption and rest api can be used for the same
  ![image](https://user-images.githubusercontent.com/16042155/203716232-6e08b3b0-9dc2-45e8-86a3-de25def8bb39.png)
Additional steps like swagger usage,enabling application insights and performance benchmark have also been done.These steps directly donot impact the model development but these can be greatly useful as a supporting steps that enable better model development.
swagger.sh running on local
![swagger_display1](https://user-images.githubusercontent.com/16042155/203639093-a2a0ecfd-99a6-495f-89b7-67c1259faab9.png)
benchmarking.sh output
![image](https://user-images.githubusercontent.com/16042155/203716452-000da819-aee8-4bda-ab65-66246526e4fd.png)
application insight is true
![image](https://user-images.githubusercontent.com/16042155/203716807-9d5ad737-665d-4e0c-a0a1-2b83e0d396bf.png)


## Screen Recording
The screencast is available at https://youtu.be/dQfkEdrFmdM

## Future Work
Following points can be implemented for future work.
1. The project can include the hyperparameter tunning in python.
2. Feature engineering can also be done in the project.
3. It can be further elaborated to the full stack development,where the model rest end point are consumed from the UI.
4. Test a local container with a downloaded model


