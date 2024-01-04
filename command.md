# convert proto file command:

```
python -m grpc_tools.protoc -I./protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/first_service.proto
```

# run client & server command:
for client:
```
python tts_python_client.py -o voice_output_client -t <text input to convert to speech>
```


# git command