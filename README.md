# Nassau-candy-factory-optimization
A Machine Learning-based Factory Reallocation and Shipping Optimization system that predicts shipping lead times, simulates alternative factory assignments, and recommends potential improvements for Nassau Candy Distributor.

# Factory Reallocation & Shipping Optimization System

## Project Overview

This project uses Machine Learning to analyze shipping lead times and identify potential factory reallocation opportunities for Nassau Candy Distributor.

The system predicts shipping lead times, compares alternative factory assignments, and generates recommendations to support operational decision-making.

## Objectives

* Analyze historical shipping data.
* Predict shipping lead times using Machine Learning.
* Compare Linear Regression, Random Forest, and Gradient Boosting models.
* Simulate alternative factory assignments.
* Identify potential lead-time improvements.
* Analyze product profitability to support business prioritization.

## Dataset

The dataset contains 10,194 records with product details, factory assignments, shipping information, dates, sales, costs, and gross profit.

## Tools & Technologies

* Python
* Pandas and NumPy
* Scikit-learn
* Matplotlib and Seaborn
* Google Colab
* GitHub

## Machine Learning Models

Three regression models were evaluated:

1. Linear Regression
2. Random Forest Regressor
3. Gradient Boosting Regressor

## Model Evaluation

| Model             |   RMSE |    MAE | R² Score |
| ----------------- | -----: | -----: | -------: |
| Linear Regression | 182.45 | 181.43 |   0.5293 |
| Random Forest     | 192.37 | 172.72 |   0.4767 |
| Gradient Boosting | 181.65 | 179.94 |   0.5334 |

Gradient Boosting achieved the highest R² score and the lowest RMSE among the evaluated models.

## Key Findings

* Dataset records: 10,194.
* Average model-predicted improvement: 74.91 days (6.82%).
* Potential actual factory reallocation opportunities identified by the scenario analysis: 11.
* Risk classification: 6 low-risk, 3 medium-risk, and 2 high-risk recommendations.

## Business Value

The analysis provides a structured way to compare factory assignment scenarios and identify products for further operational review. Historical gross profit was used as a business-priority indicator.

## Limitations

Alternative product-factory combinations were not represented in the historical data. Therefore, scenario results are model-based estimates, not confirmed real-world improvements.

Order year was the dominant model feature, indicating that the model may be capturing temporal patterns in the dataset. Further validation is required before using recommendations for actual factory reassignment.

Direct profit impact could not be measured from the available data.

## Conclusion

This project demonstrates how Machine Learning and scenario analysis can support shipping optimization decisions by identifying potential factory reallocation opportunities and estimating lead-time changes.

**Project Status:** Machine Learning analysis and scenario simulation completed.
