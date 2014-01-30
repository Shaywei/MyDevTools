import os
import unittest
import file_utils

import xml_utils

POM_XML= '''<?xml version="1.0"?>
<project xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd"
         xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.hp.ess</groupId>
    <artifactId>ess-ui</artifactId>
    <packaging>pom</packaging>
    <name>ESS UI</name>
    <!-- define new version so we can use versions:set on this pom for CI pipeline -->
    <version>1.0.0-9999-SNAPSHOT</version>

    <parent>
        <groupId>com.hp.maas.platform</groupId>
        <artifactId>platform-ui</artifactId>
        <version>1.0.0-9999-SNAPSHOT</version>
    </parent>
    <bla>
        <foo>baz</foo>
    </bla>
</project>
'''
class Test_XML_Parser(unittest.TestCase):
    def setUp(self):
        self.test_xmlp = xml_utils.XML_Parser('pom.xml', ns='{http://maven.apache.org/POM/4.0.0}')

    def test_find(self):
        # Act + Assert
        self.assertEqual('baz', self.test_xmlp.find('foo').text)

    def test_get_child(self):
        # Arrange
        expected = 'platform-ui'
        parent_elem = self.test_xmlp.find('parent')

        # Act
        actual = self.test_xmlp.get_child(parent_elem, 'artifactId').text

        # Assert
        self.assertEqual(expected, actual)

    def test_childs_to_tag_text_dict_actual_elem(self):
        # Arrange
        expected = {'version': '1.0.0-9999-SNAPSHOT', 'groupId': 'com.hp.maas.platform', 'artifactId': 'platform-ui'}
        parent_elem = self.test_xmlp.find('parent')

        # Act
        actual = self.test_xmlp.childs_to_tag_text_dict(parent_elem)

        # Assert
        self.assertEqual(expected, actual)

    def test_childs_to_tag_text_dict_actual_str(self):
        # Arrange
        expected = {'version': '1.0.0-9999-SNAPSHOT', 'groupId': 'com.hp.maas.platform', 'artifactId': 'platform-ui'}

        # Act
        actual = self.test_xmlp.childs_to_tag_text_dict('parent')

        # Assert
        self.assertEqual(expected, actual)

    def test_serialize(self):
        # Arrange
        test_output_file_name = './test_serialize_pom.xml'
        expected = self.test_xmlp.tostring()

        # Act
        self.test_xmlp.serialize(test_output_file_name)
        actual = xml_utils.XML_Parser(file_utils.read_file(test_output_file_name)).tostring()

        # Assert
        self.assertEqual(expected, actual)

        # Cleanup
        os.remove(test_output_file_name)

class Test_POM_Parser(unittest.TestCase):
    def setUp(self):
        self.test_pomp = xml_utils.POM_Parser('pom.xml', ns='{http://maven.apache.org/POM/4.0.0}')


    def test_gav_parsed_correctly(self):
        # Arrange
        expected = {'version': '1.0.0-9999-SNAPSHOT', 'groupId': 'com.hp.ess', 'artifactId': 'ess-ui'}

        # Assert
        self.assertEqual(expected, self.test_pomp.gav())

    def test_parent_gav_parsed_correctly(self):
        # Arrange
        expected = {'version': '1.0.0-9999-SNAPSHOT', 'groupId': 'com.hp.maas.platform', 'artifactId': 'platform-ui'}

        # Assert
        self.assertEqual(expected, self.test_pomp.gav(True))

    def test_change_gav(self):
        # Arrange
        expected = {'version': 'foo', 'groupId': 'baz', 'artifactId': 'bar'}

        # Act
        self.test_pomp.change_gav(version='foo', groupId='baz', artifactId='bar')
        # Assert
        self.assertEqual(expected, self.test_pomp.gav())

    def test_change_gav_parent(self):
        # Arrange
        expected = {'version': 'foo', 'groupId': 'baz', 'artifactId': 'bar'}

        # Act
        self.test_pomp.change_gav(version='foo', groupId='baz', artifactId='bar', parent=True)

        # Assert
        self.assertEqual(expected, self.test_pomp.gav(True))

    def test_change_gav_partial(self):
        # Arrange
        expected = {'version': 'foo', 'groupId': 'com.hp.ess', 'artifactId': 'bar'}

        # Act
        self.test_pomp.change_gav(version='foo', artifactId='bar')
        # Assert
        self.assertEqual(expected, self.test_pomp.gav())

    def test_change_gav_parent_partial(self):
        # Arrange
        expected = {'version': 'foo', 'groupId': 'com.hp.maas.platform', 'artifactId': 'bar'}

        # Act
        self.test_pomp.change_gav(version='foo', artifactId='bar', parent=True)

        # Assert
        self.assertEqual(expected, self.test_pomp.gav(True))
        
if __name__ == '__main__':
    unittest.main()