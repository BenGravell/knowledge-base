import unittest

from knowledge_base.config import KB_DIR, PAPERS_DIR


class PathConfigTest(unittest.TestCase):
    def test_papers_dir_is_anchored_to_the_knowledge_base(self) -> None:
        self.assertEqual(PAPERS_DIR, KB_DIR / "docs" / "papers")


if __name__ == "__main__":
    unittest.main()
