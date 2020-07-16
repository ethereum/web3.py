import logging
import os

QuikNode_URL_format = 'https://%s.quiknode.pro/%s/'

def check_endpoint_URL():
  key = os.environ.get('QuikNode_Node_URL','')
  if key == '':
    logging.getLogger('web3.auto.QuikNode').error(
      "Your node's URL is wrong or invalid. Add environment variable QuikNode_Node_URL"
      "with your endpoint URL. Get a free QuikNode endpoint at https://quiknode.io/"
    )
  return key
  
  
  def build_QuikNode_url(network):
    key = check_endpoint_URL()
    url = QuikNode_URL_format % (network, key)
    return url
