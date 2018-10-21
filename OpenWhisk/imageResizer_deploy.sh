#sudo docker run --rm -v "$PWD:/tmp" openwhisk/python3action bash "cd tmp && virtualenv virtualenv && source virtualenv/bin/activate && pip install -r requirements.txt"
#echo "INFO: DOCKER COMPLETE"
cd image-resizer
zip -r ../imageResizer.zip ./virtualenv/bin/activate_this.py virtualenv/lib/python3.6/site-packages/PIL virtualenv/lib/python3.6/site-packages/ ./__main__.py ./imageresizer.py ./requirements.txt
cd ..
echo "INFO: ZIPPING COMPLETE"
wsk -i action update imageResizer imageResizer.zip --docker ibmfunctions/action-python-v3 --web true
echo "INFO: FUNCTION DEPLOYED"
