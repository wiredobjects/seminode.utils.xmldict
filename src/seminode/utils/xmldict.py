# Copyright 2009, MC.Spring Team - Heresy.Mc@gmail.com
# All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# Based on
# Project: XML2Dict
# Url:     https://github.com/mcspring/XML2Dict
# Package: encoder
# Class:   XML2Dict
# Version: 0.1
# License  Apache License, Version 2.0


__all__ = ['XML2Dict']

try:
    import cElementTree as etree
except ImportError:
    try:
        import xml.etree.ElementTree as etree
    except ImportError:
        from elementtree import ElementTree as etree
# import third party
# import local


class XML2Dict(object):
    """
    XML2Dict: Convert xml string to python dict
    """

    def __init__(self, coding = 'UTF-8'):
        self._coding = coding

    def _parse_node(self, node):
        tree = {}
        for child in node.getchildren():
            ctag = child.tag
            cattr = child.attrib
            ctree = self._parse_node(child)
            ctext = child.text
            if ctext:
                ctext = ctext.strip().encode(self._coding)
            if not ctree:
                cdict = self._make_dict(ctag, ctext, cattr)
            else:
                cdict = self._make_dict(ctag, ctree, cattr)
            # First time found
            if ctag not in tree:
                tree.update(cdict)
                continue
            atag = '@' + ctag
            atree = tree[ctag]
            if not isinstance(atree, list):
                if atag in tree:
                    atree['#'+ctag] = tree[atag]
                    del tree[atag]
                # Multi entries, change to list
                tree[ctag] = [atree]
            if cattr:
                ctree['#'+ctag] = cattr
            tree[ctag].append(ctree)
        return  tree

    def _make_dict(self, tag, value, attr = None):
        """
        Generate a new dict with tag and value
        
        If attr is True then convert tag name to @tag
        and convert tuple list to dict
        """
        ret = {tag: value}
        # Save attributes as @tag value
        if attr:
            atag = '@' + tag
            aattr = {}
            for k, v in attr.items():
                aattr[k] = v
            ret[atag] = aattr
            del atag
            del aattr
        return ret

    def parse(self, xml):
        """
        Parse xml string to python dict
        """
        tree = etree.fromstring(xml)
        return self._make_dict(tree.tag, self._parse_node(tree), tree.attrib)

