# Importing entire module
import math
print(math.sqrt(16))

# Importing specific function
from random import randint
print(randint(1, 10))

# Aliasing a module
import datetime as dt
print(dt.datetime.now())

# Using requests library
import requests
response = requests.get('https://www.google.com')
print(response.status_code)

# Using matplotlib for visualization
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()

# Using Flask for web development
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
