# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: first_service.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x66irst_service.proto\x12\tttspython\"\x1b\n\x0bTextMessage\x12\x0c\n\x04text\x18\x01 \x01(\t\"F\n\x0eSpeechResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x12\n\ndata_shape\x18\x02 \x01(\t\x12\x12\n\nframe_rate\x18\x03 \x01(\x03\x32N\n\tTTSPython\x12\x41\n\nConvertTTS\x12\x16.ttspython.TextMessage\x1a\x19.ttspython.SpeechResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'first_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TEXTMESSAGE']._serialized_start=34
  _globals['_TEXTMESSAGE']._serialized_end=61
  _globals['_SPEECHRESPONSE']._serialized_start=63
  _globals['_SPEECHRESPONSE']._serialized_end=133
  _globals['_TTSPYTHON']._serialized_start=135
  _globals['_TTSPYTHON']._serialized_end=213
# @@protoc_insertion_point(module_scope)
