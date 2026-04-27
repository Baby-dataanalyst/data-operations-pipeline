# Run this cell first to create the test CSV
import pandas as pd
from datetime import date

data = {
    "customer_id": [101, 102, 101, 103, 104],
    "order_value": [500, None, 500, 300, 200],
    "status": ["SUCCESS", "FAILED", "SUCCESS", "SUCCESS", "SUCCESS"],
    "load_timestamp": [str(date.today()) + " 07:00:00"] * 5
}

pd.DataFrame(data).to_csv("pipeline_output.csv", index=False)
print("CSV created")