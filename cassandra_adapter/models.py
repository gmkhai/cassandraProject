from abc import ABC, abstractmethod
# from cassandra_adapter.gateway import CassandraAdapter


class BaseField(ABC):
    def __init__(self):
        self.get_type_data()

    def get_type_data(self):
        return self._type_data()

    @abstractmethod
    def _type_data(self):
        pass


class CharField(BaseField):
    def _type_data(self):
        return "text"


class IntField(BaseField):
    def _type_data(self):
        return "int"


class UUIDField(BaseField):
    def _type_data(self):
        return "uuid"


class PrimaryKey(BaseField):
    def _type_data(self):
        return "PRIMARY KEY"


class ClusterKey(BaseField):
    def _type_data(self):
        return "CLUSTERING KEY"


class Model:

    def __init__(self):
        self.get_attributes()
        self.get_subclass_name()
        print(self.get_attributes())
        print(self.get_subclass_name())

    def get_attributes(self):
        attribute_dict = self.__class__.__dict__
        attribute = {}
        for key, value in attribute_dict.items():
            if isinstance(value, BaseField):
                attribute[key] = value.get_type_data()

        return attribute

    def get_subclass_name(self):
        sub_class = self.__class__.__name__
        return sub_class


class product_test(Model):
    product_id = CharField()
    product_description = CharField()


product_test()





