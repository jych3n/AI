# Employee Future Prediction with Stratified K-Fold

Fall 2021

Contributors: 

Jun Yan Chen, Batuhan Kir

## About the Project
---
1. Built on kaggle.com.
2. Dataset from https://www.kaggle.com/tejashvi14/employee-future-prediction.

## Purpose:
Apply classifiers and find the feature importances on the most accurate model.

### Classification Models used along with K-Fold Cross Validation:
1. Random Forest
2. Decision Tree
3. Gaussian Naive Bayes
4. Logistic Regression

## Getting Start
---
## Using Kaggle

### Direct Link: https://www.kaggle.com/batuhankir/employee-future-prediction-with-stratified-k-fold

### To Open on a New Notebook
1. Register and Log in to kaggle.com.
2. Click the "+" sign on the selection tab on the left side of the screen.
3. Create New Notebook.
4. When new notebook is created, selected File -> Upload Notebook.
5. Upload "employee-future-prediction-with-stratified-k-fold.ipynb", select private.
6. Open sidebar on the right side of the screen, click "Add data"
7. In "Search dataset", search "Employee Future Prediction" or upload "employee.csv", name the dataset "Employee".
8. Click "Run All" to run the program.

## Using Other Editors
### Required Packages:
* npm
>npm install matplotlib

>npm install seaborn

>npm install numpy

>npm install pandas

>npm install scikit-learn

### Change Dataset File Route
line 
>df = pd.read_csv("../input/employee-future-prediction/Employee.csv") 


## References
---

### Python References (Code Used):
* Sklearn Tutorial on Confusion Matrix
https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html

* StackOverflow Solution Applying Feature Importances on K-Fold Spliting
https://stackoverflow.com/questions/51798540/cross-validation-dataset-folds-for-random-forest-feature-importance

### Knowledge Reference (No Code Used):

* More complex and in-depth analysis on the same dataset to help understand the information:
https://www.kaggle.com/gaganmaahi224/11classification-algos-eda-queries-visualization#Visualisation-Related-to-Query-1