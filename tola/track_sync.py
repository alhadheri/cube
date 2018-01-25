import requests
import logging
import json
from urlparse import urljoin

from django.conf import settings

logger = logging.getLogger(__name__)


# UTIL FUNCTIONS FOR SYNCHRONIZATION
# Request wrapper for Track
def track_request(method, url_subpath, data=None):
    headers = {
        'Authorization': 'Token {}'.format(settings.TOLA_TRACK_TOKEN),
    }
    url = urljoin(settings.TOLA_TRACK_URL, url_subpath)
    response = None
    if method == 'post':
        response = requests.post(url, data=data, headers=headers)
    elif method == 'put':
        response = requests.put(url, data=data, headers=headers)
    elif method == 'get':
        response = requests.get(url, params=data, headers=headers)
    elif method == 'delete':
        response = requests.delete(url)
    return response


# Log info depending of the response status code
def validate_response(response, obj):
    if response.status_code in [200, 201]:
        logger.info('The request for {} (id={}, model={}) was successfully '
                    'executed on Track.'.format(obj.name, obj.id,
                                                obj.__class__.__name__))
    elif response.status_code in [400, 403, 500]:
        logger.warning("{} (id={}, model={}) could not be created/fetched "
                       "successfully on/from Track.".format(
                        obj.name, obj.id, obj.__class__.__name__))


def _build_org_form(obj):
    return {
        'organization_uuid': obj.organization_uuid,
        'name': obj.name,
        'description': obj.description,
        'organization_url': obj.organization_url,
        'level_1_label': obj.level_1_label,
        'level_2_label': obj.level_2_label,
        'level_3_label': obj.level_3_label,
        'level_4_label': obj.level_4_label,
        'create_date': obj.create_date,
        'edit_date': obj.edit_date
    }


# FUNCTIONS TO SYNC MODELS
# Sync Tola Users
def register_user(data, tolauser):
    url_subpath = 'accounts/register/'
    response = track_request('post', url_subpath, data)
    validate_response(response, tolauser)
    return response


# Sync Programs/WorkflowLevel1
def create_workflowlevel1(obj):
    url_subpath = 'api/organization?name={}'.format(obj.organization.name)
    response = track_request('get', url_subpath)
    if response.status_code in [400, 403, 500]:
        logger.warn('The Organization {} (id={}) could not be '
                    'successfully fetched from Track.'.format(
                     obj.organization.name, obj.organization.id))
        return response

    content = json.loads(response.content)
    if response.status_code == 200 and len(content) == 0:
        logger.info('The organization {} (id={}) was not found on Track'.format(
            obj.organization.name, obj.organization.id))
        return response

    org = content[0]
    data = {
        'level1_uuid': obj.level1_uuid,
        'name': obj.name,
        'country': None,
        'organization': org['id']
    }

    response = track_request('post', 'api/workflowlevel1', data)
    if response.status_code == 201:
        logger.info('The Program {} (id={}) was created successfully on '
                    'Track.'.format(obj.name, obj.id))
    return response


# Sync Organizations
def create_organization(obj):
    data = _build_org_form(obj)
    response = track_request('post', 'api/organization', data)
    validate_response(response, obj)
    return response


def update_organization(obj):
    data = _build_org_form(obj)
    response = track_request('put', 'api/organization', data)
    validate_response(response, obj)
    return response


def delete_organization(obj):
    response = track_request('delete', 'api/organization/{}'.format(obj.id))
    validate_response(response, obj)
    return response
