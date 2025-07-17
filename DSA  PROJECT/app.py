from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        form_data = {
            'Aging': float(request.form['Aging']),
            'Gender': request.form['Gender'],
            'Device_Type': request.form['Device_Type'],
            'Customer_Login_type': request.form['Customer_Login_type'],
            'Product': request.form['Product'],
            'Sales': float(request.form['Sales']),
            'Quantity': int(request.form['Quantity']),
            'Discount': float(request.form['Discount']),
            'Profit': float(request.form['Profit']),
            'Shipping_Cost': float(request.form['Shipping_Cost']),
            'Order_Priority': request.form['Order_Priority'],
            'Payment_method': request.form['Payment_method']
        }
        prediction = predict_product_category(form_data)

    return render_template('index.html'

        <!DOCTYPE html>
<html>
<head><title>Product Category Predictor</title></head>
<body>
    <h2>Predict Product Category</h2>
    <form method="POST">
        Aging: <input name="Aging"><br>
        Gender: <input name="Gender"><br>
        Device Type: <input name="Device_Type"><br>
        Login Type: <input name="Customer_Login_type"><br>
        Product: <input name="Product"><br>
        Sales: <input name="Sales"><br>
        Quantity: <input name="Quantity"><br>
        Discount: <input name="Discount"><br>
        Profit: <input name="Profit"><br>
        Shipping Cost: <input name="Shipping_Cost"><br>
        Order Priority: <input name="Order_Priority"><br>
        Payment Method: <input name="Payment_method"><br>
        <button type="submit">Predict</button>
    </form>

    {% if prediction %}
        <h3>Predicted Category: {{ prediction }}</h3>
    {% endif %}
</body>
</html>
, prediction=prediction)
