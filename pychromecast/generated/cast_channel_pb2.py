# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cast_channel.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x12\x63\x61st_channel.proto\x12\x1b\x65xtensions.api.cast_channel"\xe3\x02\n\x0b\x43\x61stMessage\x12R\n\x10protocol_version\x18\x01 \x02(\x0e\x32\x38.extensions.api.cast_channel.CastMessage.ProtocolVersion\x12\x11\n\tsource_id\x18\x02 \x02(\t\x12\x16\n\x0e\x64\x65stination_id\x18\x03 \x02(\t\x12\x11\n\tnamespace\x18\x04 \x02(\t\x12J\n\x0cpayload_type\x18\x05 \x02(\x0e\x32\x34.extensions.api.cast_channel.CastMessage.PayloadType\x12\x14\n\x0cpayload_utf8\x18\x06 \x01(\t\x12\x16\n\x0epayload_binary\x18\x07 \x01(\x0c"!\n\x0fProtocolVersion\x12\x0e\n\nCASTV2_1_0\x10\x00"%\n\x0bPayloadType\x12\n\n\x06STRING\x10\x00\x12\n\n\x06\x42INARY\x10\x01"\xce\x01\n\rAuthChallenge\x12]\n\x13signature_algorithm\x18\x01 \x01(\x0e\x32/.extensions.api.cast_channel.SignatureAlgorithm:\x0fRSASSA_PKCS1v15\x12\x14\n\x0csender_nonce\x18\x02 \x01(\x0c\x12H\n\x0ehash_algorithm\x18\x03 \x01(\x0e\x32*.extensions.api.cast_channel.HashAlgorithm:\x04SHA1"\xb0\x02\n\x0c\x41uthResponse\x12\x11\n\tsignature\x18\x01 \x02(\x0c\x12\x1f\n\x17\x63lient_auth_certificate\x18\x02 \x02(\x0c\x12 \n\x18intermediate_certificate\x18\x03 \x03(\x0c\x12]\n\x13signature_algorithm\x18\x04 \x01(\x0e\x32/.extensions.api.cast_channel.SignatureAlgorithm:\x0fRSASSA_PKCS1v15\x12\x14\n\x0csender_nonce\x18\x05 \x01(\x0c\x12H\n\x0ehash_algorithm\x18\x06 \x01(\x0e\x32*.extensions.api.cast_channel.HashAlgorithm:\x04SHA1\x12\x0b\n\x03\x63rl\x18\x07 \x01(\x0c"\xa3\x01\n\tAuthError\x12\x44\n\nerror_type\x18\x01 \x02(\x0e\x32\x30.extensions.api.cast_channel.AuthError.ErrorType"P\n\tErrorType\x12\x12\n\x0eINTERNAL_ERROR\x10\x00\x12\n\n\x06NO_TLS\x10\x01\x12#\n\x1fSIGNATURE_ALGORITHM_UNAVAILABLE\x10\x02"\xc6\x01\n\x11\x44\x65viceAuthMessage\x12=\n\tchallenge\x18\x01 \x01(\x0b\x32*.extensions.api.cast_channel.AuthChallenge\x12;\n\x08response\x18\x02 \x01(\x0b\x32).extensions.api.cast_channel.AuthResponse\x12\x35\n\x05\x65rror\x18\x03 \x01(\x0b\x32&.extensions.api.cast_channel.AuthError*J\n\x12SignatureAlgorithm\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x13\n\x0fRSASSA_PKCS1v15\x10\x01\x12\x0e\n\nRSASSA_PSS\x10\x02*%\n\rHashAlgorithm\x12\x08\n\x04SHA1\x10\x00\x12\n\n\x06SHA256\x10\x01\x42\x02H\x03'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "cast_channel_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals["DESCRIPTOR"]._serialized_options = b"H\003"
    _globals["_SIGNATUREALGORITHM"]._serialized_start = 1292
    _globals["_SIGNATUREALGORITHM"]._serialized_end = 1366
    _globals["_HASHALGORITHM"]._serialized_start = 1368
    _globals["_HASHALGORITHM"]._serialized_end = 1405
    _globals["_CASTMESSAGE"]._serialized_start = 52
    _globals["_CASTMESSAGE"]._serialized_end = 407
    _globals["_CASTMESSAGE_PROTOCOLVERSION"]._serialized_start = 335
    _globals["_CASTMESSAGE_PROTOCOLVERSION"]._serialized_end = 368
    _globals["_CASTMESSAGE_PAYLOADTYPE"]._serialized_start = 370
    _globals["_CASTMESSAGE_PAYLOADTYPE"]._serialized_end = 407
    _globals["_AUTHCHALLENGE"]._serialized_start = 410
    _globals["_AUTHCHALLENGE"]._serialized_end = 616
    _globals["_AUTHRESPONSE"]._serialized_start = 619
    _globals["_AUTHRESPONSE"]._serialized_end = 923
    _globals["_AUTHERROR"]._serialized_start = 926
    _globals["_AUTHERROR"]._serialized_end = 1089
    _globals["_AUTHERROR_ERRORTYPE"]._serialized_start = 1009
    _globals["_AUTHERROR_ERRORTYPE"]._serialized_end = 1089
    _globals["_DEVICEAUTHMESSAGE"]._serialized_start = 1092
    _globals["_DEVICEAUTHMESSAGE"]._serialized_end = 1290
# @@protoc_insertion_point(module_scope)
