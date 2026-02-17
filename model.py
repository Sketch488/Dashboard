import pandas as pd
from sklearn.multioutput import MultiOutputRegressor
from xgboost import XGBRegressor

# Load and prepare
data = pd.read_excel("COVER Corporation.xlsx")
data["Date"] = pd.to_datetime(data["Date"])
data = data.sort_values("Date").reset_index(drop=True)
data["Days"] = (data["Date"] - data["Date"].min()).dt.days

# Lag
n_lags = 7

for i in range(1, n_lags + 1):
    data[f'lag_{i}'] = data['Close'].shift(i)
data.dropna(inplace=True)

# Features and multiple targets
X = data[["Days"] + [f'lag_{i}' for i in range(1, n_lags + 1)]]
target_cols = ["Open", "High", "Low", "Close", "Volume"]
Y = data[target_cols]

# Splits
split = int(len(data) * 0.8)

X_train = X[:split]
X_test = X[split:]

Y_train = Y[:split]
Y_test = Y[split:]

# Train
base_model = XGBRegressor(
    n_estimators=500,
    learning_rate=0.03,
    max_depth=5,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)
model = MultiOutputRegressor(base_model)
model.fit(X_train, Y_train)

# Predict 
preds = model.predict(X_test) 

for i, pred_row in enumerate(preds[:7], start=1):
    print(f"\nDay {i}")
    for col, val in zip(target_cols, pred_row):
        print(f"{col}: {val:.2f}")

