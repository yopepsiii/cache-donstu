from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GroupInfo(_message.Message):
    __slots__ = ("name", "groupID")
    NAME_FIELD_NUMBER: _ClassVar[int]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    name: str
    groupID: int
    def __init__(self, name: _Optional[str] = ..., groupID: _Optional[int] = ...) -> None: ...

class LessonInfo(_message.Message):
    __slots__ = ("moduleName", "theme", "aud", "groups")
    MODULENAME_FIELD_NUMBER: _ClassVar[int]
    THEME_FIELD_NUMBER: _ClassVar[int]
    AUD_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    moduleName: str
    theme: str
    aud: str
    groups: _containers.RepeatedCompositeFieldContainer[GroupInfo]
    def __init__(self, moduleName: _Optional[str] = ..., theme: _Optional[str] = ..., aud: _Optional[str] = ..., groups: _Optional[_Iterable[_Union[GroupInfo, _Mapping]]] = ...) -> None: ...

class Lesson(_message.Message):
    __slots__ = ("name", "color", "start", "end", "type", "dateChange", "educationSpaceID", "isControlEvent", "info")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATECHANGE_FIELD_NUMBER: _ClassVar[int]
    EDUCATIONSPACEID_FIELD_NUMBER: _ClassVar[int]
    ISCONTROLEVENT_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    name: str
    color: str
    start: str
    end: str
    type: str
    dateChange: str
    educationSpaceID: int
    isControlEvent: bool
    info: LessonInfo
    def __init__(self, name: _Optional[str] = ..., color: _Optional[str] = ..., start: _Optional[str] = ..., end: _Optional[str] = ..., type: _Optional[str] = ..., dateChange: _Optional[str] = ..., educationSpaceID: _Optional[int] = ..., isControlEvent: bool = ..., info: _Optional[_Union[LessonInfo, _Mapping]] = ...) -> None: ...

class GetScheduleRequest(_message.Message):
    __slots__ = ("educationSpaceID", "month", "showJournalFilled", "aud", "moduleID", "typeID", "themeID", "kafID", "groupsIDs", "studentsIDs", "teachersIDs", "year", "showAll", "access_token")
    EDUCATIONSPACEID_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    SHOWJOURNALFILLED_FIELD_NUMBER: _ClassVar[int]
    AUD_FIELD_NUMBER: _ClassVar[int]
    MODULEID_FIELD_NUMBER: _ClassVar[int]
    TYPEID_FIELD_NUMBER: _ClassVar[int]
    THEMEID_FIELD_NUMBER: _ClassVar[int]
    KAFID_FIELD_NUMBER: _ClassVar[int]
    GROUPSIDS_FIELD_NUMBER: _ClassVar[int]
    STUDENTSIDS_FIELD_NUMBER: _ClassVar[int]
    TEACHERSIDS_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    SHOWALL_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    educationSpaceID: int
    month: int
    showJournalFilled: bool
    aud: str
    moduleID: int
    typeID: int
    themeID: int
    kafID: int
    groupsIDs: _containers.RepeatedScalarFieldContainer[int]
    studentsIDs: _containers.RepeatedScalarFieldContainer[int]
    teachersIDs: _containers.RepeatedScalarFieldContainer[int]
    year: str
    showAll: bool
    access_token: str
    def __init__(self, educationSpaceID: _Optional[int] = ..., month: _Optional[int] = ..., showJournalFilled: bool = ..., aud: _Optional[str] = ..., moduleID: _Optional[int] = ..., typeID: _Optional[int] = ..., themeID: _Optional[int] = ..., kafID: _Optional[int] = ..., groupsIDs: _Optional[_Iterable[int]] = ..., studentsIDs: _Optional[_Iterable[int]] = ..., teachersIDs: _Optional[_Iterable[int]] = ..., year: _Optional[str] = ..., showAll: bool = ..., access_token: _Optional[str] = ...) -> None: ...

class GetScheduleResponse(_message.Message):
    __slots__ = ("lessons",)
    LESSONS_FIELD_NUMBER: _ClassVar[int]
    lessons: _containers.RepeatedCompositeFieldContainer[Lesson]
    def __init__(self, lessons: _Optional[_Iterable[_Union[Lesson, _Mapping]]] = ...) -> None: ...
