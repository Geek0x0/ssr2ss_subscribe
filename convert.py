# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
import requests,base64,json,urllib,urlparse

app = Flask(__name__)

ssr_subscribe = {
    "CordCloud": "https://www.cordcloud.me/link/%s?mu=0",
    "SSRCloud": "https://mikucloud.ml/link/%s?mu=0"
}

def decode_base64(data, decode_utf8=True):
    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += '='* missing_padding
    if decode_utf8:
        return base64.urlsafe_b64decode(data.encode('ascii')).decode("utf-8")
    else:
        return base64.urlsafe_b64decode(data.encode('ascii'))

def encode_base64(data):
    return base64.urlsafe_b64encode(data.encode("utf-8")).decode("utf-8")

def get_remarks(ssrConfig):
    param = urlparse.parse_qs(urlparse.urlsplit(ssrConfig).query)
    remarks_base64 =  param['remarks'][0].replace('-', '+').replace('_', '/')
    remarks = decode_base64(remarks_base64, False)
    return urllib.quote(remarks)

def convert_ssr2ss(ssrConfig):
    ssConfig = "ss://"
    networkConfig = ssrConfig.split('/?')[0].split(':')
    serverIP = networkConfig[0]
    serverPort = networkConfig[1]
    encryption = networkConfig[3]
    passwd = decode_base64(networkConfig[5])
    remarks = get_remarks(ssrConfig)
    ssConfig += encode_base64(encryption + ":" + passwd) + "@" + serverIP + ":" + serverPort + "/#" + remarks
    return ssConfig

def handle_ssr2ss(ssr_subscribe_url):
    ssConfigs = []
    setheaders = { "User-Agent": "ShadowsocksX-NG-R 1.4.3 Version R8(3)" }
    response = requests.get(ssr_subscribe_url, timeout = 3, headers = setheaders)
    if response.ok:
        resault_base64_str = decode_base64(response.text)
        resault_list = resault_base64_str.split('\n')
        for ssrConfig in resault_list:
            if len(ssrConfig) > 0:
                sconfig = decode_base64(ssrConfig.split('://')[1])
                ssConfigs.append(convert_ssr2ss(sconfig))
        dist = '\n'.join(ssConfigs)
        return encode_base64(dist)
    else:
        return ""


@app.route('/')
def index():
    response = app.response_class(
        response = "",
        status = 500,
    )
    return response

@app.route('/<type>/<link>', methods=['GET'])
def create_ss_subscription(type, link):
    url = ""
    if type == "CordCloud":
        url = ssr_subscribe['CordCloud'] % link
    elif type == "SSRCloud":
        url = ssr_subscribe['SSRCloud'] % link
    return handle_ssr2ss(url)
    
if __name__ == "__main__":
    # test environment
    app.run(host="0.0.0.0", port=9999)