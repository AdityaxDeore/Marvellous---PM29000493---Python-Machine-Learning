from sklearn.linear_model import LinearRegression

X = [[1, 7], [2, 6], [3, 7], [4, 6], [5, 8]]
marks = [50, 55, 60, 65, 70]

model = LinearRegression()
model.fit(X, marks)

print("Coefficient (StudyHours):", model.coef_[0])
print("Coefficient (SleepHours):", model.coef_[1])
print("Intercept:", model.intercept_)
