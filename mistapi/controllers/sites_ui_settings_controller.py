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
from mistapi.models.curd_ui_settings import CurdUiSettings
from mistapi.exceptions.api_exception import APIException
from mistapi.exceptions.api_v_1_sites_uisettings_401_error_exception import ApiV1SitesUisettings401ErrorException
from mistapi.exceptions.api_v_1_sites_uisettings_403_error_exception import ApiV1SitesUisettings403ErrorException
from mistapi.exceptions.api_v_1_sites_uisettings_404_error_exception import ApiV1SitesUisettings404ErrorException
from mistapi.exceptions.api_v_1_sites_uisettings_derived_401_error_exception import ApiV1SitesUisettingsDerived401ErrorException
from mistapi.exceptions.api_v_1_sites_uisettings_derived_403_error_exception import ApiV1SitesUisettingsDerived403ErrorException
from mistapi.exceptions.api_v_1_sites_uisettings_derived_404_error_exception import ApiV1SitesUisettingsDerived404ErrorException


class SitesUISettingsController(BaseController):

    """A Controller to access Endpoints in the mistapi API."""
    def __init__(self, config):
        super(SitesUISettingsController, self).__init__(config)

    def get_site_curd_settings(self,
                               site_id):
        """Does a GET request to /api/v1/sites/{site_id}/uisettings.

        CURD site UI settings

        Args:
            site_id (uuid|string): TODO: type description here.

        Returns:
            list of CurdUiSettings: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/uisettings')
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
            .deserialize_into(CurdUiSettings.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesUisettings401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesUisettings403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesUisettings404ErrorException)
        ).execute()

    def create_site_curd_settings(self,
                                  site_id,
                                  body=None):
        """Does a POST request to /api/v1/sites/{site_id}/uisettings.

        CURD site UI settings

        Args:
            site_id (uuid|string): TODO: type description here.
            body (CurdUiSettings, optional): Request Body

        Returns:
            CurdUiSettings: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/uisettings')
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
            .deserialize_into(CurdUiSettings.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesUisettings401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesUisettings403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesUisettings404ErrorException)
        ).execute()

    def get_site_derived_curd_setting(self,
                                      site_id):
        """Does a GET request to /api/v1/sites/{site_id}/uisettings/derived.

        Get both site UI settings(for_site=true) and org UI settings
        (for_site=false)

        Args:
            site_id (uuid|string): TODO: type description here.

        Returns:
            CurdUiSettings: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/uisettings/derived')
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
            .deserialize_into(CurdUiSettings.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesUisettingsDerived401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesUisettingsDerived403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesUisettingsDerived404ErrorException)
        ).execute()

    def delete_site_curd_setting(self,
                                 site_id,
                                 uisetting_id):
        """Does a DELETE request to /api/v1/sites/{site_id}/uisettings/{uisetting_id}.

        CURD site UI settings

        Args:
            site_id (uuid|string): TODO: type description here.
            uisetting_id (uuid|string): TODO: type description here.

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
            .path('/api/v1/sites/{site_id}/uisettings/{uisetting_id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('uisetting_id')
                            .value(uisetting_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesUisettings401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesUisettings403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesUisettings404ErrorException)
        ).execute()

    def get_site_curd_setting(self,
                              site_id,
                              uisetting_id):
        """Does a GET request to /api/v1/sites/{site_id}/uisettings/{uisetting_id}.

        CURD site UI settings

        Args:
            site_id (uuid|string): TODO: type description here.
            uisetting_id (uuid|string): TODO: type description here.

        Returns:
            CurdUiSettings: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/uisettings/{uisetting_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('uisetting_id')
                            .value(uisetting_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CurdUiSettings.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesUisettings401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesUisettings403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesUisettings404ErrorException)
        ).execute()

    def update_site_curd_setting(self,
                                 site_id,
                                 uisetting_id,
                                 body=None):
        """Does a POST request to /api/v1/sites/{site_id}/uisettings/{uisetting_id}.

        CURD site UI settings

        Args:
            site_id (uuid|string): TODO: type description here.
            uisetting_id (uuid|string): TODO: type description here.
            body (CurdUiSettings, optional): Request Body

        Returns:
            CurdUiSettings: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/uisettings/{uisetting_id}')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('uisetting_id')
                            .value(uisetting_id)
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
            .deserialize_into(CurdUiSettings.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesUisettings401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesUisettings403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesUisettings404ErrorException)
        ).execute()
