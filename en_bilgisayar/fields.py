from djongo.models.fields import EmbeddedField, ArrayField

class MyEmbeddedField(EmbeddedField):
    def from_db_value(self, value, expression, connection, context=None):
        return super(MyEmbeddedField, self).from_db_value(value, expression, connection, context)

class MyArrayField(ArrayField):
    def from_db_value(self, value, expression, connection, context=None):
        return super(MyArrayField, self).from_db_value(value, expression, connection, context)