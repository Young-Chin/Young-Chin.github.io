import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]
POST_PATH = ROOT / "_posts" / "2026-09-01-video-subtitle-ocr-practice.md"
APPLY_PAGE_PATH = ROOT / "apply" / "2026" / "index.html"
DETAILS_PATH = ROOT / "apply" / "2026" / "details.js"


class ApplyOcrPostTests(unittest.TestCase):
    def test_ocr_card_links_to_its_blog_post_without_modal_data(self):
        page = APPLY_PAGE_PATH.read_text(encoding="utf-8")

        card_match = re.search(
            r'<a class="work-card work-card-link" href="(?P<href>[^"]+)"[^>]*>\s*'
            r"<h4>视频字幕 OCR</h4>",
            page,
        )

        self.assertIsNotNone(card_match)
        self.assertEqual(card_match.group("href"), "/posts/video-subtitle-ocr-practice")
        self.assertNotIn('data-detail="ocr"', page)

    def test_ocr_article_exists_and_is_not_in_modal_details(self):
        post = POST_PATH.read_text(encoding="utf-8")
        details_source = DETAILS_PATH.read_text(encoding="utf-8")
        details = json.loads(
            details_source.removeprefix("window.applyDetails = ").removesuffix(";\n")
        )

        self.assertIn("title: '影视字幕 OCR 的工程化实践：从传统检测识别到 VLM-based OCR'", post)
        self.assertIn("permalink: /posts/video-subtitle-ocr-practice", post)
        self.assertNotIn("ocr", details)


if __name__ == "__main__":
    unittest.main()
