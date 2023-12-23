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
"""The Python implementation of the gRPC route guide server."""

from concurrent import futures
# import logging
# import math
# import time
import logging
import pyttsx3
import os
import soundfile as sf
import numpy as np

import grpc
import first_service_pb2
import first_service_pb2_grpc
# import first_service_resources


class TTSPythonServicer(first_service_pb2_grpc.TTSPythonServicer):
    """Provides methods that implement functionality of route guide server."""

    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 170)
        self.voice_output = './voice_output'
        if not os.path.isdir(self.voice_output):
            os.mkdir(self.voice_output)

    def get_speech(self, text):
        hash_len = 10 if len(text) > 10 else len(text)
        file_name = os.path.join(self.voice_output, str(hash(text[:hash_len])) + '.wav')
        self.engine.save_to_file(text, file_name)
        self.engine.runAndWait()
        if self.engine._inLoop:
            self.engine.endLoop()
        return file_name

    def ConvertTTS(self, request, context):
        speech_file = self.get_speech(request.text)
        data, fs = sf.read(speech_file, dtype='float32')
        data_shape = data.shape
        # print("sending %s to client" % (fs))
        speech_response = first_service_pb2.SpeechResponse(
            data=data.tobytes(),
            data_shape=str(data_shape),
            frame_rate=fs
            )
        return speech_response


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    first_service_pb2_grpc.add_TTSPythonServicer_to_server(
        TTSPythonServicer(), server
    )
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
