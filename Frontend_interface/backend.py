from flask import Flask, request, render_template
import main

app = Flask(__name__)

@app.route('/')
def index():
    headings = ('Label','Values')
    results = (
        ('Vendor Name',main.vendor_name),
        ('Invoice Date',main.invoice_date),
        ('Invoice number',main.invoice_number),
        ('total amount',main.total_amount),
    )
    return render_template('index.html',results=results,headings=headings)

@app.route('/table')
def table():
    render_template('table.html')
if __name__ == '__main__':
    app.run()