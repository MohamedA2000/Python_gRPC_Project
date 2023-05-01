# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: greet.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bgreet.proto\x12\x05greet\".\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08greeting\x18\x02 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"E\n\x0c\x44\x65layedReply\x12\x0f\n\x07message\x18\x01 \x01(\t\x12$\n\x07request\x18\x02 \x03(\x0b\x32\x13.greet.HelloRequest\"\x07\n\x05\x45mpty\"\x1a\n\x0bRoverNumber\x12\x0b\n\x03num\x18\x01 \x01(\r\"6\n\rRoverCommands\x12\x13\n\x0bhasCommands\x18\x01 \x01(\x08\x12\x10\n\x08\x63ommands\x18\x02 \x01(\t\"\x18\n\x08RoverMap\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"\"\n\nMineNumber\x12\t\n\x01i\x18\x01 \x01(\r\x12\t\n\x01j\x18\x02 \x01(\r\"(\n\x10MineSerialNumber\x12\x14\n\x0cserialNumber\x18\x01 \x01(\t\"1\n\x0cMineDisarmed\x12\x14\n\x0cserialNumber\x18\x01 \x01(\t\x12\x0b\n\x03pin\x18\x02 \x01(\r\"/\n\x0bRoverStatus\x12\x0b\n\x03num\x18\x01 \x01(\r\x12\x13\n\x0bhasExploded\x18\x02 \x01(\x08\"\x14\n\x03Pin\x12\r\n\x05value\x18\x01 \x01(\x04\x32\xca\x04\n\x07Greeter\x12\x32\n\x08SayHello\x12\x13.greet.HelloRequest\x1a\x11.greet.HelloReply\x12;\n\x0fParrotSaysHello\x12\x13.greet.HelloRequest\x1a\x11.greet.HelloReply0\x01\x12\x43\n\x15\x43hattyClientSaysHello\x12\x13.greet.HelloRequest\x1a\x13.greet.DelayedReply(\x01\x12>\n\x10InteractingHello\x12\x13.greet.HelloRequest\x1a\x11.greet.HelloReply(\x01\x30\x01\x12+\n\x08\x46\x65tchMap\x12\x0c.greet.Empty\x1a\x0f.greet.RoverMap\"\x00\x12;\n\rFetchCommands\x12\x12.greet.RoverNumber\x1a\x14.greet.RoverCommands\"\x00\x12\x43\n\x13GetMineSerialNumber\x12\x11.greet.MineNumber\x1a\x17.greet.MineSerialNumber\"\x00\x12\x37\n\x11NotifyRoverStatus\x12\x12.greet.RoverStatus\x1a\x0c.greet.Empty\"\x00\x12\x39\n\x12NotifyDisarmedMine\x12\x13.greet.MineDisarmed\x1a\x0c.greet.Empty\"\x00\x12&\n\x08PrintPin\x12\n.greet.Pin\x1a\x0c.greet.Empty\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'greet_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HELLOREQUEST._serialized_start=22
  _HELLOREQUEST._serialized_end=68
  _HELLOREPLY._serialized_start=70
  _HELLOREPLY._serialized_end=99
  _DELAYEDREPLY._serialized_start=101
  _DELAYEDREPLY._serialized_end=170
  _EMPTY._serialized_start=172
  _EMPTY._serialized_end=179
  _ROVERNUMBER._serialized_start=181
  _ROVERNUMBER._serialized_end=207
  _ROVERCOMMANDS._serialized_start=209
  _ROVERCOMMANDS._serialized_end=263
  _ROVERMAP._serialized_start=265
  _ROVERMAP._serialized_end=289
  _MINENUMBER._serialized_start=291
  _MINENUMBER._serialized_end=325
  _MINESERIALNUMBER._serialized_start=327
  _MINESERIALNUMBER._serialized_end=367
  _MINEDISARMED._serialized_start=369
  _MINEDISARMED._serialized_end=418
  _ROVERSTATUS._serialized_start=420
  _ROVERSTATUS._serialized_end=467
  _PIN._serialized_start=469
  _PIN._serialized_end=489
  _GREETER._serialized_start=492
  _GREETER._serialized_end=1078
# @@protoc_insertion_point(module_scope)
