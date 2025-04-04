# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: logging.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\rlogging.proto\x12!extensions.api.cast_channel.proto"\xfd\x04\n\x0bSocketEvent\x12:\n\x04type\x18\x01 \x01(\x0e\x32,.extensions.api.cast_channel.proto.EventType\x12\x18\n\x10timestamp_micros\x18\x02 \x01(\x03\x12\x0f\n\x07\x64\x65tails\x18\x03 \x01(\t\x12\x18\n\x10net_return_value\x18\x04 \x01(\x05\x12\x19\n\x11message_namespace\x18\x05 \x01(\t\x12\x42\n\x0bready_state\x18\x06 \x01(\x0e\x32-.extensions.api.cast_channel.proto.ReadyState\x12L\n\x10\x63onnection_state\x18\x07 \x01(\x0e\x32\x32.extensions.api.cast_channel.proto.ConnectionState\x12@\n\nread_state\x18\x08 \x01(\x0e\x32,.extensions.api.cast_channel.proto.ReadState\x12\x42\n\x0bwrite_state\x18\t \x01(\x0e\x32-.extensions.api.cast_channel.proto.WriteState\x12\x42\n\x0b\x65rror_state\x18\n \x01(\x0e\x32-.extensions.api.cast_channel.proto.ErrorState\x12^\n\x1a\x63hallenge_reply_error_type\x18\x0b \x01(\x0e\x32:.extensions.api.cast_channel.proto.ChallengeReplyErrorType\x12\x16\n\x0enss_error_code\x18\x0c \x01(\x05"\xf4\x01\n\x15\x41ggregatedSocketEvent\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x13\n\x0b\x65ndpoint_id\x18\x02 \x01(\x05\x12I\n\x11\x63hannel_auth_type\x18\x03 \x01(\x0e\x32..extensions.api.cast_channel.proto.ChannelAuth\x12\x44\n\x0csocket_event\x18\x04 \x03(\x0b\x32..extensions.api.cast_channel.proto.SocketEvent\x12\x12\n\nbytes_read\x18\x05 \x01(\x03\x12\x15\n\rbytes_written\x18\x06 \x01(\x03"\xb1\x01\n\x03Log\x12Y\n\x17\x61ggregated_socket_event\x18\x01 \x03(\x0b\x32\x38.extensions.api.cast_channel.proto.AggregatedSocketEvent\x12,\n$num_evicted_aggregated_socket_events\x18\x02 \x01(\x05\x12!\n\x19num_evicted_socket_events\x18\x03 \x01(\x05*\xc0\x06\n\tEventType\x12\x16\n\x12\x45VENT_TYPE_UNKNOWN\x10\x00\x12\x17\n\x13\x43\x41ST_SOCKET_CREATED\x10\x01\x12\x17\n\x13READY_STATE_CHANGED\x10\x02\x12\x1c\n\x18\x43ONNECTION_STATE_CHANGED\x10\x03\x12\x16\n\x12READ_STATE_CHANGED\x10\x04\x12\x17\n\x13WRITE_STATE_CHANGED\x10\x05\x12\x17\n\x13\x45RROR_STATE_CHANGED\x10\x06\x12\x12\n\x0e\x43ONNECT_FAILED\x10\x07\x12\x16\n\x12TCP_SOCKET_CONNECT\x10\x08\x12\x1d\n\x19TCP_SOCKET_SET_KEEP_ALIVE\x10\t\x12\x18\n\x14SSL_CERT_WHITELISTED\x10\n\x12\x16\n\x12SSL_SOCKET_CONNECT\x10\x0b\x12\x15\n\x11SSL_INFO_OBTAINED\x10\x0c\x12\x1b\n\x17\x44\x45R_ENCODED_CERT_OBTAIN\x10\r\x12\x1c\n\x18RECEIVED_CHALLENGE_REPLY\x10\x0e\x12\x18\n\x14\x41UTH_CHALLENGE_REPLY\x10\x0f\x12\x15\n\x11\x43ONNECT_TIMED_OUT\x10\x10\x12\x17\n\x13SEND_MESSAGE_FAILED\x10\x11\x12\x14\n\x10MESSAGE_ENQUEUED\x10\x12\x12\x10\n\x0cSOCKET_WRITE\x10\x13\x12\x13\n\x0fMESSAGE_WRITTEN\x10\x14\x12\x0f\n\x0bSOCKET_READ\x10\x15\x12\x10\n\x0cMESSAGE_READ\x10\x16\x12\x11\n\rSOCKET_CLOSED\x10\x19\x12\x1f\n\x1bSSL_CERT_EXCESSIVE_LIFETIME\x10\x1a\x12\x1b\n\x17\x43HANNEL_POLICY_ENFORCED\x10\x1b\x12\x1f\n\x1bTCP_SOCKET_CONNECT_COMPLETE\x10\x1c\x12\x1f\n\x1bSSL_SOCKET_CONNECT_COMPLETE\x10\x1d\x12\x1d\n\x19SSL_SOCKET_CONNECT_FAILED\x10\x1e\x12\x1e\n\x1aSEND_AUTH_CHALLENGE_FAILED\x10\x1f\x12 \n\x1c\x41UTH_CHALLENGE_REPLY_INVALID\x10 \x12\x14\n\x10PING_WRITE_ERROR\x10!*(\n\x0b\x43hannelAuth\x12\x07\n\x03SSL\x10\x01\x12\x10\n\x0cSSL_VERIFIED\x10\x02*\x85\x01\n\nReadyState\x12\x14\n\x10READY_STATE_NONE\x10\x01\x12\x1a\n\x16READY_STATE_CONNECTING\x10\x02\x12\x14\n\x10READY_STATE_OPEN\x10\x03\x12\x17\n\x13READY_STATE_CLOSING\x10\x04\x12\x16\n\x12READY_STATE_CLOSED\x10\x05*\x8f\x03\n\x0f\x43onnectionState\x12\x16\n\x12\x43ONN_STATE_UNKNOWN\x10\x01\x12\x1a\n\x16\x43ONN_STATE_TCP_CONNECT\x10\x02\x12#\n\x1f\x43ONN_STATE_TCP_CONNECT_COMPLETE\x10\x03\x12\x1a\n\x16\x43ONN_STATE_SSL_CONNECT\x10\x04\x12#\n\x1f\x43ONN_STATE_SSL_CONNECT_COMPLETE\x10\x05\x12"\n\x1e\x43ONN_STATE_AUTH_CHALLENGE_SEND\x10\x06\x12+\n\'CONN_STATE_AUTH_CHALLENGE_SEND_COMPLETE\x10\x07\x12,\n(CONN_STATE_AUTH_CHALLENGE_REPLY_COMPLETE\x10\x08\x12\x1c\n\x18\x43ONN_STATE_START_CONNECT\x10\t\x12\x17\n\x13\x43ONN_STATE_FINISHED\x10\x64\x12\x14\n\x10\x43ONN_STATE_ERROR\x10\x65\x12\x16\n\x12\x43ONN_STATE_TIMEOUT\x10\x66*\xa5\x01\n\tReadState\x12\x16\n\x12READ_STATE_UNKNOWN\x10\x01\x12\x13\n\x0fREAD_STATE_READ\x10\x02\x12\x1c\n\x18READ_STATE_READ_COMPLETE\x10\x03\x12\x1a\n\x16READ_STATE_DO_CALLBACK\x10\x04\x12\x1b\n\x17READ_STATE_HANDLE_ERROR\x10\x05\x12\x14\n\x10READ_STATE_ERROR\x10\x64*\xc4\x01\n\nWriteState\x12\x17\n\x13WRITE_STATE_UNKNOWN\x10\x01\x12\x15\n\x11WRITE_STATE_WRITE\x10\x02\x12\x1e\n\x1aWRITE_STATE_WRITE_COMPLETE\x10\x03\x12\x1b\n\x17WRITE_STATE_DO_CALLBACK\x10\x04\x12\x1c\n\x18WRITE_STATE_HANDLE_ERROR\x10\x05\x12\x15\n\x11WRITE_STATE_ERROR\x10\x64\x12\x14\n\x10WRITE_STATE_IDLE\x10\x65*\xdb\x02\n\nErrorState\x12\x16\n\x12\x43HANNEL_ERROR_NONE\x10\x01\x12"\n\x1e\x43HANNEL_ERROR_CHANNEL_NOT_OPEN\x10\x02\x12&\n"CHANNEL_ERROR_AUTHENTICATION_ERROR\x10\x03\x12\x1f\n\x1b\x43HANNEL_ERROR_CONNECT_ERROR\x10\x04\x12\x1e\n\x1a\x43HANNEL_ERROR_SOCKET_ERROR\x10\x05\x12!\n\x1d\x43HANNEL_ERROR_TRANSPORT_ERROR\x10\x06\x12!\n\x1d\x43HANNEL_ERROR_INVALID_MESSAGE\x10\x07\x12$\n CHANNEL_ERROR_INVALID_CHANNEL_ID\x10\x08\x12!\n\x1d\x43HANNEL_ERROR_CONNECT_TIMEOUT\x10\t\x12\x19\n\x15\x43HANNEL_ERROR_UNKNOWN\x10\n*\xb0\x06\n\x17\x43hallengeReplyErrorType\x12\x1e\n\x1a\x43HALLENGE_REPLY_ERROR_NONE\x10\x01\x12)\n%CHALLENGE_REPLY_ERROR_PEER_CERT_EMPTY\x10\x02\x12,\n(CHALLENGE_REPLY_ERROR_WRONG_PAYLOAD_TYPE\x10\x03\x12$\n CHALLENGE_REPLY_ERROR_NO_PAYLOAD\x10\x04\x12\x30\n,CHALLENGE_REPLY_ERROR_PAYLOAD_PARSING_FAILED\x10\x05\x12\'\n#CHALLENGE_REPLY_ERROR_MESSAGE_ERROR\x10\x06\x12%\n!CHALLENGE_REPLY_ERROR_NO_RESPONSE\x10\x07\x12/\n+CHALLENGE_REPLY_ERROR_FINGERPRINT_NOT_FOUND\x10\x08\x12-\n)CHALLENGE_REPLY_ERROR_CERT_PARSING_FAILED\x10\t\x12\x37\n3CHALLENGE_REPLY_ERROR_CERT_NOT_SIGNED_BY_TRUSTED_CA\x10\n\x12\x33\n/CHALLENGE_REPLY_ERROR_CANNOT_EXTRACT_PUBLIC_KEY\x10\x0b\x12/\n+CHALLENGE_REPLY_ERROR_SIGNED_BLOBS_MISMATCH\x10\x0c\x12;\n7CHALLENGE_REPLY_ERROR_TLS_CERT_VALIDITY_PERIOD_TOO_LONG\x10\r\x12=\n9CHALLENGE_REPLY_ERROR_TLS_CERT_VALID_START_DATE_IN_FUTURE\x10\x0e\x12*\n&CHALLENGE_REPLY_ERROR_TLS_CERT_EXPIRED\x10\x0f\x12%\n!CHALLENGE_REPLY_ERROR_CRL_INVALID\x10\x10\x12&\n"CHALLENGE_REPLY_ERROR_CERT_REVOKED\x10\x11\x42\x02H\x03'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "logging_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals["DESCRIPTOR"]._serialized_options = b"H\003"
    _globals["_EVENTTYPE"]._serialized_start = 1120
    _globals["_EVENTTYPE"]._serialized_end = 1952
    _globals["_CHANNELAUTH"]._serialized_start = 1954
    _globals["_CHANNELAUTH"]._serialized_end = 1994
    _globals["_READYSTATE"]._serialized_start = 1997
    _globals["_READYSTATE"]._serialized_end = 2130
    _globals["_CONNECTIONSTATE"]._serialized_start = 2133
    _globals["_CONNECTIONSTATE"]._serialized_end = 2532
    _globals["_READSTATE"]._serialized_start = 2535
    _globals["_READSTATE"]._serialized_end = 2700
    _globals["_WRITESTATE"]._serialized_start = 2703
    _globals["_WRITESTATE"]._serialized_end = 2899
    _globals["_ERRORSTATE"]._serialized_start = 2902
    _globals["_ERRORSTATE"]._serialized_end = 3249
    _globals["_CHALLENGEREPLYERRORTYPE"]._serialized_start = 3252
    _globals["_CHALLENGEREPLYERRORTYPE"]._serialized_end = 4068
    _globals["_SOCKETEVENT"]._serialized_start = 53
    _globals["_SOCKETEVENT"]._serialized_end = 690
    _globals["_AGGREGATEDSOCKETEVENT"]._serialized_start = 693
    _globals["_AGGREGATEDSOCKETEVENT"]._serialized_end = 937
    _globals["_LOG"]._serialized_start = 940
    _globals["_LOG"]._serialized_end = 1117
# @@protoc_insertion_point(module_scope)
