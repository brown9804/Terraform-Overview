import unittest
from pathlib import Path
from xml.etree import ElementTree

import markdown

from generate_examples import EXAMPLES, build_files


class ExampleCatalogTests(unittest.TestCase):
    def test_all_examples_are_rendered_in_the_catalog_table(self):
        source = build_files()[Path("docs/catalog.md")]
        rendered = markdown.markdown(source, extensions=["tables"])
        document = ElementTree.fromstring(f"<article>{rendered}</article>")
        rows = document.findall(".//tbody/tr")
        self.assertEqual(len(rows), len(EXAMPLES))
        for row, example in zip(rows, EXAMPLES):
            self.assertEqual(row.find("td/a").text, example[1])


if __name__ == "__main__":
    unittest.main()
