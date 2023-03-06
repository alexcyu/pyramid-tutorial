import colander

# Defined here are 5 schemas based on the example data given in the tutorial
# The single node is broken down into data definitions (the Friend TupleScheme and the Phone MappingSchema) and object definitions (the Friends SequenceSchema and Phones SequenceSchema)
# Everything is then coalesced into the single Person MappingSchema
#
# As a result of the definitions, a Person represents
#  : a Name (which must be a string)
#  : an Age (which must be deserializable into an integer)
#       - after serialization a validator ensures the value is between 0 and 200
#  : a sequence of Friend structures
#       - each Friend structure is a two-element tuple
#           - first element -> an integer rank between 0 and 9999
#           - second element -> a string name
#
#  : a sequence of Phone structures
#       - each Phone structure is a Mapping
#           - each Phone Mapping has two keys -> location and number
#                - location must be either "home" or "work"
#                - number must be a string
class Friend(colander.TupleSchema):
    rank = colander.SchemaNode(colander.Int(),
                               validator=colander.Range(0, 9999))
    name = colander.SchemaNode(colander.String())

class Phone(colander.MappingSchema):
    location = colander.SchemaNode(colander.String(),
                                   validator=colander.OneOf(['home', 'work']))
    number = colander.SchemaNode(colander.String())

class Friends(colander.SequenceSchema):
    friend = Friend()

class Phones(colander.SequenceSchema):
    phone = Phone()

class Person(colander.MappingSchema):
    name = colander.SchemaNode(colander.String())
    age = colander.SchemaNode(colander.Int(),
                              validator=colander.Range(0, 200))
    friends = Friends()
    phones = Phones()
