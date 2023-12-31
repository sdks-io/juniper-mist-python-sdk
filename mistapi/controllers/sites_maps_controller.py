# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from mistapi.api_helper import APIHelper
from mistapi.configuration import Server
from mistapi.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from mistapi.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from apimatic_core.authentication.multiple.and_auth_group import And
from apimatic_core.authentication.multiple.or_auth_group import Or
from mistapi.models.map import Map
from mistapi.models.api_v_1_sites_maps_import_response import ApiV1SitesMapsImportResponse
from mistapi.models.api_v_1_sites_maps_set_map_response import ApiV1SitesMapsSetMapResponse
from mistapi.exceptions.api_exception import APIException
from mistapi.exceptions.api_v_1_sites_maps_401_error_exception import ApiV1SitesMaps401ErrorException
from mistapi.exceptions.api_v_1_sites_maps_403_error_exception import ApiV1SitesMaps403ErrorException
from mistapi.exceptions.api_v_1_sites_maps_404_error_exception import ApiV1SitesMaps404ErrorException
from mistapi.exceptions.api_v_1_sites_maps_import_401_error_exception import ApiV1SitesMapsImport401ErrorException
from mistapi.exceptions.api_v_1_sites_maps_import_403_error_exception import ApiV1SitesMapsImport403ErrorException
from mistapi.exceptions.api_v_1_sites_maps_import_404_error_exception import ApiV1SitesMapsImport404ErrorException
from mistapi.exceptions.api_v_1_sites_maps_image_401_error_exception import ApiV1SitesMapsImage401ErrorException
from mistapi.exceptions.api_v_1_sites_maps_image_403_error_exception import ApiV1SitesMapsImage403ErrorException
from mistapi.exceptions.api_v_1_sites_maps_image_404_error_exception import ApiV1SitesMapsImage404ErrorException
from mistapi.exceptions.api_v_1_sites_maps_replace_401_error_exception import ApiV1SitesMapsReplace401ErrorException
from mistapi.exceptions.api_v_1_sites_maps_replace_403_error_exception import ApiV1SitesMapsReplace403ErrorException
from mistapi.exceptions.api_v_1_sites_maps_replace_404_error_exception import ApiV1SitesMapsReplace404ErrorException
from mistapi.exceptions.api_v_1_sites_maps_set_map_401_error_exception import ApiV1SitesMapsSetMap401ErrorException
from mistapi.exceptions.api_v_1_sites_maps_set_map_403_error_exception import ApiV1SitesMapsSetMap403ErrorException
from mistapi.exceptions.api_v_1_sites_maps_set_map_404_error_exception import ApiV1SitesMapsSetMap404ErrorException
from mistapi.exceptions.api_v_1_sites_maps_wayfinding_import_401_error_exception import ApiV1SitesMapsWayfindingImport401ErrorException
from mistapi.exceptions.api_v_1_sites_maps_wayfinding_import_403_error_exception import ApiV1SitesMapsWayfindingImport403ErrorException
from mistapi.exceptions.api_v_1_sites_maps_wayfinding_import_404_error_exception import ApiV1SitesMapsWayfindingImport404ErrorException


