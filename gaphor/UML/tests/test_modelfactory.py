from gaphor import UML
from gaphor.application import Application
from gaphor.UML.modelfactory import STEREOTYPE_FMT as fmt

import unittest

class StereotypesTest(unittest.TestCase):
    def setUp(self):
        Application.init_components()
        self.factory = UML.ElementFactory()
        self.factory.init(Application)

    def test_stereotype_name(self):
        """Test stereotype name
        """
        stereotype = self.factory.create(UML.Stereotype)
        stereotype.name = 'Test'
        self.assertEquals('test', UML.model.stereotype_name(stereotype))

        stereotype.name = 'TEST'
        self.assertEquals('TEST', UML.model.stereotype_name(stereotype))

        stereotype.name = 'T'
        self.assertEquals('t', UML.model.stereotype_name(stereotype))

        stereotype.name = ''
        self.assertEquals('', UML.model.stereotype_name(stereotype))

        stereotype.name = None
        self.assertEquals('', UML.model.stereotype_name(stereotype))


    def test_stereotypes_conversion(self):
        """Test stereotypes conversion
        """
        s1 = self.factory.create(UML.Stereotype)
        s2 = self.factory.create(UML.Stereotype)
        s3 = self.factory.create(UML.Stereotype)
        s1.name = 's1'
        s2.name = 's2'
        s3.name = 's3'

        cls = self.factory.create(UML.Class)
        UML.model.apply_stereotype(self.factory, cls, s1)
        UML.model.apply_stereotype(self.factory, cls, s2)
        UML.model.apply_stereotype(self.factory, cls, s3)

        self.assertEquals(fmt % 's1, s2, s3', UML.model.stereotypes_str(cls))


    def test_no_stereotypes(self):
        """Test stereotypes conversion without applied stereotypes
        """
        cls = self.factory.create(UML.Class)
        self.assertEquals('', UML.model.stereotypes_str(cls))


    def test_additional_stereotypes(self):
        """Test additional stereotypes conversion
        """
        s1 = self.factory.create(UML.Stereotype)
        s2 = self.factory.create(UML.Stereotype)
        s3 = self.factory.create(UML.Stereotype)
        s1.name = 's1'
        s2.name = 's2'
        s3.name = 's3'

        cls = self.factory.create(UML.Class)
        UML.model.apply_stereotype(self.factory, cls, s1)
        UML.model.apply_stereotype(self.factory, cls, s2)
        UML.model.apply_stereotype(self.factory, cls, s3)

        result = UML.model.stereotypes_str(cls, ('test',))
        self.assertEquals(fmt % 'test, s1, s2, s3', result)


    def test_just_additional_stereotypes(self):
        """Test additional stereotypes conversion without applied stereotypes
        """
        cls = self.factory.create(UML.Class)

        result = UML.model.stereotypes_str(cls, ('test',))
        self.assertEquals(fmt % 'test', result)


    def test_getting_stereotypes(self):
        """Test getting possible stereotypes
        """
        cls = self.factory.create(UML.Class)
        cls.name = 'Class'
        st1 = self.factory.create(UML.Stereotype)
        st1.name = 'st1'
        st2 = self.factory.create(UML.Stereotype)
        st2.name = 'st2'

        # first extend with st2, to check sorting
        UML.model.extend_with_stereotype(self.factory, cls, st2)
        UML.model.extend_with_stereotype(self.factory, cls, st1)

        c1 = self.factory.create(UML.Class)
        result = tuple(st.name for st in UML.model.get_stereotypes(self.factory, c1))
        self.assertEquals(('st1', 'st2'), result)


    def test_getting_stereotypes_unique(self):
        """Test if possible stereotypes are unique
        """
        cls1 = self.factory.create(UML.Class)
        cls1.name = 'Class'
        cls2 = self.factory.create(UML.Class)
        cls2.name = 'Component'
        st1 = self.factory.create(UML.Stereotype)
        st1.name = 'st1'
        st2 = self.factory.create(UML.Stereotype)
        st2.name = 'st2'

        # first extend with st2, to check sorting
        UML.model.extend_with_stereotype(self.factory, cls1, st2)
        UML.model.extend_with_stereotype(self.factory, cls1, st1)

        UML.model.extend_with_stereotype(self.factory, cls2, st1)
        UML.model.extend_with_stereotype(self.factory, cls2, st2)

        c1 = self.factory.create(UML.Component)
        result = tuple(st.name for st in UML.model.get_stereotypes(self.factory, c1))
        self.assertEquals(('st1', 'st2'), result)


class AssociationTestCase(unittest.TestCase):
    """
    Association tests.
    """
    def setUp(self):
        Application.init_components()
        self.factory = UML.ElementFactory()
        self.factory.init(Application)


    def test_creation(self):
        """Test association creation
        """
        c1 = self.factory.create(UML.Class)
        c2 = self.factory.create(UML.Class)
        assoc = UML.model.create_association(self.factory, c1, c2)
        types = [p.type for p in assoc.memberEnd]
        self.assertTrue(c1 in types, assoc.memberEnd)
        self.assertTrue(c2 in types, assoc.memberEnd)



class AssociationEndNavigabilityTestCase(unittest.TestCase):
    """
    Association navigability changes tests.
    """
    def setUp(self):
        Application.init_components()
        self.factory = UML.ElementFactory()
        self.factory.init(Application)

    
    def test_attribute_navigability(self):
        """Test navigable attribute of a class or an interface
        """
        assoc = self.factory.create(UML.Association)


    def test_relationship_navigability(self):
        """Test navigable relationship of a classifier
        """
        self.assertTrue(false)


    def test_actor_navigability(self):
        """Test navigable relationship of an actor
        """
        self.assertTrue(false)


# vim:sw=4:et
