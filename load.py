import pandas as pd
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

def save_to_csv(data, filename_prefix="output"):
    """Save transformed data to CSV with timestamp."""
    try:
        logger.info(f"Starting data loading to CSV")
        
        # Create filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{filename_prefix}_{timestamp}.csv"
        
        # Convert to DataFrame and save
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        
        logger.info(f"Data successfully saved to {filename}")
        return filename
    except Exception as e:
        logger.error(f"Error during data loading: {str(e)}")
        raise