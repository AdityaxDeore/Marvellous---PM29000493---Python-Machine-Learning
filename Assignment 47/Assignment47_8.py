from sklearn.linear_model import LinearRegression

study_hours = [[1], [2], [3], [4], [5]]
marks = [50, 55, 60, 65, 70]

model = LinearRegression()
model.fit(study_hours, marks)

predicted = model.predict([[6]])
print("Predicted marks for 6 study hours:", predicted[0])
