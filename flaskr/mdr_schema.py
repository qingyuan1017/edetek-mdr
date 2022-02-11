from flaskr import db
from flaskr.db import db


class ODM(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Child Variables
    Study = db.relationship('Study', backref='ODM', lazy=True)
    AdminData = db.relationship('AdminData', backref='ODM', lazy=True)
    ReferenceData = db.relationship('ReferenceData', backref='ODM', lazy=True)
    ClinicalData = db.relationship('ClinicalData', backref='ODM', lazy=True)
    Association = db.relationship('Association', backref='ODM', lazy=True)
    Signature = db.relationship('Signature', backref='ODM', lazy=True)

    # Attribute Variables
    Description = db.Column(db.String(500))
    Filetype = db.Column(db.String(20))
    Granularity = db.Column(db.String(50))
    Archival = db.Column(db.String(50))
    FileOID = db.Column(db.String(128))
    CreationDateTime = db.Column(db.DateTime())
    PriorFileOID = db.Column(db.String(128))
    AsOfDateTime = db.Column(db.DateTime())
    ODMVersion = db.Column(db.String(5))
    Originator = db.Column(db.String(100))
    SourceSystem = db.Column(db.String(200))

    # Additional Variable
    Context = db.Column(db.String(500))


class Study(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variables
    ODM = db.Column(db.Integer, db.ForeignKey('ODM.id'), nullable=False)
    # Child Variables
    GlobalVariables = db.relationship('GlobalVariables', backref='Study', lazy=True)
    BasicDefinitions = db.relationship('BasicDefinitions', backref='Study', lazy=True)
    MetaDataVersion = db.relationship('MetaDataVersion', backref='Study', lazy=True)

    # Attribute Variables
    OID = db.Column(db.String(128), unique=True, nullable=False)

    def __repr__(self):
        return '<Study %r>' % self.OID


class GlobalVariables(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variables
    Study = db.Column(db.Integer, db.ForeignKey('study.id'), nullable=False)

    # Child Variables
    StudyName = db.relationship('StudyName', backref='GlobalVariables', lazy=True)
    StudyDescription = db.relationship('StudyDescription', backref='GlobalVariables', lazy=True)
    ProtocolName = db.relationship('ProtocolName', backref='GlobalVariables', lazy=True)


class StudyName(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variable
    GlobalVariables = db.Column(db.Integer, db.ForeignKey('global_variables.id'), nullable=False)

    # Text Value
    Text = db.Column(db.String(200), nullable=False)


class StudyDescription(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variable
    GlobalVariables = db.Column(db.Integer, db.ForeignKey('global_variables.id'), nullable=False)

    # Text Value
    Text = db.Column(db.String(500), nullable=False)


class ProtocolName(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variable
    GlobalVariables = db.Column(db.Integer, db.ForeignKey('global_variables.id'), nullable=False)

    # Text Value
    Text = db.Column(db.String(500), nullable=False)


class BasicDefinitions(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    # Parent Variables
    Study = db.Column(db.Integer, db.ForeignKey('study.id'), nullable=False)

    # Child Variables
    MeasurementUnit = db.relationship('MeasurementUnit', backref='BasicDefinitions', lazy=True)


class MeasurementUnit(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    # Parent Variables
    BasicDefinitions = db.Column(db.Integer, db.ForeignKey('basic_definitions.id'), nullable=False)

    # Child Variables
    Symbol = db.relationship('Symbol', backref='MeasurementUnit', lazy=True)

    # Attribute Variables
    OID = db.Column(db.String(128), unique=True, nullable=False)
    Name = db.Column(db.String(128), nullable=False)


class Symbol(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    # Parent Variables
    MeasurementUnit = db.Column(db.Integer, db.ForeignKey('measurement_unit.id'), nullable=False)


class TranslatedText(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    # Parent Variables
    Symbol = db.Column(db.Integer, db.ForeignKey('symbol.id'), nullable=False)
    Decode = db.Column(db.Integer, db.ForeignKey('decode.id'), nullable=False)
    ErrorMessage = db.Column(db.Integer, db.ForeignKey('error_message.id'), nullable=False)
    Question = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    Description = db.Column(db.Integer, db.ForeignKey('description.id'), nullable=False)

    # Attribute Variables
    lang = db.Column(db.String(50))

    text = db.Column(db.String(500))


class MetaDataVersion(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    # Parent Variables
    Study = db.Column(db.Integer, db.ForeignKey('study.id'), nullable=False)

    # Child Variables
    Include = db.relationship('Include', backref='MetaDataVersion', lazy=True)
    Protocol = db.relationship('Protocol', backref='MetaDataVersion', lazy=True)
    StudyEventDef = db.relationship('StudyEventDef', backref='MetaDataVersion', lazy=True)
    FormDef = db.relationship('FormDef', backref='MetaDataVersion', lazy=True)
    ItemGroupDef = db.relationship('ItemGroupDef', backref='MetaDataVersion', lazy=True)
    ItemDef = db.relationship('ItemDef', backref='MetaDataVersion', lazy=True)
    Presentation = db.relationship('Presentation', backref='MetaDataVersion', lazy=True)
    ConditionDef = db.relationship('ConditionDef', backref='MetaDataVersion', lazy=True)
    MethodDef = db.relationship('MethodDef', backref='MetaDataVersion', lazy=True)
    Standards = db.relationship('Standards', backref='MetaDataVersion', lazy=True)
    AnnotatedCRF = db.relationship('AnnotatedCRF', backref='MetaDataVersion', lazy=True)
    SupplementalDoc = db.relationship('SupplementalDoc', backref='MetaDataVersion', lazy=True)
    ValueListDef = db.relationship('ValueListDef', backref='MetaDataVersion', lazy=True)
    WhereClauseDef = db.relationship('WhereClauseDef', backref='MetaDataVersion', lazy=True)
    CommentDef = db.relationship('CommentDef', backref='MetaDataVersion', lazy=True)

    # Attribute Variables
    OID = db.Column(db.String(128), unique=True, nullable=False)
    Name = db.Column(db.String(50), nullable=False)
    Description = db.Column(db.String(500))

    # Define Variables
    DefineVersion = db.Column(db.String(20))
    CommentOID = db.Column(db.String(128))
    Class = db.Column(db.String(20))
    StandardName = db.Column(db.String(20))
    StandardVersion = db.Column(db.String(20))


class Include(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variable
    MetaDataVersion = db.Column(db.Integer, db.ForeignKey('meta_data_version.id'), nullable=False)

    # Attribute Variable
    StudyOID = db.Column(db.String(128))
    MetaDataVersionOID = db.Column(db.String(128))


class Protocol(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Child Variable
    Description = db.relationship('Description', backref='Protocol', lazy=True)
    StudyEventRef = db.relationship('StudyEventRef', backref='Protocol', lazy=True)
    Alias = db.relationship('Alias', backref='Protocol', lazy=True)

    # Attribute Variable
    StudyOID = db.Column(db.String(128))
    MetaDataVersionOID = db.Column(db.String(128))

    # Parent Variable
    MetaDataVersion = db.Column(db.Integer, db.ForeignKey('meta_data_version.id'), nullable=False)


class Description(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    # Child Variables
    TranslatedText = db.relationship('TranslatedText', backref='Description', lazy=True)

    # Parent Variables
    Protocol = db.Column(db.Integer, db.ForeignKey('protocol.id'), nullable=False)
    StudyEventDef = db.Column(db.Integer, db.ForeignKey('study_event_def.id'), nullable=False)
    ItemGroupDef = db.Column(db.Integer, db.ForeignKey('item_group_def.id'), nullable=False)
    ConditionDef = db.Column(db.Integer, db.ForeignKey('condition_def.id'), nullable=False)
    ItemDef = db.Column(db.Integer, db.ForeignKey('item_def.id'), nullable=False)
    MethodDef = db.Column(db.Integer, db.ForeignKey('method_def.id'), nullable=False)


class StudyEventRef(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variables
    Protocol = db.Column(db.Integer, db.ForeignKey('protocol.id'), nullable=False)

    # Attribute Variables
    StudyEventOID = db.Column(db.String(128), nullable=False)
    OrderNumber = db.Column(db.Integer)
    Mandatory = db.Column(db.Boolean(), nullable=False)
    CollectionExceptionConditionOID = db.Column(db.String(128))


class StudyEventDef(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variable
    MetaDataVersion = db.Column(db.Integer, db.ForeignKey('meta_data_version.id'), nullable=False)

    # Child Variables
    Description = db.relationship('Description', backref='StudyEventDef', lazy=True)
    FromRef = db.relationship('FromRef', backref='StudyEventDef', lazy=True)
    Alias = db.relationship('Alias', backref='StudyEventDef', lazy=True)

    # Attribute Variables
    OID = db.Column(db.String(128), unique=True, nullable=False)
    Name = db.Column(db.String(50), nullable=False)
    Repeating = db.Column(db.Boolean(), nullable=False)
    Type = db.Column(db.String(20), nullable=False)
    Category = db.Column(db.String(200))


class FormRef(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variables
    StudyEventDef = db.Column(db.Integer, db.ForeignKey('study_event_def.id'),
                              nullable=False)

    # Attribute Variables
    FormOID = db.Column(db.String(128), nullable=False)
    OrderNumber = db.Column(db.Integer)
    Mandatory = db.Column(db.Boolean(), nullable=False)
    CollectionExceptionConditionOID = db.Column(db.String(128))


class FormDef(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variables
    MetaDataVersion = db.Column(db.Integer, db.ForeignKey('meta_data_version.id'), nullable=False)

    # Child Variables
    Description = db.relationship('Description', backref='FormDef', lazy=True)
    ItemGroupRef = db.relationship('ItemGroupRef', backref='FormDef', lazy=True)
    ArchiveLayout = db.relationship('ArchiveLayout', backref='FormDef', lazy=True)
    Alias = db.relationship('Alias', backref='FormDef', lazy=True)

    # Attribute Variables
    OID = db.Column(db.String(128), unique=True, nullable=False)
    Name = db.Column(db.String(50), nullable=False)
    Repeating = db.Column(db.Boolean(), nullable=False)


class ItemGroupRef(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variables
    FormDef = db.Column(db.Integer, db.ForeignKey('form_def.id'), nullable=False)

    # Attribute Variables
    ItemGroupOID = db.Column(db.String(128), nullable=False)
    OrderNumber = db.Column(db.Integer)
    Mandatory = db.Column(db.Boolean(), nullable=False)
    CollectionExceptionConditionOID = db.Column(db.String(128))


class ItemGroupDef(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    # Parent Variables
    MetaDataVersion = db.Column(db.Integer, db.ForeignKey('meta_data_version.id'), nullable=False)

    # Child Variables
    Description = db.relationship('Description', backref='ItemGroupDef', lazy=True)
    ItemRef = db.relationship('ItemRef', backref='ItemGroupDef', lazy=True)
    Alias = db.relationship('Alias', backref='ItemGroupDef', lazy=True)

    # Define Variables
    Class = db.relationship('Class', backref='ItemGroupDef', lazy=True)
    leaf = db.relationship('leaf', backref='ItemGroupDef', lazy=True)
    Attribute = db.relationship('Attribute', backref='ItemGroupDef', lazy=True)
    BasicValidation = db.relationship('BasicValidation', backref='ItemGroupDef', lazy=True)

    # Attribute Variables
    OID = db.Column(db.String(128), unique=True, nullable=False)
    Name = db.Column(db.String(50), nullable=False)
    Repeating = db.Column(db.Boolean(), nullable=False)
    IsReferenceData = db.Column(db.Boolean())
    # TODO Maybe add SAS_NAME check
    SASDatasetName = db.Column(db.String(20))
    Domain = db.Column(db.String(20))
    Origin = db.Column(db.String(20))
    # Deprecate in the future
    Role = db.Column(db.String(100))
    Purpose = db.Column(db.String(100))
    Comment = db.Column(db.String(200))
    # Define Attribute
    Structure = db.Column(db.String(100))
    ArchivedLocationID = db.Column(db.String(100))
    StandardOID = db.Column(db.String(128))
    IsNonStandard = db.Column(db.Boolean())
    HasNoData = db.Column(db.Boolean())
    # EDETEK Attribute
    CommentOID = db.Column(db.String(128))
    Class = db.Column(db.String(100))


class ItemRef(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variables
    ItemGroupDef = db.Column(db.Integer, db.ForeignKey('item_group_def.id'), nullable=False)

    # Child Variables
    WhereClauseRef = db.relationship('WhereClauseRef', backref='ItemRef', lazy=True)

    # Attribute Variables
    ItemOID = db.Column(db.String(128), nullable=False)
    OrderNumber = db.Column(db.Integer)
    Mandatory = db.Column(db.Boolean(), nullable=False)
    KeySequence = db.Column(db.Integer)
    MethodOID = db.Column(db.String(128))
    # Deprecated in the future
    ImputationMethodOID = db.Column(db.String(128))

    Role = db.Column(db.String(100))
    RoleCodeListOID = db.Column(db.String(128))
    CollectionExceptionConditionOID = db.Column(db.String(128))

    # Define variable
    IsNonStandard = db.Column(db.Boolean())
    HasNoData = db.Column(db.Boolean())

    # EDETEK variables
    Core = db.Column(db.String(20))


class ItemDef(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variables
    MetaDataVersion = db.Column(db.Integer, db.ForeignKey('meta_data_version.id'), nullable=False)

    # Child Variables
    Description = db.relationship('Description', backref='ItemDef', lazy=True)
    Question = db.relationship('Question', backref='ItemDef', lazy=True)
    ExternalQuestion = db.relationship('ExternalQuestion', backref='ItemDef', lazy=True)
    MeasurementUnitRef = db.relationship('MeasurementUnitRef', backref='ItemDef', lazy=True)
    RangeCheck = db.relationship('RangeCheck', backref='ItemDef', lazy=True)
    CodeListRef = db.relationship('CodeListRef', backref='ItemDef', lazy=True)
    Alias = db.relationship('Alias', backref='ItemDef', lazy=True)
    # Define variables
    Origin = db.relationship('Origin', backref='ItemDef', lazy=True)
    ValueListRef = db.relationship('ValueListRef', backref='ItemDef', lazy=True)

    # EDETEK variables
    BasicValidation = db.relationship('BasicValidation', backref='ItemDef', lazy=True)
    Label = db.relationship('Label', backref='ItemDef', lazy=True)
    IsShared = db.relationship('IsShared', backref='ItemDef', lazy=True)
    Attribute = db.relationship('Attribute', backref='ItemDef', lazy=True)

    # Attribute Variables
    OID = db.Column(db.String(128), unique=True, nullable=False)
    Name = db.Column(db.String(50), nullable=False)
    # TODO Change to enum in the future
    DataType = db.Column(db.String(30), nullable=False)
    Length = db.Column(db.Integer)
    SignificantDigits = db.Column(db.Integer)
    SASFieldName = db.Column(db.String(20))
    SDSVarName = db.Column(db.String(20))
    Origin = db.Column(db.String(200))
    Comment = db.Column(db.String(500))
    DisplayFormat = db.Column(db.String(100))
    CommentOID = db.Column(db.String(128))
    # TODO Change to enum in the future
    ProcessingDataType = db.Column(db.String(30))


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variables
    ItemDef = db.Column(db.Integer, db.ForeignKey('item_def.id'), nullable=False)

    # Child Variables
    TranslatedText = db.relationship('TranslatedText', backref='Question', lazy=True)


class ExternalQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variables
    ItemDef = db.Column(db.Integer, db.ForeignKey('item_def.id'), nullable=False)

    # Attribute Variables
    Dictionary = db.Column(db.String(200))
    Version = db.Column(db.String(200))
    Code = db.Column(db.String(100))


class MeasurementUnitRef(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variables
    # ItemData = db.Column(db.Integer, db.ForeignKey('item_data.id'), nullable=False)
    ItemDef = db.Column(db.Integer, db.ForeignKey('item_def.id'), nullable=False)
    RangeCheck = db.Column(db.Integer, db.ForeignKey('range_check.id'), nullable=False)

    # Attribute
    MeasurementUnitOID = db.Column(db.String(128), nullable=False)


class RangeCheck(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variables
    ItemDef = db.Column(db.Integer, db.ForeignKey('item_def.id'), nullable=False)

    # Child Variables
    CheckValue = db.relationship('CheckValue', backref='RangeCheck', lazy=True)
    FormalExpression = db.relationship('FormalExpression', backref='RangeCheck', lazy=True)
    MeasurementUnitRef = db.relationship('MeasurementUnitRef', backref='RangeCheck', lazy=True)
    ErrorMessage = db.relationship('ErrorMessage', backref='RangeCheck', lazy=True)

    # Attribute Variables
    Comparator = db.Column(db.String(200))
    SoftHard = db.Column(db.String(200), nullable=False)

    # Define Variables
    ItemOID = db.Column(db.String(128))


class CheckValue(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variables
    RangeCheck = db.Column(db.Integer, db.ForeignKey('range_check.id'), nullable=False)

    text = db.Column(db.String(200))


class ErrorMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variables
    RangeCheck = db.Column(db.Integer, db.ForeignKey('range_check.id'), nullable=False)

    # Child Variable
    TranslatedText = db.relationship('TranslatedText', backref='ErrorMessage', lazy=True)


class CodeListRef(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variables
    ItemDef = db.Column(db.Integer, db.ForeignKey('item_def.id'), nullable=False)

    # Attribute Variable
    CodeListOID = db.Column(db.Text(128), nullable=False)


class Alias(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variables
    Protocol = db.Column(db.Integer, db.ForeignKey('protocol.id'))
    StudyEventDef = db.Column(db.Integer, db.ForeignKey('study_event_def.id'))
    FormDef = db.Column(db.Integer, db.ForeignKey('form_def.id'))
    ItemGroupDef = db.Column(db.Integer, db.ForeignKey('item_group_def.id'))
    ItemDef = db.Column(db.Integer, db.ForeignKey('item_def.id'))
    CodeList = db.Column(db.Integer, db.ForeignKey('code_list.id'))
    CodeListItem = db.Column(db.Integer, db.ForeignKey('code_list_item.id'))
    EnumeratedItem = db.Column(db.Integer, db.ForeignKey('enumerated_item.id'))
    MethodDef = db.Column(db.Integer, db.ForeignKey('method_def.id'))
    ConditionDef = db.Column(db.Integer, db.ForeignKey('condition_def.id'))

    # Attribute Variables
    Context = db.Column(db.Text(200), nullable=False)
    Name = db.Column(db.Text(200), nullable=False)


class CodeList(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variables
    MetaDataVersion = db.Column(db.Integer, db.ForeignKey('meta_data_version.id'), nullable=False)

    # Child Variables
    Description = db.relationship('Description', backref='CodeList', lazy=True)
    CodeListItem = db.relationship('CodeListItem', backref='CodeList', lazy=True)
    EnumeratedItem = db.relationship('EnumeratedItem', backref='CodeList', lazy=True)
    ExternalCodeList = db.relationship('ExternalCodeList', backref='CodeList', lazy=True)
    Alias = db.relationship('Alias', backref='CodeList', lazy=True)

    # Attribute Variables
    OID = db.Column(db.String(128), unique=True, nullable=False)
    Name = db.Column(db.String(50), nullable=False)
    # TODO Change to enum in the future
    DataType = db.Column(db.String(30), nullable=False)
    SASFormatName = db.Column(db.String(20))

    # Define Variable
    StandardOID = db.Column(db.String(128))
    IsNonStandard = db.Column(db.Boolean())
    CommentOID = db.Column(db.String(128))


class CodeListItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variables
    CodeList = db.Column(db.Integer, db.ForeignKey('code_list.id'), nullable=False)

    # Child Variables
    Decode = db.relationship('Decode', backref='CodeListItem', lazy=True)
    Alias = db.relationship('Alias', backref='CodeListItem', lazy=True)
    Description = db.relationship('Description', backref='CodeListItem', lazy=True)

    # Attribute Variables
    CodedValue = db.Column(db.String(200), nullable=False)
    Rank = db.Column(db.Numeric())
    OrderNumber = db.Column(db.Integer)

    # Define Variables
    ExtendedValue = db.Column(db.String(200))


class Decode(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variables
    CodeListItem = db.Column(db.Integer, db.ForeignKey('code_list_item.id'), nullable=False)

    # Child Variable
    TranslatedText = db.relationship('TranslatedText', backref='Decode', lazy=True)


class ExternalCodeList(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variables
    CodeList = db.Column(db.Integer, db.ForeignKey('code_list.id'), nullable=False)

    # Attribute Variables
    Dictionary = db.Column(db.String(200))
    Version = db.Column(db.String(200))
    ref = db.Column(db.String(200))
    href = db.Column(db.String(200))


class EnumeratedItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variables
    CodeList = db.Column(db.Integer, db.ForeignKey('code_list.id'), nullable=False)

    # Child Variables
    Alias = db.relationship('Alias', backref='EnumeratedItem', lazy=True)

    # Attribute Variables
    CodedValue = db.Column(db.String(200), nullable=False)
    Rank = db.Column(db.Numeric())
    OrderNumber = db.Column(db.Integer)

    # Define Variables
    ExtendedValue = db.Column(db.String(200))


class ArchivedLayout(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variables
    FormDef = db.Column(db.Integer, db.ForeignKey('form_def.id'), nullable=False)

    # Attribute Variables
    OID = db.Column(db.String(128), unique=True, nullable=False)
    PdfFileName = db.Column(db.String(50), nullable=False)
    PresentationOID = db.Column(db.String(128))


class MethodDef(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variable
    MetaDataVersion = db.Column(db.Integer, db.ForeignKey('meta_data_version.id'), nullable=False)

    # Child Variable
    Description = db.relationship('Description', backref='ItemGroupDef', lazy=True)
    ItemRef = db.relationship('FormalExpression', backref='ItemGroupDef', lazy=True)
    Alias = db.relationship('Alias', backref='ItemGroupDef', lazy=True)

    # Attribute Variable
    OID = db.Column(db.String(128), unique=True, nullable=False)
    Name = db.Column(db.String(50), nullable=False)
    # TODO Change to enum in the future
    Type = db.Column(db.String(20), nullable=False)


class Presentation(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variable
    MetaDataVersion = db.Column(db.Integer, db.ForeignKey('meta_data_version.id'), nullable=False)

    # Attribute Variables
    OID = db.Column(db.String(128), unique=True, nullable=False)
    lang = db.Column(db.String(50))

    text = db.Column(db.String(200))


class ConditionDef(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variable
    MetaDataVersion = db.Column(db.Integer, db.ForeignKey('meta_data_version.id'), nullable=False)

    # Child Variable
    Description = db.relationship('Description', backref='ItemGroupDef', lazy=True)
    ItemRef = db.relationship('FormalExpression', backref='ItemGroupDef', lazy=True)
    Alias = db.relationship('Alias', backref='ItemGroupDef', lazy=True)

    # Attribute Variable
    OID = db.Column(db.String(128), unique=True, nullable=False)
    Name = db.Column(db.String(50), nullable=False)


class FormalExpression(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Parent Variables
    ConditionDef = db.Column(db.Integer, db.ForeignKey('condition_def.id'), nullable=False)
    MethodDef = db.Column(db.Integer, db.ForeignKey('method_def.id'), nullable=False)
    RangeCheck = db.Column(db.Integer, db.ForeignKey('range_check.id'), nullable=False)

    # Child Variables
    PCDATA = db.Column(db.String(200), nullable=False)

    # Attribute Variables
    Context = db.Column(db.String(200), nullable=False)


# class AdminData(db.Model):
#
#     body_keys = ["User", "Location", "SignatureDef"]
#     attributes_keys = ["StudyOID"]
#
#
# class ODMUser(db.Model):
#     body_keys = ["LoginName", "DisplayName", "FullName", "FirstName", "LastName", "Organization",
#                  "Address", "Email", "Picture", "Pager", "Fax", "Phone", "LocationRef",
#                  "Certificate"]
#     attributes_keys = ["OID", "UserType"]
#
#
# class ODMLoginName(db.Model):
#     pass
#
#
# class ODMDisplayName(db.Model):
#     pass
#
#
# class ODMFullName(db.Model):
#     pass
#
#
# class ODMFirstName(db.Model):
#     pass
#
#
# class ODMLastName(db.Model):
#     pass
#
#
# class ODMOrganization(db.Model):
#     pass
#
#
# class ODMAddress(db.Model):
#     body_keys = ["StreetName", "City", "StateProv", "Country", "PostalCode", "OtherText"]
#     attributes_keys = []
#
#
# class ODMStreetName(db.Model):
#     pass
#
#
# class ODMCity(db.Model):
#     pass
#
#
# class ODMStateProv(db.Model):
#     pass
#
#
# class ODMCountry(db.Model):
#     pass
#
#
# class ODMPostalCode(db.Model):
#     pass
#
#
# class ODMOtherText(db.Model):
#     pass
#
#
# class ODMEmail(db.Model):
#     pass
#
#
# class ODMPicture(db.Model):
#     body_keys = None
#     attributes_keys = ["PictureFileName", "ImageType"]
#
#
# class ODMPager(db.Model):
#     pass
#
#
# class ODMFax(db.Model):
#     pass
#
#
# class ODMPhone(db.Model):
#     pass
#
#
# class ODMLocationRef(db.Model):
#     body_keys = None
#     attributes_keys = ["LocationOID"]
#
#
# class ODMCertificate(db.Model):
#     pass
#
#
# class ODMLocation(db.Model):
#     body_keys = ["MetaDataVersionRef"]
#     attributes_keys = ["OID", "Name", "LocationType"]
#
#
# class ODMMetaDataVersionRef(db.Model):
#     body_keys = None
#     attributes_keys = ["StudyOID", "MetaDataVersionOID", "EffectiveDate"]
#
#
# class ODMSignatureDef(db.Model):
#     body_keys = ["Meaning", "LegalReason"]
#     attributes_keys = ["OID", "Methodology"]
#
#
# class ODMMeaning(db.Model):
#     pass
#
#
# class ODMLegalReason(db.Model):
#     pass
#
#
# class ODMReferenceData(db.Model):
#     body_keys = ["ItemGroupData", "AuditRecords", "Signatures", "Annotations"]
#     attributes_keys = ["StudyOID", "MetaDataVersionOID"]
#
#
# class ODMClinicalData(db.Model):
#     body_keys = ["SubjectData", "AuditRecords", "Signatures", "Annotations"]
#     attributes_keys = ["StudyOID", "MetaDataVersionOID"]
#
#
# class ODMSubjectData(db.Model):
#
#     body_keys = ["SubjectData", "AuditRecords", "Signatures", "Annotation", "StudyEventData"]
#     attributes_keys = ["StudyOID", "MetaDataVersionOID"]
#
#
# class ODMStudyEventData(db.Model):
#     body_keys = ["AuditRecords", "Signatures", "Annotation", "FormData"]
#     attributes_keys = ["StudyEventOID", "StudyEventRepeatKey", "TransactionType"]
#
#
# class ODMFormData(db.Model):
#     body_keys = ["AuditRecords", "Signatures", "ArchiveLayoutRef", "Annotation", "ItemGroupData"]
#     attributes_keys = ["FormOID", "FormRepeatKey", "TransactionType"]
#
#
# class ODMItemGroupData(db.Model):
#     body_keys = ["AuditRecords", "Signatures", "ArchiveLayoutRef", "Annotation", "ItemData"]
#     attributes_keys = ["FormOID", "FormRepeatKey", "TransactionType"]
#
#
# class ODMItemData(db.Model):
#     body_keys = ["AuditRecords", "Signatures", "MeasurementUnitRef", "Annotation"]
#     attributes_keys = ["ItemOID", "TransactionType", "Value", "IsNull"]
#
#
# class ODMArchiveLayoutRef(db.Model):
#     body_keys = None
#     attributes_keys = ["ArchiveLayoutOID"]
#
#
# class ODMAuditRecord(db.Model):
#     body_keys = ['UserRef', "LocationRef", "DateTimeStamp", "ReasonForChange", "SourceID"]
#     attributes_keys = ["EditPoint", "UserImputationMehtod", "ID"]
#
#
# class ODMUserRef(db.Model):
#     body_keys = None
#     attributes_keys = ["UserOID"]
#
#
# class ODMDateTimeStamp(db.Model):
#     pass
#
#
# class ODMReasonForChange(db.Model):
#     pass
#
#
# class ODMSourceID(db.Model):
#     pass
#
#
# class ODMSignature(db.Model):
#     body_keys = ["UserRef", "LocationRef", "SignatureRef", "DateTimeStamp"]
#     attributes_keys = ["ID"]
#
#
# class ODMSignatureRef(db.Model):
#     body_keys = None
#     attributes_keys = ["SignatureOID"]
#
#
# class ODMAnnotation(db.Model):
#     body_keys = ["Comment", "Flag"]
#     attributes_keys = ["SeqNum", "TransactionType", "ID"]
#
#
# class ODMComment(db.Model):
#     body_keys = []
#     attributes_keys = ["SponsorOrSite"]
#
#
# class ODMFlag(db.Model):
#     body_keys = ["FlagValue", "FlagType"]
#     attributes_keys = []
#
#
# class ODMFlagValue(db.Model):
#     body_keys = []
#     attributes_keys = ["CodeListOID"]
#
#
# class ODMFlagType(db.Model):
#     body_keys = []
#     attributes_keys = ["CodeListOID"]
#
#
# class ODMInvestigatorRef(db.Model):
#     body_keys = None
#     attributes_keys = ["UserOID"]
#
#
# class ODMSiteRef(db.Model):
#     body_keys = None
#     attributes_keys = ["LocationOID"]
#
#
# class ODMAuditRecords(db.Model):
#     body_keys = ['AuditRecord']
#     attributes_keys = []
#
#
# class ODMSignatures(db.Model):
#     body_keys = ['Signature']
#     attributes_keys = []
#
#
# class ODMAnnotations(db.Model):
#     body_keys = ['Annotation']
#     attributes_keys = []
#
#
# class ODMAssociations(db.Model):
#     body_keys = ['KeySet', "Annotation"]
#     attributes_keys = ["StudyOID", "MetaDataVersionOID"]
#
#
# class ODMKeySet(db.Model):
#     body_keys = None
#     attributes_keys = ["StudyOID", "StudyKey", "StudyEventOID", "StudyEventRepeatKey", "FormOID",
#                        "FormRepeatKey", "ItemGroupOID", "ItemGroupRepeatKey", "ItemOID"]
#
#
# class ODMSignature(db.Model):
#     body_keys = ["SignedInfo", "SignatureValue", "KeyInfo", "Object"]
#     attributes_keys = ["xmlns", "Id"]


# define xml extension
# class ODMDocumentRef(db.Model):
#     body_keys = ["PDFPageRef"]
#     attributes_keys = ['leafID']
#
#
# class ODMStandards(db.Model):
#     body_keys = ["Standard"]
#     attributes_keys = []
#
#
# class ODMStandard(db.Model):
#     body_keys = None
#     attributes_keys = ['OID', "Name", "Type", "PublishingSet", "Version", "Status",
#                                 "CommentOID"]
#
#
# class ODMSupplementalDoc(db.Model):
#     body_keys = ['DocumentRef']
#     attributes_keys = []
#
#
# class ODMValueListRef(db.Model):
#     body_keys = None
#     attributes_keys = ['ValueListOID']
#
#
# class ODMValueListDef(db.Model):
#     body_keys = ["ItemRef"]
#     attributes_keys = ["OID"]
#
#
# class ODMWhereClauseRef(db.Model):
#     body_keys = None
#     attributes_keys = ["WhereClauseOID"]
#
#
# class ODMWhereClauseDef(db.Model):
#     body_keys = ["RangeCheck"]
#     attributes_keys = ['OID', "CommentOID"]
#
#
# class ODMOrigin(db.Model):
#     body_keys = ["Description", 'DocumentRef']
#     attributes_keys = ['Type', 'Source']
#
#
# class ODMPDFPageRef(db.Model):
#     body_keys = None
#     attributes_keys = ['PageRefs', 'FirstPage', 'LastPage', 'Type', 'Title']
#
#
# class ODMClass(db.Model):
#     body_keys = ['Subclass']
#     attributes_keys = ['Name']
#
#
# class ODMSubClass(db.Model):
#     body_keys = None
#     attributes_keys = ["Name", "ParentClass"]
#
#
# class ODMleaf(db.Model):
#     body_keys = ["title"]
#     attributes_keys = ['ID', 'xlink:href']
#
#
# class ODMCommentDef(db.Model):
#     body_keys = ['Description']
#     attributes_keys = ['OID']
#
#
# # EDETEK Extension
# class ODMLabel(db.Model):
#     pass
#
#
# class ODMIsShared(db.Model):
#     pass
#
#
# class ODMAttribute(db.Model):
#     body_keys = None
#     attributes_keys = ["Name"]
#
#
# class ODMBasicValidation(db.Model):
#     pass
#
#
# class ODMStandardStatus(db.Model):
#     pass


# #
# # # ODM example
# # # tree = etree.parse(r"E:\Work\EDETEK\Python\edetek\edetek\data\standard\CDISC_ODM_example_1"
# # #                         r".xml")
# # # root = tree.getroot()
# # # odm = ODM.create_object_from_xml(root)
# #
# # # Define example (ET)
# # # tree = ET.parse(r"E:\Work\EDETEK\Python\edetek\edetek\data\DefineV21ReleasePackage\DefineV21"
# # #                 r"\examples\DefineXML-2-1-SDTM\defineV21-SDTM.xml")
# # # root = tree.getroot()
# # # define = ODM.create_object_from_xml(root)
# #
# #
# # # Define example (lxml)
# # # tree = ET.parse(r"E:\Work\EDETEK\Python\edetek\edetek\data\DefineV21ReleasePackage\DefineV21"
# # #                 r"\examples\DefineXML-2-1-SDTM\defineV21-SDTM.xml")
# # # root = tree.getroot()
# # # define = ODM.create_object_from_xml(root)
# #
# #
# # # Conform example (lxml)
# # tree = etree.parse(r"E:\Work\EDETEK\Python\edetek\edetek\data\standard\Validation Rest.xml")
# # # tree = ET.parse(r"E:\Work\EDETEK\Python\edetek\edetek\data\DefineV21ReleasePackage\DefineV21"
# # #                 r"\examples\DefineXML-2-1-SDTM\defineV21-SDTM.xml")
# #
# # root = tree.getroot()
# # define = ODMODM.create_object_from_xml(root)
# # root = define.create_xml_from_object(define)
# # tree = root.getroottree()
# # tree.write("temp.xml", pretty_print=True)
# # # study_view = define.study_view()
