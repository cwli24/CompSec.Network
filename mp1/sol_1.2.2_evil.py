#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """            �1��<� ��Y[���wrV�RAP2;~�7�N��ޏ�!�,LD�!edgu|Դ�\�߾�1ȣ���y���@������ "����]q}27O��.s�0_k���5j��B8��0l���Τ"""
from hashlib import sha256
if sha256(blob).hexdigest() == "54dc9b77a727534ffca599d31424a347d16fc35c46585c076feb519f8a08cc62":
	print "I come in peace."
else:
	print "Prepare to be destroyed."