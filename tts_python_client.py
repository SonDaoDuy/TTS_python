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
from email.policy import default

import logging
import pyttsx3
import os
import soundfile as sf
from scipy.io.wavfile import write
import numpy as np
from ast import literal_eval
import argparse
import sys

import grpc
import first_service_pb2
import first_service_pb2_grpc




def make_text_message(text):
    return first_service_pb2.TextMessage(
        text=text
        )


def convert_tts(stub, args):
    text = args.text
    responses = stub.ConvertTTS(make_text_message(text))
    
    print(
        "Received message of type %s" % (type(responses))
    )

    a = sys.getsizeof(responses.data)
    print(
        "Received message of size %s" % (a)
    )
    hash_len = 10 if len(text) > 10 else len(text)
    save_file = os.path.join(args.output, str(hash(text[:hash_len])) + '.wav')
    with open(save_file, "wb") as binary_file:
        binary_file.write(responses.data)
        


def run(args):
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    if not os.path.isdir(args.output):
        os.mkdir(args.output)
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = first_service_pb2_grpc.TTSPythonStub(channel)
        print("-------------- Convert TTS--------------")
        convert_tts(stub, args)

def parse_augment():
    parser = argparse.ArgumentParser(description='Example client request parameters')
    parser.add_argument('-t','--text', help='Text input to convert to speech', required=True, type=str)
    parser.add_argument('-o','--output', help='Output folder', default='./')
    return parser.parse_args()

if __name__ == "__main__":
    logging.basicConfig()
    args = parse_augment()
    run(args)
