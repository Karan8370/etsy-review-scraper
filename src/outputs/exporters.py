thonpython
import json
import csv
import logging
from xml.etree.ElementTree import Element, SubElement, tostring
import pandas as pd

class Exporter:
    def export(self, data, filepath, fmt="json"):
        fmt = fmt.lower()
        if fmt == "json":
            self._to_json(data, filepath)
        elif fmt == "csv":
            self._to_csv(data, filepath)
        elif fmt == "excel":
            self._to_excel(data, filepath)
        elif fmt == "html":
            self._to_html(data, filepath)
        elif fmt == "xml":
            self._to_xml(data, filepath)
        else:
            raise ValueError(f"Unsupported export format: {fmt}")

    def _to_json(self, data, filepath):
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)

    def _to_csv(self, data, filepath):
        with open(filepath, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

    def _to_excel(self, data, filepath):
        df = pd.DataFrame(data)
        df.to_excel(filepath, index=False)

    def _to_html(self, data, filepath):
        df = pd.DataFrame(data)
        df.to_html(filepath, index=False)

    def _to_xml(self, data, filepath):
        root = Element("reviews")
        for entry in data:
            item = SubElement(root, "review")
            for key, value in entry.items():
                child = SubElement(item, key)
                child.text = str(value)

        with open(filepath, "wb") as f:
            f.write(tostring(root))