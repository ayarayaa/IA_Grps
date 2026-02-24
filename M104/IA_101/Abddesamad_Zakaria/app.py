from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)
CSV_FILE = 'StudentsPerformance.csv'

@app.route('/', methods=['GET', 'POST'])
def index():
    # 1. Load your actual CSV data
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
    else:
        # Create dummy data if file is missing so the app doesn't crash
        df = pd.DataFrame(columns=['math score', 'reading score', 'writing score'])

    # 2. Get the very last row for the graph
    if not df.empty:
        last_row = df.iloc[-1]
        # We use .get() in case the columns have slightly different names
        current_data = {
            'math': int(last_row.get('math score', 0)),
            'reading': int(last_row.get('reading score', 0)),
            'writing': int(last_row.get('writing score', 0))
        }
    else:
        current_data = {'math': 0, 'reading': 0, 'writing': 0}

    if request.method == 'POST':
        # 3. Handle New Entry
        new_entry = {
            'math score': int(request.form.get('math', 0)),
            'reading score': int(request.form.get('reading', 0)),
            'writing score': int(request.form.get('writing', 0))
        }
        # Append to the dataframe and save back to CSV
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        df.to_csv(CSV_FILE, index=False)
        
        current_data = {'math': new_entry['math score'], 
                        'reading': new_entry['reading score'], 
                        'writing': new_entry['writing score']}

    # Prepare history for the table (last 10 rows)
    history = df.tail(10).to_dict(orient='records')

    return render_template('index.html', data=current_data, history=history)

if __name__ == '__main__':
    app.run(debug=True)