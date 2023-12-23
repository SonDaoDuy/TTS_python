# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the gRPC route guide client."""

from __future__ import print_function

import logging
import pyttsx3
import os
import soundfile as sf
from scipy.io.wavfile import write
import numpy as np
from ast import literal_eval

import grpc
import first_service_pb2
import first_service_pb2_grpc


def make_text_message(text):
    return first_service_pb2.TextMessage(
        text=text
        )


def convert_tts(stub, save_file='output.wav', text=None):
    responses = stub.ConvertTTS(make_text_message(text))
    data = np.frombuffer(responses.data)
    # data_shape = tuple(responses.data_shape)
    data_shape = literal_eval(responses.data_shape)
    data = data.reshape(data_shape)
    fs = responses.frame_rate
    print(
        "Received message %s" % (fs)
    )
    # for response in responses:
    write(save_file, fs, data)
    print(
        "Received message at frame rate %s" % (fs)
    )


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = first_service_pb2_grpc.TTSPythonStub(channel)
        print("-------------- Convert TTS--------------")
        text = "This is the first sentence that is converted to speech."
        convert_tts(stub, text=text)


if __name__ == "__main__":
    logging.basicConfig()
    run()
