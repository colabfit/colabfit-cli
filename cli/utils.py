from pprint import pprint
import json
import requests
def _query(text=None, elements=None, elements_exact=None, properties=None):
    query = {}
    if text is not None:
        query['$text']={'$search':text}
    if elements is not None:
        if elements_exact is not None:
            raise Exception('Only one of elements or elements-exact should be specified')
        else:
            query['aggregated_info.elements']={'$all':elements.upper().split(' ')}
    if elements_exact is not None:
            ee = elements_exact.upper().split(' ')
            query['aggregated_info.elements']={"$size":len(ee), '$all': ee}
    if properties is not None:
            query['aggregated_info.property_types']={'$all':properties.split(' ')}



    #post to REST API
    q = requests.post('https://cf.hsrn.nyu.edu/datasets',json=query) 
    return q.json()
    
def format_print(doc):
    new_doc={}
    new_doc['colabfit-id']=doc['colabfit-id']
    new_doc['name']=doc['name']
    new_doc['authors']=doc['authors']
    new_doc['description']=doc['description']
    new_doc['links']=doc['links']
    new_doc['links'].append('https://materials.colabfit.org/id/%s'%doc['colabfit-id'])
    #new_doc['aggregated_info']=doc['aggregated_info']
    pprint (new_doc,sort_dicts=False)
