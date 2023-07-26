# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.passphrase_rules import PassphraseRules
from mistapi.models.sso_2 import Sso2


class PskPortal(object):

    """Implementation of the 'psk_portal' model.

    TODO: type model description here.

    Attributes:
        auth (Auth1Enum): Note: `sponsor` not yet available
        bg_image_url (string): TODO: type description here.
        cleanup_psk (bool): used to cleanup exited psk when portal delete or
            ssid changed
        created_time (int): TODO: type description here.
        expire_time (int): unit min
        expiry_notification_time (int): Number of days before psk is expired.
            Used as to when to start sending reminder notification when the
            psk is about to expire
        hide_psks_created_by_other_admins (bool): only if `type`==`admin`
        id (string): TODO: type description here.
        max_usage (int): `max_usage`==`0` means unlimited
        modified_time (int): TODO: type description here.
        name (string): TODO: type description here.
        notify_expiry (bool): If set to true, reminder notification will be
            sent when psk is about to expire
        notify_on_create_or_edit (bool): TODO: type description here.
        org_id (string): TODO: type description here.
        passphrase_rules (PassphraseRules): TODO: type description here.
        required_fields (list of string): what information to ask for (email
            is required by default)
        role (string): TODO: type description here.
        ssid (string): intended SSID
        sso (Sso2): if `auth`==`sso`
        template_url (string): UI customization
        thumbnail_url (string): TODO: type description here.
        mtype (Type35Enum): for personal psk portal
        vlan_id (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "ssid": 'ssid',
        "auth": 'auth',
        "bg_image_url": 'bg_image_url',
        "cleanup_psk": 'cleanup_psk',
        "created_time": 'created_time',
        "expire_time": 'expire_time',
        "expiry_notification_time": 'expiry_notification_time',
        "hide_psks_created_by_other_admins": 'hide_psks_created_by_other_admins',
        "id": 'id',
        "max_usage": 'max_usage',
        "modified_time": 'modified_time',
        "notify_expiry": 'notify_expiry',
        "notify_on_create_or_edit": 'notify_on_create_or_edit',
        "org_id": 'org_id',
        "passphrase_rules": 'passphrase_rules',
        "required_fields": 'required_fields',
        "role": 'role',
        "sso": 'sso',
        "template_url": 'template_url',
        "thumbnail_url": 'thumbnail_url',
        "mtype": 'type',
        "vlan_id": 'vlan_id'
    }

    _optionals = [
        'auth',
        'bg_image_url',
        'cleanup_psk',
        'created_time',
        'expire_time',
        'expiry_notification_time',
        'hide_psks_created_by_other_admins',
        'id',
        'max_usage',
        'modified_time',
        'notify_expiry',
        'notify_on_create_or_edit',
        'org_id',
        'passphrase_rules',
        'required_fields',
        'role',
        'sso',
        'template_url',
        'thumbnail_url',
        'mtype',
        'vlan_id',
    ]

    def __init__(self,
                 name=None,
                 ssid=None,
                 auth='sso',
                 bg_image_url=APIHelper.SKIP,
                 cleanup_psk=False,
                 created_time=APIHelper.SKIP,
                 expire_time=APIHelper.SKIP,
                 expiry_notification_time=APIHelper.SKIP,
                 hide_psks_created_by_other_admins=False,
                 id=APIHelper.SKIP,
                 max_usage=0,
                 modified_time=APIHelper.SKIP,
                 notify_expiry=APIHelper.SKIP,
                 notify_on_create_or_edit=False,
                 org_id=APIHelper.SKIP,
                 passphrase_rules=APIHelper.SKIP,
                 required_fields=APIHelper.SKIP,
                 role=APIHelper.SKIP,
                 sso=APIHelper.SKIP,
                 template_url=APIHelper.SKIP,
                 thumbnail_url=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 vlan_id=APIHelper.SKIP):
        """Constructor for the PskPortal class"""

        # Initialize members of the class
        self.auth = auth 
        if bg_image_url is not APIHelper.SKIP:
            self.bg_image_url = bg_image_url 
        self.cleanup_psk = cleanup_psk 
        if created_time is not APIHelper.SKIP:
            self.created_time = created_time 
        if expire_time is not APIHelper.SKIP:
            self.expire_time = expire_time 
        if expiry_notification_time is not APIHelper.SKIP:
            self.expiry_notification_time = expiry_notification_time 
        self.hide_psks_created_by_other_admins = hide_psks_created_by_other_admins 
        if id is not APIHelper.SKIP:
            self.id = id 
        self.max_usage = max_usage 
        if modified_time is not APIHelper.SKIP:
            self.modified_time = modified_time 
        self.name = name 
        if notify_expiry is not APIHelper.SKIP:
            self.notify_expiry = notify_expiry 
        self.notify_on_create_or_edit = notify_on_create_or_edit 
        if org_id is not APIHelper.SKIP:
            self.org_id = org_id 
        if passphrase_rules is not APIHelper.SKIP:
            self.passphrase_rules = passphrase_rules 
        if required_fields is not APIHelper.SKIP:
            self.required_fields = required_fields 
        if role is not APIHelper.SKIP:
            self.role = role 
        self.ssid = ssid 
        if sso is not APIHelper.SKIP:
            self.sso = sso 
        if template_url is not APIHelper.SKIP:
            self.template_url = template_url 
        if thumbnail_url is not APIHelper.SKIP:
            self.thumbnail_url = thumbnail_url 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if vlan_id is not APIHelper.SKIP:
            self.vlan_id = vlan_id 

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
        ssid = dictionary.get("ssid") if dictionary.get("ssid") else None
        auth = dictionary.get("auth") if dictionary.get("auth") else 'sso'
        bg_image_url = dictionary.get("bg_image_url") if dictionary.get("bg_image_url") else APIHelper.SKIP
        cleanup_psk = dictionary.get("cleanup_psk") if dictionary.get("cleanup_psk") else False
        created_time = dictionary.get("created_time") if dictionary.get("created_time") else APIHelper.SKIP
        expire_time = dictionary.get("expire_time") if dictionary.get("expire_time") else APIHelper.SKIP
        expiry_notification_time = dictionary.get("expiry_notification_time") if dictionary.get("expiry_notification_time") else APIHelper.SKIP
        hide_psks_created_by_other_admins = dictionary.get("hide_psks_created_by_other_admins") if dictionary.get("hide_psks_created_by_other_admins") else False
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        max_usage = dictionary.get("max_usage") if dictionary.get("max_usage") else 0
        modified_time = dictionary.get("modified_time") if dictionary.get("modified_time") else APIHelper.SKIP
        notify_expiry = dictionary.get("notify_expiry") if "notify_expiry" in dictionary.keys() else APIHelper.SKIP
        notify_on_create_or_edit = dictionary.get("notify_on_create_or_edit") if dictionary.get("notify_on_create_or_edit") else False
        org_id = dictionary.get("org_id") if dictionary.get("org_id") else APIHelper.SKIP
        passphrase_rules = PassphraseRules.from_dictionary(dictionary.get('passphrase_rules')) if 'passphrase_rules' in dictionary.keys() else APIHelper.SKIP
        required_fields = dictionary.get("required_fields") if dictionary.get("required_fields") else APIHelper.SKIP
        role = dictionary.get("role") if dictionary.get("role") else APIHelper.SKIP
        sso = Sso2.from_dictionary(dictionary.get('sso')) if 'sso' in dictionary.keys() else APIHelper.SKIP
        template_url = dictionary.get("template_url") if dictionary.get("template_url") else APIHelper.SKIP
        thumbnail_url = dictionary.get("thumbnail_url") if dictionary.get("thumbnail_url") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        vlan_id = dictionary.get("vlan_id") if dictionary.get("vlan_id") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   ssid,
                   auth,
                   bg_image_url,
                   cleanup_psk,
                   created_time,
                   expire_time,
                   expiry_notification_time,
                   hide_psks_created_by_other_admins,
                   id,
                   max_usage,
                   modified_time,
                   notify_expiry,
                   notify_on_create_or_edit,
                   org_id,
                   passphrase_rules,
                   required_fields,
                   role,
                   sso,
                   template_url,
                   thumbnail_url,
                   mtype,
                   vlan_id)