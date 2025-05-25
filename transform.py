import pandas as pd
import logging

logger = logging.getLogger(__name__)

def transform_data(raw_data):
    """Transform raw API data into structured format with aggregations."""
    try:
        logger.info("Starting data transformation")
        
        # Convert to DataFrame
        df = pd.DataFrame(raw_data)
        
        # Example transformations:
        # 1. Count posts per user
        user_post_counts = df['userId'].value_counts().reset_index()
        user_post_counts.columns = ['userId', 'postCount']
        
        # 2. Average title length per user
        df['titleLength'] = df['title'].str.len()
        avg_title_length = df.groupby('userId')['titleLength'].mean().reset_index()
        avg_title_length.columns = ['userId', 'avgTitleLength']
        
        # Merge aggregations
        transformed_data = pd.merge(user_post_counts, avg_title_length, on='userId')
        
        logger.info("Data transformation completed")
        return transformed_data.to_dict('records')
    
    except Exception as e:
        logger.error(f"Error during data transformation: {str(e)}")
        raise