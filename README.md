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
  a)Reading and registering the dataset
  ![reading_bankingdata](https://user-images.githubusercontent.com/16042155/203637037-e9883751-02c2-4937-a9bc-057ef326ffc8.png)
  b)Experiment Run and Completition
  ![Experiment_run](https://user-images.githubusercontent.com/16042155/203637601-97e6a7d7-9318-482b-b973-89ad9b61b98f.png)
  c)Best Model Selection
  <img width="861" alt="s2_deploy_model" src="https://user-images.githubusercontent.com/16042155/203637934-35cf5f25-dde8-4e2e-96b5-d03ab87dc11b.PNG">
  d) Model Deployment
  <img width="863" alt="s5_model_deployed_successfully" src="https://user-images.githubusercontent.com/16042155/203638049-89cf3864-b498-4ecf-9f64-b5470efc501e.PNG">
  e)Model Consumption
  <img width="690" alt="s7_model_consumption_credentials_authentication" src="https://user-images.githubusercontent.com/16042155/203638304-c31edf4a-2aa8-4d65-b858-094a16b43978.PNG">
Additional steps like swagger usage,enabling application insights and performance benchmark have also been done.These steps directly donot impact the model development but these can be greatly useful as a supporting steps that enable better model development.
![swagger_display1](https://user-images.githubusercontent.com/16042155/203639093-a2a0ecfd-99a6-495f-89b7-67c1259faab9.png)
<img width="443" alt="benchmark5" src="https://user-images.githubusercontent.com/16042155/203639129-75cbb2c6-e0b0-4ba1-ad7e-1748886ee052.PNG">
<img width="602" alt="s10_application_insight_true" src="https://user-images.githubusercontent.com/16042155/203639048-94f4d028-c327-47a6-973d-4804f38344c4.PNG">

## Screen Recording
The screencast is available at https://youtu.be/dQfkEdrFmdM

## Future Work
Following points can be implemented for future work.
1. The project can include the hyperparameter tunning in python.
2. Feature engineering can also be done in the project.
3. It can be further elaborated to the full stack development,where the model rest end point are consumed from the UI.
4. Test a local container with a downloaded model


