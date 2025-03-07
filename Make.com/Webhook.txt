import json

def analyze_market_data(market_data):
 """
 Filters companies with a growth rate greater than 5%
 and calculates the average growth by industry.
 """
 # Filter companies with growth > 5%
 filtered_data = [company for company in market_data if company.get('growth_rate', 0) > 5]

 # Calculate average growth by industry
 industry_growth = {}
 for company in filtered_data:
 industry = company.get('industry', 'Unknown')
 industry_growth.setdefault(industry, []).append(company['growth_rate'])

 avg_growth = {industry: sum(rates) / len(rates) for industry, rates in industry_growth.items()}
 return avg_growth

if __name__ == '__main__':

 from flask import Flask, request, jsonify

app = Flask(__name__)

def analyze_market_data(market_data):
"""
Filter companies with a growth rate greater than 5%
and calculate the average growth by industry.
"""
# Filter companies with growth > 5%
filtered_data = [company for company in market_data if company.get('growth_rate', 0) > 5]

# Calculate average growth by industry
industry_growth = {}
for company in filtered_data:
industry = company.get('industry', 'Unknown')
industry_growth.setdefault(industry, []).append(company['growth_rate'])

avg_growth = {industry: sum(rates) / len(rates) for industry, rates in industry_growth.items()}
return avg_growth

@app.route('/webhook', methods=['POST'])
def webhook():
 # Receive the JSON payload sent via an HTTP POST request
 data = request.get_json()
 if not data:
 return jsonify({"error": "No data received"}), 400

 # Process the data
 result = analyze_market_data(data)
 return jsonify(result)

if __name__ == '__main__':
 app.run(debug=True, port=5000)

 data = request.get_json()
 result = analyze_market_data(data)
 print(json.dumps(result, indent=2))