class SitesMapsController(BaseController):

    """A Controller to access Endpoints in the mistapi API."""
    def __init__(self, config):
        super(SitesMapsController, self).__init__(config)

    def list_site_maps(self,
                       site_id):
        """Does a GET request to /api/v1/sites/{site_id}/maps.

        Get List of Site Maps

        Args:
            site_id (uuid|string): TODO: type description here.

        Returns:
            list of Map: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/maps')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Map.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesMaps401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesMaps403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesMaps404ErrorException)
        ).execute()

    def create_site_map(self,
                        site_id,
                        body=None):
        """Does a POST request to /api/v1/sites/{site_id}/maps.

        Create Site Map

        Args:
            site_id (uuid|string): TODO: type description here.
            body (Map, optional): Request Body

        Returns:
            Map: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/maps')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Map.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesMaps401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesMaps403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesMaps404ErrorException)
        ).execute()

    def import_site_maps(self,
                         site_id,
                         auto_deviceprofile_assignment=None,
                         csv=None,
                         file=None,
                         json=None):
        """Does a POST request to /api/v1/sites/{site_id}/maps/import.

        Import data from files is a multipart POST which has an file, an
        optional json, and an optional csv, to create floorplan, assign
        matching inventory to specific site, place ap if name or mac matches.
        # Note
        This endpoint (at the site level), the AP must be already assigned to
        the site to be placed on the floorplan. If you want to place APs from
        the Org inventory, it is required to use the endpoint at the Org level
        [importOrgMaps](#operation/importOrgMaps)
        # CSV File Format
        ```csv
        Vendor AP name,Mist AP Mac
        US Office AP-2,5c:5b:35:00:00:02
        US Office AP-3,5c5b35000002
        ``` 

        Args:
            site_id (uuid|string): TODO: type description here.
            auto_deviceprofile_assignment (bool, optional): whether to auto
                assign device to deviceprofile by name
            csv (string, optional): csv file for ap name mapping, optional
            file (string, optional): ekahau or ibwave file
            json (Json, optional): TODO: type description here.

        Returns:
            ApiV1SitesMapsImportResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/maps/import')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .form_param(Parameter()
                        .key('auto_deviceprofile_assignment')
                        .value(auto_deviceprofile_assignment))
            .form_param(Parameter()
                        .key('csv')
                        .value(csv))
            .form_param(Parameter()
                        .key('file')
                        .value(file))
            .form_param(Parameter()
                        .key('json')
                        .value(json))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ApiV1SitesMapsImportResponse.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesMapsImport401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesMapsImport403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesMapsImport404ErrorException)
        ).execute()

    def delete_site_map(self,
                        site_id,
                        map_id):
        """Does a DELETE request to /api/v1/sites/{site_id}/maps/{map_id}.

        Delete Site Map

        Args:
            site_id (uuid|string): TODO: type description here.
            map_id (uuid|string): TODO: type description here.

        Returns:
            object: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/maps/{map_id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('map_id')
                            .value(map_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesMaps401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesMaps403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesMaps404ErrorException)
        ).execute()

    def get_site_map(self,
                     site_id,
                     map_id):
        """Does a GET request to /api/v1/sites/{site_id}/maps/{map_id}.

        Get Site Map Details

        Args:
            site_id (uuid|string): TODO: type description here.
            map_id (uuid|string): TODO: type description here.

        Returns:
            Map: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/maps/{map_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('map_id')
                            .value(map_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Map.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesMaps401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesMaps403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesMaps404ErrorException)
        ).execute()

    def update_site_map(self,
                        site_id,
                        map_id,
                        body=None):
        """Does a PUT request to /api/v1/sites/{site_id}/maps/{map_id}.

        Update Site Map

        Args:
            site_id (uuid|string): TODO: type description here.
            map_id (uuid|string): TODO: type description here.
            body (Map, optional): Request Body

        Returns:
            Map: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/maps/{map_id}')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('map_id')
                            .value(map_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Map.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesMaps401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesMaps403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesMaps404ErrorException)
        ).execute()

    def delete_site_map_image(self,
                              site_id,
                              map_id):
        """Does a DELETE request to /api/v1/sites/{site_id}/maps/{map_id}/image.

        Delete Site Map Image

        Args:
            site_id (uuid|string): TODO: type description here.
            map_id (uuid|string): TODO: type description here.

        Returns:
            object: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/maps/{map_id}/image')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('map_id')
                            .value(map_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesMapsImage401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesMapsImage403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesMapsImage404ErrorException)
        ).execute()

    def add_site_map_image(self,
                           site_id,
                           map_id,
                           file=None,
                           json=None):
        """Does a POST request to /api/v1/sites/{site_id}/maps/{map_id}/image.

        Add image map is a multipart POST which has an file (Image) and an
        optional json parameter

        Args:
            site_id (uuid|string): TODO: type description here.
            map_id (uuid|string): TODO: type description here.
            file (string, optional): binary file
            json (string, optional): JSON string describing your upload

        Returns:
            object: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/maps/{map_id}/image')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('map_id')
                            .value(map_id)
                            .should_encode(True))
            .form_param(Parameter()
                        .key('file')
                        .value(file))
            .form_param(Parameter()
                        .key('json')
                        .value(json))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesMapsImage401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesMapsImage403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesMapsImage404ErrorException)
        ).execute()

    def replace_site_map_image(self,
                               site_id,
                               map_id,
                               file,
                               json=None):
        """Does a POST request to /api/v1/sites/{site_id}/maps/{map_id}/replace.

        Replace Map Image
        This works like an PUT where the image will be replaced. If transform
        is provided, all the locations of the objects on the map (AP, Zone,
        Vbeacon, Beacon) will be transformed as well (relative to the new
        Map)

        Args:
            site_id (uuid|string): TODO: type description here.
            map_id (uuid|string): TODO: type description here.
            file (string): TODO: type description here.
            json (Json2, optional): TODO: type description here.

        Returns:
            object: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/maps/{map_id}/replace')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('map_id')
                            .value(map_id)
                            .should_encode(True))
            .form_param(Parameter()
                        .key('file')
                        .value(file))
            .form_param(Parameter()
                        .key('json')
                        .value(json))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesMapsReplace401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesMapsReplace403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesMapsReplace404ErrorException)
        ).execute()

    def bulk_assign_site_aps_to_map(self,
                                    site_id,
                                    map_id,
                                    body=None):
        """Does a POST request to /api/v1/sites/{site_id}/maps/{map_id}/set_map.

        This API can be used to assign a list of AP Macs associated with
        site_id to the specified map_id. Note that map_id must be associated
        with corresponding site_id. This API obeys the following rules 
        1. if AP is unassigned to any Map, it gets associated with map_id 
        2. Any moved APs are returned in the response 
        3. If the AP is considered a locked AP, no action will be taken

        Args:
            site_id (uuid|string): TODO: type description here.
            map_id (uuid|string): TODO: type description here.
            body (ApiV1SitesMapsSetMapRequest, optional): TODO: type
                description here.

        Returns:
            ApiV1SitesMapsSetMapResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/maps/{map_id}/set_map')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('map_id')
                            .value(map_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ApiV1SitesMapsSetMapResponse.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesMapsSetMap401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesMapsSetMap403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesMapsSetMap404ErrorException)
        ).execute()

    def import_site_wayfindings(self,
                                site_id,
                                map_id,
                                body=None):
        """Does a POST request to /api/v1/sites/{site_id}/maps/{map_id}/wayfinding/import.

        This imports the vendor map meta data into the Map JSON. This is
        required by the SDK and App in order to access/render the vendor Map
        properly.

        Args:
            site_id (uuid|string): TODO: type description here.
            map_id (uuid|string): TODO: type description here.
            body (object, optional): Request Body

        Returns:
            object: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/maps/{map_id}/wayfinding/import')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('map_id')
                            .value(map_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesMapsWayfindingImport401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesMapsWayfindingImport403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesMapsWayfindingImport404ErrorException)
        ).execute()
