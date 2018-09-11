sudo docker run --rm -v "$PWD:/tmp" openwhisk/python3action bash "cd tmp && virtualenv virtualenv && source virtualenv/bin/activate && pip install -r requirements.txt"
echo "INFO: DOCKER COMPLETE"
cd image-resizer
zip -r ../imageResizer.zip ./virtualenv ./__main__.py ./imageresizer.py
cd ..
echo "INFO: ZIPPING COMPLETE"
wsk -i action update imageResizer --kind python:3 imageResizer.zip --web true
echo "INFO: FUNCTION DEPLOYED"
