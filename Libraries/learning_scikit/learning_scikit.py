from sklearn.datasets import load_diabetes as lb
from sklearn.neighbors import KNeighborsRegressor

x, y = lb(return_X_y=True)
print(x.shape, y.shape)  # (442, 10) (442,)

mod = KNeighborsRegressor()
mod.fit(x, y)

print(mod.predict(x))
