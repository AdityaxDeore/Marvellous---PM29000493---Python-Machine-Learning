# Assignment 47 — Regression: Coefficients and Linear Regression

## Q1. What does a coefficient represent in regression? Give a real-life example.

A coefficient is the number that multiplies an input feature in a regression equation. It tells us how much the output (target) changes when that feature increases by one unit, while all other features stay constant. In simple terms, it measures the strength and direction of the relationship between the feature and the output: a positive coefficient means the output increases as the feature increases; a negative one means the output decreases.

Example: In the equation `ElectricityBill = 5 × UnitsConsumed + 100`, the coefficient 5 means every extra unit of electricity consumed raises the bill by Rs 5 (direction: positive; magnitude: 5 per unit).

## Q2. For Y = 8X + 15, identify the coefficient and the intercept. What does the coefficient tell us about the X–Y relationship?

- Coefficient = 8 (the number multiplying X)
- Intercept = 15 (the constant term, the value of Y when X = 0)

The coefficient 8 tells us that for every one-unit increase in X, Y increases by 8 units. The relationship is positive and linear — X and Y move in the same direction, and the change is constant (8 per unit of X).

## Q3. Marks = 6 × StudyHours + 40. Explain the coefficient 6 and the intercept 40. What happens if study hours increase by 2?

- Coefficient 6: for every additional hour studied, the predicted marks increase by 6.
- Intercept 40: the predicted marks when study hours = 0, i.e. the baseline score before any study.
- If study hours increase by 2 hours, predicted marks increase by 6 × 2 = 12 marks.

## Q4. Salary = 12 × Experience + 25. Calculate predicted salary for 2, 5 and 7 years of experience.

Substituting into Salary = 12 × Experience + 25:

- Experience = 2: Salary = 12 × 2 + 25 = 24 + 25 = 49
- Experience = 5: Salary = 12 × 5 + 25 = 60 + 25 = 85
- Experience = 7: Salary = 12 × 7 + 25 = 84 + 25 = 109

Predicted salaries: 49, 85 and 109 (in the salary's units, e.g. thousands).

## Q5. Y = −3X + 20. What does the negative coefficient indicate? What happens to Y when X increases by 1? Find Y when X = 4.

- The negative coefficient (−3) indicates an inverse (negative) relationship: as X increases, Y decreases.
- When X increases by 1, Y decreases by 3 (change in Y = −3 × 1 = −3).
- When X = 4: Y = −3 × 4 + 20 = −12 + 20 = 8.

## Q6. Price = 3000 × Size + 40000 × Bedrooms + 150000. Explain the meaning of the Size and Bedrooms coefficients. Which feature has a larger impact on the house price?

- Coefficient of Size (3000): each extra unit of size (e.g. each square foot) raises the predicted price by 3000.
- Coefficient of Bedrooms (40000): each additional bedroom raises the predicted price by 40000, keeping size constant.
- Intercept 150000: the base price of a (hypothetical) house with zero size and zero bedrooms — the starting price before features add value.

Which feature has a larger impact? Per unit, Bedrooms (40000) is far larger than Size (3000). But impact in practice also depends on how much each feature typically varies: Size can vary by hundreds of square feet (so its total contribution can dominate), while Bedrooms varies by only a few units. Comparing coefficients directly is only meaningful if the features are on comparable scales; with different units, the per-unit coefficient alone does not decide overall impact.

## Q10. Why are coefficients important in regression models? How do they help in understanding feature impact?

Coefficients are important because they turn the model from a black box into an interpretable explanation of how each input drives the prediction:

1. Direction: the sign (+/−) tells whether a feature increases or decreases the output.
2. Magnitude: the value tells how sensitive the output is to a one-unit change in that feature.
3. Comparison: coefficients reveal which features matter most (after accounting for scale, e.g. via standardization), guiding feature selection and business decisions — for example, whether improving one factor is worth more than another.
4. Actionability: they quantify trade-offs, e.g. "one more study hour is worth 6 extra marks", which supports planning and decision-making.
