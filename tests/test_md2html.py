import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).parents[1] / "scripts" / "md2html.py"
spec = importlib.util.spec_from_file_location("md2html", MODULE_PATH)
md2html = importlib.util.module_from_spec(spec)
spec.loader.exec_module(md2html)


class MarkdownToHtmlTests(unittest.TestCase):
    def test_parses_detail_sections_and_markdown_blocks(self):
        source = """## ocr
# OCR 详情
### 背景
字幕 **识别**。
- 第一项
- 第二项
![结果图](images/result.png)
"""

        details = md2html.parse_details(source)

        self.assertEqual(set(details), {"ocr"})
        self.assertIn('<h3>OCR 详情</h3>', details["ocr"])
        self.assertIn('<h4>背景</h4>', details["ocr"])
        self.assertIn('<strong>识别</strong>', details["ocr"])
        self.assertIn('<ul><li>第一项</li><li>第二项</li></ul>', details["ocr"])
        self.assertIn('<img src="./images/result.png" alt="结果图">', details["ocr"])

    def test_renders_safe_javascript_data(self):
        rendered = md2html.render_js({"demo": '<p>Bob & "AI"</p>'})

        self.assertTrue(rendered.startswith("window.applyDetails = "))
        self.assertIn('"demo": "<p>Bob & \\\"AI\\\"</p>"', rendered)
        self.assertTrue(rendered.rstrip().endswith(";"))


if __name__ == "__main__":
    unittest.main()
