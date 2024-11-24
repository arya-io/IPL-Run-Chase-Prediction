# A Machine Learning Approach for Run Chase Prediction in IPL

This project utilizes a machine learning model to predict the win/loss outcome of the batting team in the second innings of IPL matches, based on historical data from IPL seasons 2008 to 2023.

### Dataset
The data used for this project was obtained from a public dataset available on Kaggle, titled [IPL 2008 to 2023 dataset](https://www.kaggle.com/datasets), contributed by user **Sri tata**. The dataset is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license. We acknowledge **Sri tata** and further recognize **cricsheet.com** as a potential source of the raw data based on the contributor's note.

### Model Overview
Two machine learning models were developed for this project:
- **Random Forest Classifier**: Achieved an accuracy of **99.87%**.
- **Logistic Regression**: Achieved an accuracy of **80.38%**.

The models predict the win/loss probability for the batting team during the run chase in the second innings of IPL matches. After analysis, we selected **Logistic Regression** as the final model due to its ability to provide probability percentages with more engaging and interpretable figures for users, especially cricket fans. The **Random Forest** model, while accurate, produced more extreme predictions.

---

### Visualization and Results

#### 1. Working of Algorithm with Pipeline
*Fig. 1*: Illustration of the end-to-end algorithm pipeline used in the project.

#### 2. Over by Over Win and Lose Probability for Chase Team
*Fig. 2*: Visualization of the win/lose probabilities for the chasing team on an over-by-over basis.

#### 3. Visual Representation of Over by Over Data Using Random Forest Algorithm
*Fig. 3*: Graphical representation of the Random Forest model predictions for the chase scenario, over by over.

### Random Forest Model Visuals
Below are images representing the results and functioning of the **Random Forest Algorithm**:

![Random Forest Image 1](https://github.com/arya-io/IPL-Run-Chase-Prediction/assets/127336304/2de29bf8-da21-4d8c-8568-7fa397196cdd)
![Random Forest Image 2](https://github.com/arya-io/IPL-Run-Chase-Prediction/assets/127336304/e7427548-d82c-43ce-9ca3-4a06ee57f3ba)
![Random Forest Image 3](https://github.com/arya-io/IPL-Run-Chase-Prediction/assets/127336304/15bb35c8-8681-4877-8b5f-f7c320529615)

### Logistic Regression Model Visuals
Below are images representing the results and functioning of the **Logistic Regression Algorithm**:

![Logistic Regression Image 1](https://github.com/arya-io/IPL-Run-Chase-Prediction/assets/127336304/9b854477-92a6-43d6-8bdc-1e4b1fbdc763)
![Logistic Regression Image 2](https://github.com/arya-io/IPL-Run-Chase-Prediction/assets/127336304/52fd0db0-38a7-4a86-b616-6bf8f44fea40)
![Logistic Regression Image 3](https://github.com/arya-io/IPL-Run-Chase-Prediction/assets/127336304/f4cef24f-692f-4501-a375-4b534dba5fb8)

---

### Conclusion
Although the **Random Forest** model achieved higher accuracy, the **Logistic Regression** model was chosen as the final model due to its ability to present win/loss probabilities in a more interpretable manner, making it more engaging for cricket fans.

---

### Video Demonstration
A video demonstration of the project has been attached.

---

### License
This project is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)** license.
