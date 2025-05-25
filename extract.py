import requests
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='etl.log'
)
logger = logging.getLogger(__name__)

def fetch_data(api_url):
    """Fetch data from the specified API endpoint."""
    try:
        logger.info(f"Starting data extraction from {api_url}")
        response = requests.get(api_url)
        response.raise_for_status()  # Raises exception for 4XX/5XX status
        logger.info("Data extraction successful")
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error during data extraction: {str(e)}")
        raise

if __name__ == "__main__":
    # Example usage
    API_URL = "https://jsonplaceholder.typicode.com/posts"
    data = fetch_data(API_URL)
    print(f"Fetched {len(data)} records")