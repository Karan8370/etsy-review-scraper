thonpython
import json
import logging
from extractors.etsy_review_parser import EtsyReviewParser
from outputs.exporters import Exporter
from config.settings import Settings

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def main():
    try:
        settings = Settings.load()
        input_file = settings.get("input_file", "data/input.sample.json")
        output_file = settings.get("output_file", "data/sample_output.json")
        output_format = settings.get("output_format", "json")

        logging.info("Loading input file...")
        with open(input_file, "r") as f:
            data = json.load(f)

        keyword = data.get("keyword", "")
        limit = data.get("limit", 20)

        parser = EtsyReviewParser(keyword=keyword, limit=limit)
        reviews = parser.extract_reviews()

        exporter = Exporter()
        exporter.export(reviews, output_file, output_format)

        logging.info(f"Export complete: {output_file}")
    except Exception as e:
        logging.exception("Runner failed")

if __name__ == "__main__":
    main()