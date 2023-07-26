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
from mistapi.models.deviceprofile import Deviceprofile
from mistapi.models.service_policy import ServicePolicy
from mistapi.exceptions.api_exception import APIException
from mistapi.exceptions.api_v_1_sites_deviceprofiles_derived_401_error_exception import ApiV1SitesDeviceprofilesDerived401ErrorException
from mistapi.exceptions.api_v_1_sites_deviceprofiles_derived_403_error_exception import ApiV1SitesDeviceprofilesDerived403ErrorException
from mistapi.exceptions.api_v_1_sites_deviceprofiles_derived_404_error_exception import ApiV1SitesDeviceprofilesDerived404ErrorException
from mistapi.exceptions.api_v_1_sites_servicepolicies_derived_401_error_exception import ApiV1SitesServicepoliciesDerived401ErrorException
from mistapi.exceptions.api_v_1_sites_servicepolicies_derived_403_error_exception import ApiV1SitesServicepoliciesDerived403ErrorException
from mistapi.exceptions.api_v_1_sites_servicepolicies_derived_404_error_exception import ApiV1SitesServicepoliciesDerived404ErrorException


class SitesServicePoliciesController(BaseController):

    """A Controller to access Endpoints in the mistapi API."""
    def __init__(self, config):
        super(SitesServicePoliciesController, self).__init__(config)

    def list_site_device_profiles_derived(self,
                                          site_id,
                                          resolve=False):
        """Does a GET request to /api/v1/sites/{site_id}/deviceprofiles/derived.

        Retrieves the list of Device Profiles available for the Site

        Args:
            site_id (uuid|string): TODO: type description here.
            resolve (bool, optional): whether resolve the site variables

        Returns:
            list of Deviceprofile: Response from the API. Example response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/deviceprofiles/derived')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('resolve')
                         .value(resolve))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Deviceprofile.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesDeviceprofilesDerived401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesDeviceprofilesDerived403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesDeviceprofilesDerived404ErrorException)
        ).execute()

    def list_site_service_policies_derived(self,
                                           site_id,
                                           resolve=False):
        """Does a GET request to /api/v1/sites/{site_id}/servicepolicies/derived.

        Retrieves the list of Service Policies available for the Site

        Args:
            site_id (uuid|string): TODO: type description here.
            resolve (bool, optional): whether resolve the site variables

        Returns:
            list of ServicePolicy: Response from the API. Example response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/servicepolicies/derived')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('resolve')
                         .value(resolve))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServicePolicy.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesServicepoliciesDerived401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesServicepoliciesDerived403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesServicepoliciesDerived404ErrorException)
        ).execute()