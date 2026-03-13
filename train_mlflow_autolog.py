from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error


# Load dataset
data = load_diabetes()
X = data.data
y = data.target

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Models
models = {
    "LinearRegression": LinearRegression(),
    "RandomForest": RandomForestRegressor(n_estimators=100, random_state=42),
    "GradientBoosting": GradientBoostingRegressor(random_state=42),
}

best_mse = float("inf")
best_model = None
best_model_name = None

# Train and evaluate
for model_name, model in models.items():

    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    mse = mean_squared_error(y_test, preds)

    print(f"{model_name} MSE: {mse:.4f}")

    # Track best model
    if mse < best_mse:
        best_mse = mse
        best_model = model
        best_model_name = model_name


print("\nBEST MODEL")
print(f"Best Model: {best_model_name}")
print(f"Best MSE: {best_mse:.4f}")