import unittest

from knowledge_base.utils.arxiv_utils import (
    arxiv_record_to_fields,
    parse_arxiv_feed_records,
    parse_arxiv_oai_record,
)


class ArxivRecordParsingTest(unittest.TestCase):
    def test_parse_atom_feed_returns_shared_record(self) -> None:
        feed = """\
<feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">
  <entry>
    <id>http://arxiv.org/abs/2401.01234v2</id>
    <title>  A   Useful
      Paper  </title>
    <summary>  Abstract
      text with    spacing. </summary>
    <published>2024-01-05T00:00:00Z</published>
    <author><name> Ada   Lovelace </name></author>
    <author><name>Grace Hopper</name></author>
    <arxiv:doi>10.1000/example</arxiv:doi>
    <arxiv:journal_ref>Journal Ref</arxiv:journal_ref>
    <arxiv:comment>12 pages</arxiv:comment>
    <arxiv:primary_category term="cs.LG" />
    <category term="cs.AI" />
    <category term="cs.LG" />
  </entry>
</feed>
"""

        records = parse_arxiv_feed_records(feed)

        record = records["2401.01234"]
        self.assertEqual(record.arxiv_id, "2401.01234")
        self.assertEqual(record.title, "A Useful Paper")
        self.assertEqual(record.authors, ["Ada Lovelace", "Grace Hopper"])
        self.assertEqual(record.year, 2024)
        self.assertEqual(record.abstract, "Abstract text with spacing.")
        self.assertEqual(record.doi, "10.1000/example")
        self.assertEqual(record.journal_ref, "Journal Ref")
        self.assertEqual(record.comment, "12 pages")
        self.assertEqual(record.primary_category, "cs.LG")
        self.assertEqual(record.categories, ["cs.AI", "cs.LG"])

        fields = arxiv_record_to_fields(record)
        self.assertEqual(fields["link"], "https://arxiv.org/pdf/2401.01234")
        self.assertEqual(fields["doi"], "10.1000/example")

    def test_parse_oai_record_returns_same_shape(self) -> None:
        record_xml = """\
<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/">
  <GetRecord>
    <record>
      <metadata>
        <arXiv xmlns="http://arxiv.org/OAI/arXiv/">
          <id>cs/9901001</id>
          <created>1999-01-12</created>
          <title>  Classic
            Result </title>
          <authors>
            <author>
              <keyname>Church</keyname>
              <forenames>Alonzo</forenames>
            </author>
            <author>
              <keyname>Turing</keyname>
              <forenames>Alan</forenames>
              <suffix>Jr.</suffix>
            </author>
          </authors>
          <abstract>  OAI
            abstract. </abstract>
          <doi>10.1000/oai</doi>
        </arXiv>
      </metadata>
    </record>
  </GetRecord>
</OAI-PMH>
"""

        record = parse_arxiv_oai_record(record_xml)

        self.assertEqual(record.arxiv_id, "cs/9901001")
        self.assertEqual(record.title, "Classic Result")
        self.assertEqual(record.authors, ["Alonzo Church", "Alan Turing Jr."])
        self.assertEqual(record.year, 1999)
        self.assertEqual(record.abstract, "OAI abstract.")
        self.assertEqual(record.doi, "10.1000/oai")

        fields = arxiv_record_to_fields(record)
        self.assertEqual(fields["link"], "https://arxiv.org/pdf/cs/9901001")
        self.assertEqual(fields["doi"], "10.1000/oai")


if __name__ == "__main__":
    unittest.main()
