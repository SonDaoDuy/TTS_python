from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TextMessage(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class SpeechResponse(_message.Message):
    __slots__ = ("data", "data_shape", "frame_rate")
    DATA_FIELD_NUMBER: _ClassVar[int]
    DATA_SHAPE_FIELD_NUMBER: _ClassVar[int]
    FRAME_RATE_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    data_shape: str
    frame_rate: int
    def __init__(self, data: _Optional[bytes] = ..., data_shape: _Optional[str] = ..., frame_rate: _Optional[int] = ...) -> None: ...
