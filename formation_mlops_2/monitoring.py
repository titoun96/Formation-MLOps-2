import pandas as pd
from datetime import datetime



def monitor(latest_predictions: pd.DataFrame) -> pd.DataFrame:
    # Start filling function
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    monitoring_df = pd.DataFrame({
        "predictions_time": [latest_predictions['predictions_time'].min(), latest_predictions['predictions_time'].max()],
        "predictions": [latest_predictions['predictions'].min(), latest_predictions['predictions'].max()]
    })
    # End filling function
    return monitoring_df
