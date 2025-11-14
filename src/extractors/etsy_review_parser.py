thonpython
import logging
from datetime import datetime
from .utils_date import normalize_date

class EtsyReviewParser:
    def __init__(self, keyword: str, limit: int = 20):
        self.keyword = keyword
        self.limit = limit

    def extract_reviews(self):
        logging.info(f"Simulating Etsy review extraction for shop keyword '{self.keyword}'...")
        # Simulated extraction (replace with real scraping logic)
        sample_reviews = []
        for i in range(self.limit):
            sample_reviews.append({
                "receipt_id": 1000000000 + i,
                "buyer_login_name": f"user{i}",
                "buyer_real_name": f"User {i}",
                "date": normalize_date(str(datetime.utcnow().date())),
                "listing_title": f"Product {i}",
                "listing_image_url": "https://example.com/image.png",
                "listing_review": f"This is a sample review #{i}",
                "response": None if i % 2 == 0 else f"Seller response #{i}",
                "rating": 5 if i % 3 != 0 else 4
            })

        return sample_reviews