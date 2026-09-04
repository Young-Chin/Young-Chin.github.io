import re
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]
POST_PATH = ROOT / "_posts" / "2026-09-04-smart-marketing-agent-architecture.html"
APPLY_PAGE_PATH = ROOT / "apply" / "2026" / "index.html"


class ApplyMarketingPostTests(unittest.TestCase):
    def test_marketing_agent_card_links_to_architecture_post(self):
        page = APPLY_PAGE_PATH.read_text(encoding="utf-8")

        card_match = re.search(
            r'<a class="work-card work-card-link" href="(?P<href>[^"]+)"[^>]*>\s*'
            r"<h4>智能营销 Agent</h4>",
            page,
        )

        self.assertIsNotNone(card_match)
        self.assertEqual(
            card_match.group("href"), "/posts/smart-marketing-agent-architecture"
        )

    def test_marketing_agent_article_exists_with_expected_permalink(self):
        post = POST_PATH.read_text(encoding="utf-8")

        self.assertIn("layout: none", post)
        self.assertIn("title: '智能营销 Agent 系统架构图'", post)
        self.assertIn("permalink: /posts/smart-marketing-agent-architecture", post)
        self.assertIn("<html", post)


if __name__ == "__main__":
    unittest.main()
