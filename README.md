# HustleSasa Recommendation Engine

## Overview
A machine learning-powered recommendation system for HustleSasa's e-commerce platform, demonstrating content-based and collaborative filtering techniques.

## Features
- Content-based recommendations
- Collaborative filtering
- Flexible recommendation strategies
- Easy integration with existing systems

## Requirements
- Python 3.8+
- pandas
- scikit-learn
- numpy

## Installation
```bash
git clone https://github.com/hustlesasa/recommendation-engine.git
cd recommendation-engine
pip install -r requirements.txt
```

## Usage
```python
from recommender import HustleSasaRecommender

# Initialize with product data
recommender = HustleSasaRecommender('products.csv')

# Get content-based recommendations
content_recs = recommender.get_content_based_recommendations(
    product_id='PROD001', 
    top_n=5
)

# Get collaborative filtering recommendations
collab_recs = recommender.collaborative_filter_recommendation(
    user_interactions=['PROD002', 'PROD003'], 
    top_n=5
)
```

## Testing
```bash
python -m unittest discover tests
```

## Future Improvements
- Advanced machine learning models
- Real-time recommendation updates
- Enhanced personalization