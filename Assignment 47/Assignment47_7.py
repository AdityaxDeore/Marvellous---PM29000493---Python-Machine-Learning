from sklearn.linear_model import LinearRegression

study_hours = [[1], [2], [3], [4], [5]]
marks = [50, 55, 60, 65, 70]

model = LinearRegression()
model.fit(study_hours, marks)

print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)
