import os
import sys

import file_utils
from lxml import etree

DEFAULT_NAMESPACE = '{http://maven.apache.org/POM/4.0.0}'

class XML_Parser(object):
    def __init__(self, xml, ns=DEFAULT_NAMESPACE):
        self.ns = ns

        if os.path.exists(xml):
            self.root = etree.parse(xml).getroot()
        else:
            self.root = etree.fromstring(xml)
       
    def tostring(self):
        return '<?xml version="1.0"?>\n'+etree.tostring(self.root, pretty_print=True)

    def serialize(self, path):
        file_utils.write_file(path, self.tostring())

    def find(self, tag):
        return self.root.find('.//%s%s' % (self.ns, tag))
    
    def get_child(self, parent_elem, child_tag):
        for child in list(parent_elem):
            if child.tag == '%s%s' % (self.ns, child_tag):
                return child

    def childs_to_tag_text_dict(self, elem):
        acutal_elem = None
        if type(elem) == str:
            acutal_elem = self.root.find('.//%s%s' % (self.ns, elem))
            if acutal_elem is None:
                raise ValueError('No element %s in tree.' % (elem))
        elif type(elem) == etree._Element:
            acutal_elem = elem
        else:
            raise ValueError('Expecting elem to be of type string or etree._Element, got %s' (str(type(elem))))

        res = dict()
        for child in [child for child in list(acutal_elem) if type(child.tag) is str]:
            res[child.tag[len(DEFAULT_NAMESPACE):]] = child.text

        return res


class POM_Parser(XML_Parser):
    @staticmethod
    def _distill_gav(d):
        return {key: value for key, value in d.items() if key in ('groupId', 'artifactId', 'version')}

    def __init__(self, xml, ns=DEFAULT_NAMESPACE):
        XML_Parser.__init__(self, xml, ns=DEFAULT_NAMESPACE)
        self.parent = self.find('parent')
        
    def gav(self, parent=False):
        if parent and self.parent is None:
            raise ValueError('can\'t change parent\'s gav when there is not parent!')
        gav_for = self.root if not parent else self.parent
        return POM_Parser._distill_gav(self.childs_to_tag_text_dict(gav_for))

    def change_gav(self, groupId=None, artifactId=None, version=None, parent=False):
        gav_variables = [(key, value) for key, value in locals().items() if key not in ('self','parent') and value is not None]

        if parent and self.parent is None:
            raise ValueError('can\'t change parent\'s gav when there is not parent!')

        elem_to_change = self.root if not parent else self.parent
        for key, value in gav_variables:
            self.get_child(elem_to_change, key).text = value

if __name__ == '__main__':
    xmp = POM_Parser('./pom.xml')
    print xmp.gav
    print xmp.parent_gav
    print xmp.get_child(xmp.root, 'parent')
    print xmp.get_child(xmp.find('parent'), 'version')
    xmp.change_gav('12', parent=False)
    print xmp.gav
    print xmp.parent_gav
