from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Lesson(_message.Message):
    __slots__ = ("name", "start_time", "end_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    start_time: str
    end_time: str
    def __init__(self, name: _Optional[str] = ..., start_time: _Optional[str] = ..., end_time: _Optional[str] = ...) -> None: ...

class GetScheduleRequest(_message.Message):
    __slots__ = ("educationSpaceID", "month", "showJournalFilled", "years", "showAll")
    EDUCATIONSPACEID_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    SHOWJOURNALFILLED_FIELD_NUMBER: _ClassVar[int]
    YEARS_FIELD_NUMBER: _ClassVar[int]
    SHOWALL_FIELD_NUMBER: _ClassVar[int]
    educationSpaceID: int
    month: int
    showJournalFilled: bool
    years: str
    showAll: bool
    def __init__(self, educationSpaceID: _Optional[int] = ..., month: _Optional[int] = ..., showJournalFilled: bool = ..., years: _Optional[str] = ..., showAll: bool = ...) -> None: ...

class GetScheduleResponse(_message.Message):
    __slots__ = ("lessons",)
    LESSONS_FIELD_NUMBER: _ClassVar[int]
    lessons: _containers.RepeatedCompositeFieldContainer[Lesson]
    def __init__(self, lessons: _Optional[_Iterable[_Union[Lesson, _Mapping]]] = ...) -> None: ...
