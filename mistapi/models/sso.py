# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Sso(object):

    """Implementation of the 'sso' model.

    SSO

    Attributes:
        created_time (float): TODO: type description here.
        custom_logout_url (string): optional, a URL we will redirect the user
            after user logout from Mist (for some IdP which supports a custom
            logout URL that is different from SP-initiated SLO process)
        default_role (string): default role to assign if there’s no match. By
            default, an assertion is treated as invalid when there’s no role
            matched
        domain (string): TODO: type description here.
        id (uuid|string): TODO: type description here.
        idp_cert (string): if `idp_type`==`saml`. IDP Cert (used to verify the
            signed response)
        idp_sign_algo (string): if `idp_type`==`saml`. Signing algorithm for
            SAML Assertion
        idp_sso_url (string): IDP Single-Sign-On URL
        idp_type (IdpTypeEnum): TODO: type description here.
        ignore_unmatched_roles (bool): ignore any unmatched roles provided in
            assertion. By default, an assertion is treated as invalid for any
            unmatched role
        issuer (string): if `idp_type`==`saml`. IDP issuer URL
        ldap_base_dn (string): if `idp_type`==`ldap`
        ldap_bind_dn (string): if `idp_type`==`ldap`
        ldap_bind_password (string): if `idp_type`==`ldap`
        ldap_certs (list of string): if `idp_type`==`ldap`
        ldap_client_cert (string): if `idp_type`==`ldap`
        ldap_client_key (string): if `idp_type`==`ldap`
        ldap_group_attr (string): Only if `ldap_type`==`custom`
        ldap_group_dn (string): Only if `ldap_type`==`custom`
        ldap_group_filter (string): Only if `ldap_type`==`custom`
        ldap_server_hosts (list of string): if `idp_type`==`ldap`
        ldap_type (LdapTypeEnum): if `idp_type`==`ldap`
        ldap_user_filter (string): Only if `ldap_type`==`custom`
        modified_time (float): TODO: type description here.
        msp_id (uuid|string): TODO: type description here.
        name (string): name
        nameid_format (NameidFormatEnum): if `idp_type`==`saml`
        oauth_cc_client_id (string): if `oauth_type`==`okta`, Client
            Credentials
        oauth_cc_client_secret (string): if `oauth_type`==`okta`,
            oauth_cc_client_secret is RSA private key, of the form "-----BEGIN
            RSA PRIVATE KEY--...."
        oauth_discovery_url (string): if `idp_type`==`oauth`
        oauth_ropc_client_id (string): ropc = Resource Owner Password
            Credentials
        oauth_ropc_secret (string): oauth_ropc_client_secret can be empty if
            oauth_type is azure
        oauth_tenant_id (string): if `oauth_type`==`okta`, oauth_tenant_id
        oauth_type (OauthTypeEnum): TODO: type description here.
        org_id (uuid|string): TODO: type description here.
        role_attr_extraction (string): optional, custom role attribute parsing
            scheme  Supported Role Parsing Schemes
            <table><tr><th>Name</th><th>Scheme</th></tr><tr><td>cn</td><td><ul>
            <li>The expected role attribute format in SAML Assertion is
            “CN=cn,OU=ou1,OU=ou2,…”</li><li>CN (the key) is case insensitive
            and exactly 1 CN is expected (or the entire entry will be
            ignored)</li><li>E.g. if role attribute is “CN=cn,OU=ou1,OU=ou2”
            then parsed role value is “cn”</li></ul></td></tr></table>
        role_attr_from (string): name of the attribute in SAML Assertion to
            extract role from
        site_id (uuid|string): TODO: type description here.
        mtype (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "created_time": 'created_time',
        "custom_logout_url": 'custom_logout_url',
        "default_role": 'default_role',
        "domain": 'domain',
        "id": 'id',
        "idp_cert": 'idp_cert',
        "idp_sign_algo": 'idp_sign_algo',
        "idp_sso_url": 'idp_sso_url',
        "idp_type": 'idp_type',
        "ignore_unmatched_roles": 'ignore_unmatched_roles',
        "issuer": 'issuer',
        "ldap_base_dn": 'ldap_base_dn',
        "ldap_bind_dn": 'ldap_bind_dn',
        "ldap_bind_password": 'ldap_bind_password',
        "ldap_certs": 'ldap_certs',
        "ldap_client_cert": 'ldap_client_cert',
        "ldap_client_key": 'ldap_client_key',
        "ldap_group_attr": 'ldap_group_attr',
        "ldap_group_dn": 'ldap_group_dn',
        "ldap_group_filter": 'ldap_group_filter',
        "ldap_server_hosts": 'ldap_server_hosts',
        "ldap_type": 'ldap_type',
        "ldap_user_filter": 'ldap_user_filter',
        "modified_time": 'modified_time',
        "msp_id": 'msp_id',
        "nameid_format": 'nameid_format',
        "oauth_cc_client_id": 'oauth_cc_client_id',
        "oauth_cc_client_secret": 'oauth_cc_client_secret',
        "oauth_discovery_url": 'oauth_discovery_url',
        "oauth_ropc_client_id": 'oauth_ropc_client_id',
        "oauth_ropc_secret": 'oauth_ropc_secret',
        "oauth_tenant_id": 'oauth_tenant_id',
        "oauth_type": 'oauth_type',
        "org_id": 'org_id',
        "role_attr_extraction": 'role_attr_extraction',
        "role_attr_from": 'role_attr_from',
        "site_id": 'site_id',
        "mtype": 'type'
    }

    _optionals = [
        'created_time',
        'custom_logout_url',
        'default_role',
        'domain',
        'id',
        'idp_cert',
        'idp_sign_algo',
        'idp_sso_url',
        'idp_type',
        'ignore_unmatched_roles',
        'issuer',
        'ldap_base_dn',
        'ldap_bind_dn',
        'ldap_bind_password',
        'ldap_certs',
        'ldap_client_cert',
        'ldap_client_key',
        'ldap_group_attr',
        'ldap_group_dn',
        'ldap_group_filter',
        'ldap_server_hosts',
        'ldap_type',
        'ldap_user_filter',
        'modified_time',
        'msp_id',
        'nameid_format',
        'oauth_cc_client_id',
        'oauth_cc_client_secret',
        'oauth_discovery_url',
        'oauth_ropc_client_id',
        'oauth_ropc_secret',
        'oauth_tenant_id',
        'oauth_type',
        'org_id',
        'role_attr_extraction',
        'role_attr_from',
        'site_id',
        'mtype',
    ]

    def __init__(self,
                 name=None,
                 created_time=APIHelper.SKIP,
                 custom_logout_url=APIHelper.SKIP,
                 default_role=APIHelper.SKIP,
                 domain=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 idp_cert=APIHelper.SKIP,
                 idp_sign_algo=APIHelper.SKIP,
                 idp_sso_url=APIHelper.SKIP,
                 idp_type='saml',
                 ignore_unmatched_roles=APIHelper.SKIP,
                 issuer=APIHelper.SKIP,
                 ldap_base_dn=APIHelper.SKIP,
                 ldap_bind_dn=APIHelper.SKIP,
                 ldap_bind_password=APIHelper.SKIP,
                 ldap_certs=APIHelper.SKIP,
                 ldap_client_cert=APIHelper.SKIP,
                 ldap_client_key=APIHelper.SKIP,
                 ldap_group_attr=APIHelper.SKIP,
                 ldap_group_dn=APIHelper.SKIP,
                 ldap_group_filter=APIHelper.SKIP,
                 ldap_server_hosts=APIHelper.SKIP,
                 ldap_type='azure',
                 ldap_user_filter=APIHelper.SKIP,
                 modified_time=APIHelper.SKIP,
                 msp_id=APIHelper.SKIP,
                 nameid_format='email',
                 oauth_cc_client_id=APIHelper.SKIP,
                 oauth_cc_client_secret=APIHelper.SKIP,
                 oauth_discovery_url=APIHelper.SKIP,
                 oauth_ropc_client_id=APIHelper.SKIP,
                 oauth_ropc_secret=APIHelper.SKIP,
                 oauth_tenant_id=APIHelper.SKIP,
                 oauth_type='azure',
                 org_id=APIHelper.SKIP,
                 role_attr_extraction=APIHelper.SKIP,
                 role_attr_from='role',
                 site_id=APIHelper.SKIP,
                 mtype=APIHelper.SKIP):
        """Constructor for the Sso class"""

        # Initialize members of the class
        if created_time is not APIHelper.SKIP:
            self.created_time = created_time 
        if custom_logout_url is not APIHelper.SKIP:
            self.custom_logout_url = custom_logout_url 
        if default_role is not APIHelper.SKIP:
            self.default_role = default_role 
        if domain is not APIHelper.SKIP:
            self.domain = domain 
        if id is not APIHelper.SKIP:
            self.id = id 
        if idp_cert is not APIHelper.SKIP:
            self.idp_cert = idp_cert 
        if idp_sign_algo is not APIHelper.SKIP:
            self.idp_sign_algo = idp_sign_algo 
        if idp_sso_url is not APIHelper.SKIP:
            self.idp_sso_url = idp_sso_url 
        self.idp_type = idp_type 
        if ignore_unmatched_roles is not APIHelper.SKIP:
            self.ignore_unmatched_roles = ignore_unmatched_roles 
        if issuer is not APIHelper.SKIP:
            self.issuer = issuer 
        if ldap_base_dn is not APIHelper.SKIP:
            self.ldap_base_dn = ldap_base_dn 
        if ldap_bind_dn is not APIHelper.SKIP:
            self.ldap_bind_dn = ldap_bind_dn 
        if ldap_bind_password is not APIHelper.SKIP:
            self.ldap_bind_password = ldap_bind_password 
        if ldap_certs is not APIHelper.SKIP:
            self.ldap_certs = ldap_certs 
        if ldap_client_cert is not APIHelper.SKIP:
            self.ldap_client_cert = ldap_client_cert 
        if ldap_client_key is not APIHelper.SKIP:
            self.ldap_client_key = ldap_client_key 
        if ldap_group_attr is not APIHelper.SKIP:
            self.ldap_group_attr = ldap_group_attr 
        if ldap_group_dn is not APIHelper.SKIP:
            self.ldap_group_dn = ldap_group_dn 
        if ldap_group_filter is not APIHelper.SKIP:
            self.ldap_group_filter = ldap_group_filter 
        if ldap_server_hosts is not APIHelper.SKIP:
            self.ldap_server_hosts = ldap_server_hosts 
        self.ldap_type = ldap_type 
        if ldap_user_filter is not APIHelper.SKIP:
            self.ldap_user_filter = ldap_user_filter 
        if modified_time is not APIHelper.SKIP:
            self.modified_time = modified_time 
        if msp_id is not APIHelper.SKIP:
            self.msp_id = msp_id 
        self.name = name 
        self.nameid_format = nameid_format 
        if oauth_cc_client_id is not APIHelper.SKIP:
            self.oauth_cc_client_id = oauth_cc_client_id 
        if oauth_cc_client_secret is not APIHelper.SKIP:
            self.oauth_cc_client_secret = oauth_cc_client_secret 
        if oauth_discovery_url is not APIHelper.SKIP:
            self.oauth_discovery_url = oauth_discovery_url 
        if oauth_ropc_client_id is not APIHelper.SKIP:
            self.oauth_ropc_client_id = oauth_ropc_client_id 
        if oauth_ropc_secret is not APIHelper.SKIP:
            self.oauth_ropc_secret = oauth_ropc_secret 
        if oauth_tenant_id is not APIHelper.SKIP:
            self.oauth_tenant_id = oauth_tenant_id 
        self.oauth_type = oauth_type 
        if org_id is not APIHelper.SKIP:
            self.org_id = org_id 
        if role_attr_extraction is not APIHelper.SKIP:
            self.role_attr_extraction = role_attr_extraction 
        self.role_attr_from = role_attr_from 
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        name = dictionary.get("name") if dictionary.get("name") else None
        created_time = dictionary.get("created_time") if dictionary.get("created_time") else APIHelper.SKIP
        custom_logout_url = dictionary.get("custom_logout_url") if dictionary.get("custom_logout_url") else APIHelper.SKIP
        default_role = dictionary.get("default_role") if dictionary.get("default_role") else APIHelper.SKIP
        domain = dictionary.get("domain") if dictionary.get("domain") else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        idp_cert = dictionary.get("idp_cert") if dictionary.get("idp_cert") else APIHelper.SKIP
        idp_sign_algo = dictionary.get("idp_sign_algo") if dictionary.get("idp_sign_algo") else APIHelper.SKIP
        idp_sso_url = dictionary.get("idp_sso_url") if dictionary.get("idp_sso_url") else APIHelper.SKIP
        idp_type = dictionary.get("idp_type") if dictionary.get("idp_type") else 'saml'
        ignore_unmatched_roles = dictionary.get("ignore_unmatched_roles") if "ignore_unmatched_roles" in dictionary.keys() else APIHelper.SKIP
        issuer = dictionary.get("issuer") if dictionary.get("issuer") else APIHelper.SKIP
        ldap_base_dn = dictionary.get("ldap_base_dn") if dictionary.get("ldap_base_dn") else APIHelper.SKIP
        ldap_bind_dn = dictionary.get("ldap_bind_dn") if dictionary.get("ldap_bind_dn") else APIHelper.SKIP
        ldap_bind_password = dictionary.get("ldap_bind_password") if dictionary.get("ldap_bind_password") else APIHelper.SKIP
        ldap_certs = dictionary.get("ldap_certs") if dictionary.get("ldap_certs") else APIHelper.SKIP
        ldap_client_cert = dictionary.get("ldap_client_cert") if dictionary.get("ldap_client_cert") else APIHelper.SKIP
        ldap_client_key = dictionary.get("ldap_client_key") if dictionary.get("ldap_client_key") else APIHelper.SKIP
        ldap_group_attr = dictionary.get("ldap_group_attr") if dictionary.get("ldap_group_attr") else APIHelper.SKIP
        ldap_group_dn = dictionary.get("ldap_group_dn") if dictionary.get("ldap_group_dn") else APIHelper.SKIP
        ldap_group_filter = dictionary.get("ldap_group_filter") if dictionary.get("ldap_group_filter") else APIHelper.SKIP
        ldap_server_hosts = dictionary.get("ldap_server_hosts") if dictionary.get("ldap_server_hosts") else APIHelper.SKIP
        ldap_type = dictionary.get("ldap_type") if dictionary.get("ldap_type") else 'azure'
        ldap_user_filter = dictionary.get("ldap_user_filter") if dictionary.get("ldap_user_filter") else APIHelper.SKIP
        modified_time = dictionary.get("modified_time") if dictionary.get("modified_time") else APIHelper.SKIP
        msp_id = dictionary.get("msp_id") if dictionary.get("msp_id") else APIHelper.SKIP
        nameid_format = dictionary.get("nameid_format") if dictionary.get("nameid_format") else 'email'
        oauth_cc_client_id = dictionary.get("oauth_cc_client_id") if dictionary.get("oauth_cc_client_id") else APIHelper.SKIP
        oauth_cc_client_secret = dictionary.get("oauth_cc_client_secret") if dictionary.get("oauth_cc_client_secret") else APIHelper.SKIP
        oauth_discovery_url = dictionary.get("oauth_discovery_url") if dictionary.get("oauth_discovery_url") else APIHelper.SKIP
        oauth_ropc_client_id = dictionary.get("oauth_ropc_client_id") if dictionary.get("oauth_ropc_client_id") else APIHelper.SKIP
        oauth_ropc_secret = dictionary.get("oauth_ropc_secret") if dictionary.get("oauth_ropc_secret") else APIHelper.SKIP
        oauth_tenant_id = dictionary.get("oauth_tenant_id") if dictionary.get("oauth_tenant_id") else APIHelper.SKIP
        oauth_type = dictionary.get("oauth_type") if dictionary.get("oauth_type") else 'azure'
        org_id = dictionary.get("org_id") if dictionary.get("org_id") else APIHelper.SKIP
        role_attr_extraction = dictionary.get("role_attr_extraction") if dictionary.get("role_attr_extraction") else APIHelper.SKIP
        role_attr_from = dictionary.get("role_attr_from") if dictionary.get("role_attr_from") else 'role'
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   created_time,
                   custom_logout_url,
                   default_role,
                   domain,
                   id,
                   idp_cert,
                   idp_sign_algo,
                   idp_sso_url,
                   idp_type,
                   ignore_unmatched_roles,
                   issuer,
                   ldap_base_dn,
                   ldap_bind_dn,
                   ldap_bind_password,
                   ldap_certs,
                   ldap_client_cert,
                   ldap_client_key,
                   ldap_group_attr,
                   ldap_group_dn,
                   ldap_group_filter,
                   ldap_server_hosts,
                   ldap_type,
                   ldap_user_filter,
                   modified_time,
                   msp_id,
                   nameid_format,
                   oauth_cc_client_id,
                   oauth_cc_client_secret,
                   oauth_discovery_url,
                   oauth_ropc_client_id,
                   oauth_ropc_secret,
                   oauth_tenant_id,
                   oauth_type,
                   org_id,
                   role_attr_extraction,
                   role_attr_from,
                   site_id,
                   mtype)
