# Sites Wlans

```python
sites_wlans_controller = client.sites_wlans
```

## Class Name

`SitesWlansController`

## Methods

* [List Site Wlans](../../doc/controllers/sites-wlans.md#list-site-wlans)
* [Create Site Wlan](../../doc/controllers/sites-wlans.md#create-site-wlan)
* [List Site Wlan Derived](../../doc/controllers/sites-wlans.md#list-site-wlan-derived)
* [Delete Site Wlan](../../doc/controllers/sites-wlans.md#delete-site-wlan)
* [Get Site Wlan](../../doc/controllers/sites-wlans.md#get-site-wlan)
* [Update Site Wlan](../../doc/controllers/sites-wlans.md#update-site-wlan)
* [Upload Site Wlan Portal Image](../../doc/controllers/sites-wlans.md#upload-site-wlan-portal-image)
* [Update Site Wlan Portal Template](../../doc/controllers/sites-wlans.md#update-site-wlan-portal-template)
* [Test Site Wlan Telstra Setup](../../doc/controllers/sites-wlans.md#test-site-wlan-telstra-setup)
* [Test Site Wlan Twilio Setup](../../doc/controllers/sites-wlans.md#test-site-wlan-twilio-setup)


# List Site Wlans

Get List of Site WLANs

```python
def list_site_wlans(self,
                   site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of Wlan`](../../doc/models/wlan.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_wlans_controller.list_site_wlans(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "acct_interim_interval": 0,
    "acct_servers": [
      {
        "host": "string",
        "port": 0,
        "secret": "string"
      }
    ],
    "airwatch": {
      "api_key": "string",
      "console_url": "string",
      "enabled": true,
      "password": "string",
      "username": "string"
    },
    "allow_ipv6_ndp": true,
    "allow_mdns": true,
    "ap_ids": [
      "b069b358-4c97-5319-1f8c-7c5ca64d6ab1"
    ],
    "app_limit": {
      "apps": {},
      "enabled": true,
      "wxtag_ids": {}
    },
    "app_qos": {
      "apps": {
        "skype-business-video": {
          "dscp": 0,
          "dst_subnet": "string",
          "src_subnet": "string"
        },
        "skype-business-voice": {
          "dscp": 0
        }
      },
      "enabled": true,
      "others": [
        {
          "dscp": 0,
          "dst_subnet": "string",
          "port_ranges": "string",
          "protocol": "string",
          "src_subnet": "string"
        }
      ]
    },
    "apply_to": "site",
    "arp_filter": true,
    "auth": {
      "eap_reauth": true,
      "enable_mac_auth": true,
      "key_idx": 1,
      "keys": [
        "string"
      ],
      "multi_psk_only": true,
      "owe": "string",
      "pairwise": [
        "string"
      ],
      "private_wlan": true,
      "psk": "string123",
      "type": "open",
      "wep_as_secondary_auth": true
    },
    "auth_server_selection": "ordered",
    "auth_servers": [
      {
        "host": "string",
        "port": 0,
        "secret": "string"
      }
    ],
    "auth_servers_nas_id": "string",
    "auth_servers_nas_ip": "string",
    "auth_servers_retries": 0,
    "auth_servers_timeout": 0,
    "band": "string",
    "band_steer": true,
    "band_steer_force_band5": true,
    "block_blacklist_clients": true,
    "bonjour": {
      "additional_vlan_ids": [
        0
      ],
      "enabled": true,
      "services": {
        "property1": {
          "disable_local": true,
          "radius_groups": [
            "string"
          ],
          "scope": "string"
        },
        "property2": {
          "disable_local": true,
          "radius_groups": [
            "string"
          ],
          "scope": "string"
        }
      }
    },
    "cisco_cwa": {
      "allowed_hostnames": [
        "string"
      ],
      "allowed_subnets": [
        "string"
      ],
      "enabled": true
    },
    "client_limit_down": 0,
    "client_limit_down_enabled": true,
    "client_limit_up": 0,
    "client_limit_up_enabled": true,
    "coa_servers": [
      {
        "disable_event_timestamp_check": true,
        "enabled": true,
        "ip": "192.168.1.1",
        "port": "3799",
        "secret": "string"
      }
    ],
    "created_time": 0,
    "disable_11ax": true,
    "disable_uapsd": true,
    "disable_wmm": true,
    "dns_server_rewrite": {
      "enabled": true,
      "radius_groups": {}
    },
    "dtim": 0,
    "dynamic_psk": {
      "default_vlan_id": 1,
      "enabled": true,
      "source": "radius",
      "vlan_ids": [
        1
      ]
    },
    "dynamic_vlan": {
      "default_vlan_id": 1,
      "enabled": true,
      "local_vlan_ids": [
        1
      ],
      "type": "standard",
      "vlans": {}
    },
    "enable_wireless_bridging": true,
    "enabled": true,
    "hide_ssid": true,
    "hostname_ie": true,
    "hotspot20": {
      "enabled": true,
      "operators": [
        "string"
      ],
      "venue_name": "string"
    },
    "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "interface": "all",
    "isolation": true,
    "legacy_overds": true,
    "limit_bcast": true,
    "limit_probe_response": true,
    "max_idletime": 60,
    "modified_time": 0,
    "msp_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "mxtunnel_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "no_static_dns": true,
    "no_static_ip": true,
    "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "portal": {
      "amazon_client_id": "string",
      "amazon_client_secret": "string",
      "amazon_email_domains": [
        "string"
      ],
      "amazon_enabled": true,
      "auth": "none",
      "azure_client_id": "string",
      "azure_client_secret": "string",
      "azure_enabled": true,
      "azure_tenant_id": "string",
      "bypass_when_cloud_down": true,
      "email_enabled": true,
      "enabled": true,
      "expire": 0,
      "external_portal_url": "string",
      "facebook_client_id": "string",
      "facebook_client_secret": "string",
      "facebook_email_domains": [
        "string"
      ],
      "facebook_enabled": true,
      "forward": true,
      "forward_url": "string",
      "google_email_domains": [
        "string"
      ],
      "google_enabled": true,
      "microsoft_client_id": "string",
      "microsoft_client_secret": "string",
      "microsoft_email_domains": [
        "string"
      ],
      "microsoft_enabled": true,
      "passphrase_enabled": true,
      "password": "string",
      "portal_allowed_hostnames": "string",
      "portal_allowed_subnets": "string",
      "portal_api_secret": "string",
      "portal_denied_hostnames": "string",
      "portal_image": "string",
      "portal_sso_url": "string",
      "privacy": true,
      "sms_enabled": true,
      "sms_provider": "manual",
      "sponsor_email_domains": [
        "string"
      ],
      "sponsor_enabled": true,
      "sponsor_link_validity_duration": "60",
      "sponsors": {
        "property1": "string",
        "property2": "string"
      },
      "sso_default_role": "string",
      "sso_idp_cert": "string",
      "sso_idp_sign_algo": "string",
      "sso_idp_sso_url": "string",
      "sso_issuer": "string",
      "thumbnail": "string",
      "twilio_auth_token": "string",
      "twilio_phone_number": "string",
      "twilio_sid": "string"
    },
    "portal_allowed_hostnames": [
      "string"
    ],
    "portal_allowed_subnets": [
      "string"
    ],
    "portal_api_secret": "string",
    "portal_denied_hostnames": [
      "string"
    ],
    "portal_image": "http://example.com",
    "portal_sso_url": "string",
    "portal_template_url": "string",
    "qos": {
      "class": "best_effort",
      "overwrite": true
    },
    "radsec": {
      "enabled": true,
      "server_name": "string",
      "servers": [
        {
          "host": "string",
          "port": 0
        }
      ],
      "use_mxedge": true
    },
    "rateset": {
      "24": {
        "ht": "string",
        "legacy": [
          "string"
        ],
        "min_rssi": 0,
        "template": "string",
        "vht": "string"
      },
      "5": {
        "ht": "string",
        "legacy": [
          "string"
        ],
        "min_rssi": 0,
        "template": "string",
        "vht": "string"
      }
    },
    "roam_mode": "11r",
    "schedule": {
      "enabled": true,
      "hours": {}
    },
    "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "sle_excluded": true,
    "ssid": "string",
    "thumbnail": "http://example.com",
    "use_eapol_v1": true,
    "vlan_enabled": true,
    "vlan_id": 1,
    "vlan_ids": [
      1
    ],
    "vlan_pooling": true,
    "wlan_limit_down": 0,
    "wlan_limit_down_enabled": true,
    "wlan_limit_up": 0,
    "wlan_limit_up_enabled": true,
    "wxtag_ids": [
      "b069b358-4c97-5319-1f8c-7c5ca64d6ab1"
    ],
    "wxtunnel_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "wxtunnel_remote_id": "string"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWlans401ErrorException`](../../doc/models/api-v1-sites-wlans-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWlans403ErrorException`](../../doc/models/api-v1-sites-wlans-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWlans404ErrorException`](../../doc/models/api-v1-sites-wlans-404-error-exception.md) |


# Create Site Wlan

Create Site WLAN

```python
def create_site_wlan(self,
                    site_id,
                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Wlan`](../../doc/models/wlan.md) | Body, Optional | Request Body |

## Response Type

[`Wlan`](../../doc/models/wlan.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Wlan(
    ssid='string',
    acct_interim_interval=0,
    acct_servers=[
        AcctServer(
            host='string',
            port=0,
            secret='string'
        )
    ],
    airwatch=WlanAirwatch(
        api_key='string',
        console_url='string',
        enabled=True,
        password='string',
        username='string'
    ),
    allow_ipv_6_ndp=True,
    allow_mdns=True,
    ap_ids=[
        'b069b358-4c97-5319-1f8c-7c5ca64d6ab1'
    ],
    app_limit=AppLimit(
        apps={},
        enabled=True,
        wxtag_ids={}
    ),
    app_qos=WlanAppQos(
        apps=Apps(
            skype_business_video=SkypeBusinessVideo(
                dscp=0,
                dst_subnet='string',
                src_subnet='string'
            ),
            skype_business_voice=SkypeBusinessVoice(
                dscp=0
            )
        ),
        enabled=True,
        others=[
            Other(
                dscp=0,
                dst_subnet='string',
                port_ranges='string',
                protocol='string',
                src_subnet='string'
            )
        ]
    ),
    apply_to=ApplyToEnum.SITE,
    arp_filter=True,
    auth=WlanAuth(
        mtype=Type38Enum.OPEN,
        eap_reauth=True,
        enable_mac_auth=True,
        key_idx=1,
        keys=[
            'string'
        ],
        multi_psk_only=True,
        owe='string',
        pairwise=[
            'string'
        ],
        private_wlan=True,
        psk='string123',
        wep_as_secondary_auth=True
    ),
    auth_server_selection=AuthServerSelectionEnum.ORDERED,
    auth_servers=[
        AuthServer(
            host='string',
            port=0,
            secret='string'
        )
    ],
    auth_servers_nas_id='string',
    auth_servers_nas_ip='string',
    auth_servers_retries=0,
    auth_servers_timeout=0,
    band='string',
    band_steer=True,
    band_steer_force_band_5=True,
    block_blacklist_clients=True,
    bonjour=WlanBonjour(
        additional_vlan_ids=[
            0
        ],
        services={
            "service_name2": Services(
                disable_local=True,
                radius_groups=[
                    'string'
                ],
                scope='string'
            )
        },
        enabled=True
    ),
    cisco_cwa=WlanCiscoCwa(
        allowed_hostnames=[
            'string'
        ],
        allowed_subnets=[
            'string'
        ],
        enabled=True
    ),
    client_limit_down=0,
    client_limit_down_enabled=True,
    client_limit_up=0,
    client_limit_up_enabled=True,
    coa_servers=[
        CoaServer(
            disable_event_timestamp_check=True,
            enabled=True,
            ip='192.168.1.1',
            port='3799',
            secret='string'
        )
    ],
    disable_11_ax=True,
    disable_uapsd=True,
    disable_wmm=True,
    dns_server_rewrite=DnsServerRewrite(
        enabled=True,
        radius_groups={}
    ),
    dtim=0,
    dynamic_psk=DynamicPsk(
        enabled=True
    ),
    dynamic_vlan=DynamicVlan1(
        default_vlan_id=1,
        enabled=True,
        local_vlan_ids=[
            1
        ],
        mtype=Type39Enum.STANDARD,
        vlans={}
    ),
    enable_wireless_bridging=True,
    enabled=True,
    hide_ssid=True,
    hostname_ie=True,
    hotspot_20=WlanHotspot20(
        enabled=True,
        operators=[
            'string'
        ],
        venue_name='string'
    ),
    interface=InterfaceEnum.ALL,
    isolation=True,
    legacy_overds=True,
    limit_bcast=True,
    limit_probe_response=True,
    max_idletime=60,
    no_static_dns=True,
    no_static_ip=True,
    portal=WlanPortal(
        amazon_client_id='string',
        amazon_client_secret='string',
        amazon_email_domains=[
            'string'
        ],
        amazon_enabled=True,
        auth=Auth2Enum.NONE,
        azure_client_id='string',
        azure_client_secret='string',
        azure_enabled=True,
        azure_tenant_id='string',
        bypass_when_cloud_down=True,
        email_enabled=True,
        enabled=True,
        expire=0,
        external_portal_url='string',
        facebook_client_id='string',
        facebook_client_secret='string',
        facebook_email_domains=[
            'string'
        ],
        facebook_enabled=True,
        forward=True,
        forward_url='string',
        google_email_domains=[
            'string'
        ],
        google_enabled=True,
        microsoft_client_id='string',
        microsoft_client_secret='string',
        microsoft_email_domains=[
            'string'
        ],
        microsoft_enabled=True,
        passphrase_enabled=True,
        password='string',
        portal_allowed_hostnames='string',
        portal_allowed_subnets='string',
        portal_api_secret='string',
        portal_denied_hostnames='string',
        portal_image='string',
        portal_sso_url='string',
        privacy=True,
        sms_enabled=True,
        sms_provider=SmsProviderEnum.MANUAL,
        sponsor_email_domains=[
            'string'
        ],
        sponsor_enabled=True,
        sponsor_link_validity_duration='60',
        sso_default_role='string',
        sso_idp_cert='string',
        sso_idp_sign_algo='string',
        sso_idp_sso_url='string',
        sso_issuer='string',
        thumbnail='string',
        twilio_auth_token='string',
        twilio_phone_number='string',
        twilio_sid='string'
    ),
    portal_allowed_hostnames=[
        'string'
    ],
    portal_allowed_subnets=[
        'string'
    ],
    portal_api_secret='string',
    portal_denied_hostnames=[
        'string'
    ],
    portal_image='http://example.com',
    portal_sso_url='string',
    portal_template_url='string',
    qos=Qos(
        mclass=ClassEnum.BEST_EFFORT,
        overwrite=True
    ),
    radsec=Radsec(
        enabled=True,
        server_name='string',
        servers=[
            Server(
                host='string',
                port=0
            )
        ]
    ),
    rateset={
        "24": WlanDatarates(
            ht='string',
            legacy=[
                'string'
            ],
            min_rssi=0,
            template='string',
            vht='string'
        ),
        "5": WlanDatarates(
            ht='string',
            legacy=[
                'string'
            ],
            min_rssi=0,
            template='string',
            vht='string'
        )
    },
    roam_mode=RoamModeEnum.ENUM_11R,
    schedule=Schedule(
        enabled=True,
        hours={}
    ),
    sle_excluded=True,
    thumbnail='http://example.com',
    use_eapol_v_1=True,
    vlan_enabled=True,
    vlan_id=1,
    vlan_ids=[
        1
    ],
    vlan_pooling=True,
    wlan_limit_down=0,
    wlan_limit_down_enabled=True,
    wlan_limit_up=0,
    wlan_limit_up_enabled=True,
    wxtag_ids=[
        'b069b358-4c97-5319-1f8c-7c5ca64d6ab1'
    ],
    wxtunnel_id='6f4bf402-45f9-2a56-6c8b-7f83d3bc98e9',
    wxtunnel_remote_id='string'
)

result = sites_wlans_controller.create_site_wlan(
    site_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "acct_interim_interval": 0,
  "acct_servers": [
    {
      "host": "string",
      "port": 1813,
      "secret": "string"
    }
  ],
  "airwatch": {
    "api_key": "string",
    "console_url": "string",
    "enabled": true,
    "password": "string",
    "username": "string"
  },
  "allow_ipv6_ndp": true,
  "allow_mdns": false,
  "ap_ids": [
    "097f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "app_limit": {
    "apps": {},
    "enabled": true,
    "wxtag_ids": {}
  },
  "app_qos": {
    "apps": {
      "skype-business-video": {
        "dscp": 0,
        "dst_subnet": "string",
        "src_subnet": "string"
      },
      "skype-business-voice": {
        "dscp": 0
      }
    },
    "enabled": true,
    "others": [
      {
        "dscp": 0,
        "dst_subnet": "string",
        "port_ranges": "string",
        "protocol": "string",
        "src_subnet": "string"
      }
    ]
  },
  "apply_to": "site",
  "arp_filter": false,
  "auth": {
    "eap_reauth": false,
    "enable_mac_auth": false,
    "key_idx": 1,
    "keys": [
      "string"
    ],
    "multi_psk_only": false,
    "owe": "string",
    "pairwise": [
      "wpa2-ccmp"
    ],
    "private_wlan": true,
    "psk": "stringst",
    "type": "open",
    "wep_as_secondary_auth": true
  },
  "auth_server_selection": "ordered",
  "auth_servers": [
    {
      "host": "string",
      "port": 1812,
      "secret": "string"
    }
  ],
  "auth_servers_nas_id": "string",
  "auth_servers_nas_ip": "string",
  "auth_servers_retries": 3,
  "auth_servers_timeout": 5,
  "band": "string",
  "band_steer": false,
  "band_steer_force_band5": false,
  "block_blacklist_clients": true,
  "bonjour": {
    "additional_vlan_ids": [
      0
    ],
    "enabled": false,
    "services": {
      "property1": {
        "disable_local": false,
        "radius_groups": [
          "string"
        ],
        "scope": "string"
      },
      "property2": {
        "disable_local": false,
        "radius_groups": [
          "string"
        ],
        "scope": "string"
      }
    }
  },
  "cisco_cwa": {
    "allowed_hostnames": [
      "string"
    ],
    "allowed_subnets": [
      "string"
    ],
    "enabled": true
  },
  "client_limit_down": 0,
  "client_limit_down_enabled": false,
  "client_limit_up": 0,
  "client_limit_up_enabled": false,
  "coa_servers": [
    {
      "disable_event_timestamp_check": true,
      "enabled": true,
      "ip": "192.168.0.1",
      "port": "string",
      "secret": "string"
    }
  ],
  "created_time": 0,
  "disable_11ax": false,
  "disable_ht_vht_rates": false,
  "disable_uapsd": false,
  "disable_wmm": false,
  "dns_server_rewrite": {
    "enabled": true,
    "radius_groups": {}
  },
  "dtim": 2,
  "dynamic_psk": {
    "default_psk": "stringst",
    "default_vlan_id": 0,
    "enabled": true,
    "source": "radius",
    "vlan_ids": [
      1
    ]
  },
  "dynamic_vlan": {
    "default_vlan_id": 999,
    "enabled": false,
    "local_vlan_ids": [
      1
    ],
    "type": "standard",
    "vlans": {
      "property1": "string",
      "property2": "string"
    }
  },
  "enable_wireless_bridging": true,
  "enabled": true,
  "for_site": true,
  "hide_ssid": false,
  "hostname_ie": false,
  "hotspot20": {
    "enabled": true,
    "operators": [
      "string"
    ],
    "venue_name": "string"
  },
  "id": "197f6eca-6276-4993-bfeb-53cbbbba6f08",
  "interface": "all",
  "isolation": false,
  "legacy_overds": true,
  "limit_bcast": false,
  "limit_probe_response": true,
  "max_idletime": 1800,
  "modified_time": 0,
  "msp_id": "c0cf23fc-d82f-4219-988c-82fb61d8c875",
  "mxtunnel": {},
  "mxtunnel_id": "6741baab-cbd6-45bd-9e5b-93e8eede3c80",
  "mxtunnel_name": [
    "default"
  ],
  "no_static_dns": false,
  "no_static_ip": false,
  "org_id": "a40f5d1f-d889-42e9-94ea-b9b33585fc6b",
  "portal": {
    "amazon_client_id": "string",
    "amazon_client_secret": "string",
    "amazon_email_domains": [
      "string"
    ],
    "amazon_enabled": true,
    "auth": "none",
    "azure_client_id": "string",
    "azure_client_secret": "string",
    "azure_enabled": true,
    "azure_tenant_id": "string",
    "broadnet_password": "string",
    "broadnet_sid": "string",
    "broadnet_user_id": "string",
    "bypass_when_cloud_down": false,
    "clickatell_api_key": "string",
    "email_enabled": true,
    "enabled": false,
    "expire": 1440,
    "external_portal_url": "string",
    "facebook_client_id": "string",
    "facebook_client_secret": "string",
    "facebook_email_domains": [
      "string"
    ],
    "facebook_enabled": true,
    "forward": false,
    "forward_url": "string",
    "google_client_id": "string",
    "google_client_secret": "string",
    "google_email_domains": [
      "string"
    ],
    "google_enabled": true,
    "gupshup_password": "string",
    "gupshup_userid": "string",
    "microsoft_client_id": "string",
    "microsoft_client_secret": "string",
    "microsoft_email_domains": [
      "string"
    ],
    "microsoft_enabled": true,
    "passphrase_enabled": true,
    "password": "string",
    "portal_allowed_hostnames": "string",
    "portal_allowed_subnets": "string",
    "portal_api_secret": "string",
    "portal_denied_hostnames": "string",
    "portal_image": "string",
    "portal_sso_url": "string",
    "predefined_sponsors_enabled": true,
    "privacy": true,
    "puzzel_password": "string",
    "puzzel_service_id": "string",
    "puzzel_username": "string",
    "smsMessageFormat": "string",
    "sms_enabled": true,
    "sms_provider": "manual",
    "sponsor_email_domains": [
      "string"
    ],
    "sponsor_enabled": true,
    "sponsor_link_validity_duration": "string",
    "sponsor_notify_all": false,
    "sponsors": {
      "property1": "string",
      "property2": "string"
    },
    "sso_default_role": "string",
    "sso_forced_role": "string",
    "sso_idp_cert": "string",
    "sso_idp_sign_algo": "string",
    "sso_idp_sso_url": "string",
    "sso_issuer": "string",
    "sso_nameid_format": "email",
    "thumbnail": "string",
    "twilio_auth_token": "string",
    "twilio_phone_number": "string",
    "twilio_sid": "string"
  },
  "portal_allowed_hostnames": [
    "string"
  ],
  "portal_allowed_subnets": [
    "string"
  ],
  "portal_api_secret": "string",
  "portal_denied_hostnames": [
    "string"
  ],
  "portal_image": "http://example.com",
  "portal_sso_url": "string",
  "portal_template_url": "string",
  "qos": {
    "class": "best_effort",
    "overwrite": false
  },
  "radsec": {
    "enabled": true,
    "idle_timeout": 0,
    "server_name": "string",
    "servers": [
      {
        "host": "string",
        "port": 0
      }
    ],
    "use_mxedge": true
  },
  "rateset": {
    "24": {
      "ht": "string",
      "legacy": [
        "string"
      ],
      "min_rssi": 0,
      "template": "string",
      "vht": "string"
    },
    "5": {
      "ht": "string",
      "legacy": [
        "string"
      ],
      "min_rssi": 0,
      "template": "string",
      "vht": "string"
    }
  },
  "roam_mode": "none",
  "schedule": {
    "enabled": false,
    "hours": {}
  },
  "site_id": "72771e6a-6f5e-4de4-a5b9-1266c4197811",
  "sle_excluded": false,
  "ssid": "string",
  "template_id": "c6d67e98-83ea-49f0-8812-e4abae2b68bc",
  "thumbnail": "http://example.com",
  "use_eapol_v1": false,
  "vlan_enabled": false,
  "vlan_id": 1,
  "vlan_ids": [
    1
  ],
  "vlan_pooling": false,
  "wlan_limit_down": 0,
  "wlan_limit_down_enabled": false,
  "wlan_limit_up": 0,
  "wlan_limit_up_enabled": false,
  "wxtag_ids": [
    "297f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "wxtunnel_id": "string",
  "wxtunnel_remote_id": "string"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWlans401ErrorException`](../../doc/models/api-v1-sites-wlans-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWlans403ErrorException`](../../doc/models/api-v1-sites-wlans-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWlans404ErrorException`](../../doc/models/api-v1-sites-wlans-404-error-exception.md) |


# List Site Wlan Derived

Get Wlans Derived

```python
def list_site_wlan_derived(self,
                          site_id,
                          resolve=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `resolve` | `bool` | Query, Optional | whether to resolve SITE_VARS<br>**Default**: `False` |

## Response Type

[`List of Wlan`](../../doc/models/wlan.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

resolve = True

result = sites_wlans_controller.list_site_wlan_derived(
    site_id,
    resolve
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "acct_interim_interval": 0,
    "acct_servers": [
      {
        "host": "string",
        "port": 0,
        "secret": "string"
      }
    ],
    "airwatch": {
      "api_key": "string",
      "console_url": "string",
      "enabled": true,
      "password": "string",
      "username": "string"
    },
    "allow_ipv6_ndp": true,
    "allow_mdns": true,
    "ap_ids": [
      "b069b358-4c97-5319-1f8c-7c5ca64d6ab1"
    ],
    "app_limit": {
      "apps": {},
      "enabled": true,
      "wxtag_ids": {}
    },
    "app_qos": {
      "apps": {
        "skype-business-video": {
          "dscp": 0,
          "dst_subnet": "string",
          "src_subnet": "string"
        },
        "skype-business-voice": {
          "dscp": 0
        }
      },
      "enabled": true,
      "others": [
        {
          "dscp": 0,
          "dst_subnet": "string",
          "port_ranges": "string",
          "protocol": "string",
          "src_subnet": "string"
        }
      ]
    },
    "apply_to": "site",
    "arp_filter": true,
    "auth": {
      "eap_reauth": true,
      "enable_mac_auth": true,
      "key_idx": 1,
      "keys": [
        "string"
      ],
      "multi_psk_only": true,
      "owe": "string",
      "pairwise": [
        "string"
      ],
      "private_wlan": true,
      "psk": "string123",
      "type": "open",
      "wep_as_secondary_auth": true
    },
    "auth_server_selection": "ordered",
    "auth_servers": [
      {
        "host": "string",
        "port": 0,
        "secret": "string"
      }
    ],
    "auth_servers_nas_id": "string",
    "auth_servers_nas_ip": "string",
    "auth_servers_retries": 0,
    "auth_servers_timeout": 0,
    "band": "string",
    "band_steer": true,
    "band_steer_force_band5": true,
    "block_blacklist_clients": true,
    "bonjour": {
      "additional_vlan_ids": [
        0
      ],
      "enabled": true,
      "services": {
        "property1": {
          "disable_local": true,
          "radius_groups": [
            "string"
          ],
          "scope": "string"
        },
        "property2": {
          "disable_local": true,
          "radius_groups": [
            "string"
          ],
          "scope": "string"
        }
      }
    },
    "cisco_cwa": {
      "allowed_hostnames": [
        "string"
      ],
      "allowed_subnets": [
        "string"
      ],
      "enabled": true
    },
    "client_limit_down": 0,
    "client_limit_down_enabled": true,
    "client_limit_up": 0,
    "client_limit_up_enabled": true,
    "coa_servers": [
      {
        "disable_event_timestamp_check": true,
        "enabled": true,
        "ip": "192.168.1.1",
        "port": "3799",
        "secret": "string"
      }
    ],
    "created_time": 0,
    "disable_11ax": true,
    "disable_uapsd": true,
    "disable_wmm": true,
    "dns_server_rewrite": {
      "enabled": true,
      "radius_groups": {}
    },
    "dtim": 0,
    "dynamic_psk": {
      "default_vlan_id": 1,
      "enabled": true,
      "source": "radius",
      "vlan_ids": [
        1
      ]
    },
    "dynamic_vlan": {
      "default_vlan_id": 1,
      "enabled": true,
      "local_vlan_ids": [
        1
      ],
      "type": "standard",
      "vlans": {}
    },
    "enable_wireless_bridging": true,
    "enabled": true,
    "hide_ssid": true,
    "hostname_ie": true,
    "hotspot20": {
      "enabled": true,
      "operators": [
        "string"
      ],
      "venue_name": "string"
    },
    "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "interface": "all",
    "isolation": true,
    "legacy_overds": true,
    "limit_bcast": true,
    "limit_probe_response": true,
    "max_idletime": 60,
    "modified_time": 0,
    "msp_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "mxtunnel_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "no_static_dns": true,
    "no_static_ip": true,
    "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "portal": {
      "amazon_client_id": "string",
      "amazon_client_secret": "string",
      "amazon_email_domains": [
        "string"
      ],
      "amazon_enabled": true,
      "auth": "none",
      "azure_client_id": "string",
      "azure_client_secret": "string",
      "azure_enabled": true,
      "azure_tenant_id": "string",
      "bypass_when_cloud_down": true,
      "email_enabled": true,
      "enabled": true,
      "expire": 0,
      "external_portal_url": "string",
      "facebook_client_id": "string",
      "facebook_client_secret": "string",
      "facebook_email_domains": [
        "string"
      ],
      "facebook_enabled": true,
      "forward": true,
      "forward_url": "string",
      "google_email_domains": [
        "string"
      ],
      "google_enabled": true,
      "microsoft_client_id": "string",
      "microsoft_client_secret": "string",
      "microsoft_email_domains": [
        "string"
      ],
      "microsoft_enabled": true,
      "passphrase_enabled": true,
      "password": "string",
      "portal_allowed_hostnames": "string",
      "portal_allowed_subnets": "string",
      "portal_api_secret": "string",
      "portal_denied_hostnames": "string",
      "portal_image": "string",
      "portal_sso_url": "string",
      "privacy": true,
      "sms_enabled": true,
      "sms_provider": "manual",
      "sponsor_email_domains": [
        "string"
      ],
      "sponsor_enabled": true,
      "sponsor_link_validity_duration": "60",
      "sponsors": {
        "property1": "string",
        "property2": "string"
      },
      "sso_default_role": "string",
      "sso_idp_cert": "string",
      "sso_idp_sign_algo": "string",
      "sso_idp_sso_url": "string",
      "sso_issuer": "string",
      "thumbnail": "string",
      "twilio_auth_token": "string",
      "twilio_phone_number": "string",
      "twilio_sid": "string"
    },
    "portal_allowed_hostnames": [
      "string"
    ],
    "portal_allowed_subnets": [
      "string"
    ],
    "portal_api_secret": "string",
    "portal_denied_hostnames": [
      "string"
    ],
    "portal_image": "http://example.com",
    "portal_sso_url": "string",
    "portal_template_url": "string",
    "qos": {
      "class": "best_effort",
      "overwrite": true
    },
    "radsec": {
      "enabled": true,
      "server_name": "string",
      "servers": [
        {
          "host": "string",
          "port": 0
        }
      ],
      "use_mxedge": true
    },
    "rateset": {
      "24": {
        "ht": "string",
        "legacy": [
          "string"
        ],
        "min_rssi": 0,
        "template": "string",
        "vht": "string"
      },
      "5": {
        "ht": "string",
        "legacy": [
          "string"
        ],
        "min_rssi": 0,
        "template": "string",
        "vht": "string"
      }
    },
    "roam_mode": "11r",
    "schedule": {
      "enabled": true,
      "hours": {}
    },
    "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "sle_excluded": true,
    "ssid": "string",
    "thumbnail": "http://example.com",
    "use_eapol_v1": true,
    "vlan_enabled": true,
    "vlan_id": 1,
    "vlan_ids": [
      1
    ],
    "vlan_pooling": true,
    "wlan_limit_down": 0,
    "wlan_limit_down_enabled": true,
    "wlan_limit_up": 0,
    "wlan_limit_up_enabled": true,
    "wxtag_ids": [
      "b069b358-4c97-5319-1f8c-7c5ca64d6ab1"
    ],
    "wxtunnel_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "wxtunnel_remote_id": "string"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWlansDerived401ErrorException`](../../doc/models/api-v1-sites-wlans-derived-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWlansDerived403ErrorException`](../../doc/models/api-v1-sites-wlans-derived-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWlansDerived404ErrorException`](../../doc/models/api-v1-sites-wlans-derived-404-error-exception.md) |


# Delete Site Wlan

Delete Site WLAN

```python
def delete_site_wlan(self,
                    site_id,
                    wlan_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `wlan_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

wlan_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_wlans_controller.delete_site_wlan(
    site_id,
    wlan_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWlans401ErrorException`](../../doc/models/api-v1-sites-wlans-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWlans403ErrorException`](../../doc/models/api-v1-sites-wlans-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWlans404ErrorException`](../../doc/models/api-v1-sites-wlans-404-error-exception.md) |


# Get Site Wlan

Get Site WLAN

```python
def get_site_wlan(self,
                 site_id,
                 wlan_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `wlan_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`Wlan`](../../doc/models/wlan.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

wlan_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_wlans_controller.get_site_wlan(
    site_id,
    wlan_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "acct_interim_interval": 0,
  "acct_servers": [
    {
      "host": "string",
      "port": 1813,
      "secret": "string"
    }
  ],
  "airwatch": {
    "api_key": "string",
    "console_url": "string",
    "enabled": true,
    "password": "string",
    "username": "string"
  },
  "allow_ipv6_ndp": true,
  "allow_mdns": false,
  "ap_ids": [
    "097f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "app_limit": {
    "apps": {},
    "enabled": true,
    "wxtag_ids": {}
  },
  "app_qos": {
    "apps": {
      "skype-business-video": {
        "dscp": 0,
        "dst_subnet": "string",
        "src_subnet": "string"
      },
      "skype-business-voice": {
        "dscp": 0
      }
    },
    "enabled": true,
    "others": [
      {
        "dscp": 0,
        "dst_subnet": "string",
        "port_ranges": "string",
        "protocol": "string",
        "src_subnet": "string"
      }
    ]
  },
  "apply_to": "site",
  "arp_filter": false,
  "auth": {
    "eap_reauth": false,
    "enable_mac_auth": false,
    "key_idx": 1,
    "keys": [
      "string"
    ],
    "multi_psk_only": false,
    "owe": "string",
    "pairwise": [
      "wpa2-ccmp"
    ],
    "private_wlan": true,
    "psk": "stringst",
    "type": "open",
    "wep_as_secondary_auth": true
  },
  "auth_server_selection": "ordered",
  "auth_servers": [
    {
      "host": "string",
      "port": 1812,
      "secret": "string"
    }
  ],
  "auth_servers_nas_id": "string",
  "auth_servers_nas_ip": "string",
  "auth_servers_retries": 3,
  "auth_servers_timeout": 5,
  "band": "string",
  "band_steer": false,
  "band_steer_force_band5": false,
  "block_blacklist_clients": true,
  "bonjour": {
    "additional_vlan_ids": [
      0
    ],
    "enabled": false,
    "services": {
      "property1": {
        "disable_local": false,
        "radius_groups": [
          "string"
        ],
        "scope": "string"
      },
      "property2": {
        "disable_local": false,
        "radius_groups": [
          "string"
        ],
        "scope": "string"
      }
    }
  },
  "cisco_cwa": {
    "allowed_hostnames": [
      "string"
    ],
    "allowed_subnets": [
      "string"
    ],
    "enabled": true
  },
  "client_limit_down": 0,
  "client_limit_down_enabled": false,
  "client_limit_up": 0,
  "client_limit_up_enabled": false,
  "coa_servers": [
    {
      "disable_event_timestamp_check": true,
      "enabled": true,
      "ip": "192.168.0.1",
      "port": "string",
      "secret": "string"
    }
  ],
  "created_time": 0,
  "disable_11ax": false,
  "disable_ht_vht_rates": false,
  "disable_uapsd": false,
  "disable_wmm": false,
  "dns_server_rewrite": {
    "enabled": true,
    "radius_groups": {}
  },
  "dtim": 2,
  "dynamic_psk": {
    "default_psk": "stringst",
    "default_vlan_id": 0,
    "enabled": true,
    "source": "radius",
    "vlan_ids": [
      1
    ]
  },
  "dynamic_vlan": {
    "default_vlan_id": 999,
    "enabled": false,
    "local_vlan_ids": [
      1
    ],
    "type": "standard",
    "vlans": {
      "property1": "string",
      "property2": "string"
    }
  },
  "enable_wireless_bridging": true,
  "enabled": true,
  "for_site": true,
  "hide_ssid": false,
  "hostname_ie": false,
  "hotspot20": {
    "enabled": true,
    "operators": [
      "string"
    ],
    "venue_name": "string"
  },
  "id": "197f6eca-6276-4993-bfeb-53cbbbba6f08",
  "interface": "all",
  "isolation": false,
  "legacy_overds": true,
  "limit_bcast": false,
  "limit_probe_response": true,
  "max_idletime": 1800,
  "modified_time": 0,
  "msp_id": "c0cf23fc-d82f-4219-988c-82fb61d8c875",
  "mxtunnel": {},
  "mxtunnel_id": "6741baab-cbd6-45bd-9e5b-93e8eede3c80",
  "mxtunnel_name": [
    "default"
  ],
  "no_static_dns": false,
  "no_static_ip": false,
  "org_id": "a40f5d1f-d889-42e9-94ea-b9b33585fc6b",
  "portal": {
    "amazon_client_id": "string",
    "amazon_client_secret": "string",
    "amazon_email_domains": [
      "string"
    ],
    "amazon_enabled": true,
    "auth": "none",
    "azure_client_id": "string",
    "azure_client_secret": "string",
    "azure_enabled": true,
    "azure_tenant_id": "string",
    "broadnet_password": "string",
    "broadnet_sid": "string",
    "broadnet_user_id": "string",
    "bypass_when_cloud_down": false,
    "clickatell_api_key": "string",
    "email_enabled": true,
    "enabled": false,
    "expire": 1440,
    "external_portal_url": "string",
    "facebook_client_id": "string",
    "facebook_client_secret": "string",
    "facebook_email_domains": [
      "string"
    ],
    "facebook_enabled": true,
    "forward": false,
    "forward_url": "string",
    "google_client_id": "string",
    "google_client_secret": "string",
    "google_email_domains": [
      "string"
    ],
    "google_enabled": true,
    "gupshup_password": "string",
    "gupshup_userid": "string",
    "microsoft_client_id": "string",
    "microsoft_client_secret": "string",
    "microsoft_email_domains": [
      "string"
    ],
    "microsoft_enabled": true,
    "passphrase_enabled": true,
    "password": "string",
    "portal_allowed_hostnames": "string",
    "portal_allowed_subnets": "string",
    "portal_api_secret": "string",
    "portal_denied_hostnames": "string",
    "portal_image": "string",
    "portal_sso_url": "string",
    "predefined_sponsors_enabled": true,
    "privacy": true,
    "puzzel_password": "string",
    "puzzel_service_id": "string",
    "puzzel_username": "string",
    "smsMessageFormat": "string",
    "sms_enabled": true,
    "sms_provider": "manual",
    "sponsor_email_domains": [
      "string"
    ],
    "sponsor_enabled": true,
    "sponsor_link_validity_duration": "string",
    "sponsor_notify_all": false,
    "sponsors": {
      "property1": "string",
      "property2": "string"
    },
    "sso_default_role": "string",
    "sso_forced_role": "string",
    "sso_idp_cert": "string",
    "sso_idp_sign_algo": "string",
    "sso_idp_sso_url": "string",
    "sso_issuer": "string",
    "sso_nameid_format": "email",
    "thumbnail": "string",
    "twilio_auth_token": "string",
    "twilio_phone_number": "string",
    "twilio_sid": "string"
  },
  "portal_allowed_hostnames": [
    "string"
  ],
  "portal_allowed_subnets": [
    "string"
  ],
  "portal_api_secret": "string",
  "portal_denied_hostnames": [
    "string"
  ],
  "portal_image": "http://example.com",
  "portal_sso_url": "string",
  "portal_template_url": "string",
  "qos": {
    "class": "best_effort",
    "overwrite": false
  },
  "radsec": {
    "enabled": true,
    "idle_timeout": 0,
    "server_name": "string",
    "servers": [
      {
        "host": "string",
        "port": 0
      }
    ],
    "use_mxedge": true
  },
  "rateset": {
    "24": {
      "ht": "string",
      "legacy": [
        "string"
      ],
      "min_rssi": 0,
      "template": "string",
      "vht": "string"
    },
    "5": {
      "ht": "string",
      "legacy": [
        "string"
      ],
      "min_rssi": 0,
      "template": "string",
      "vht": "string"
    }
  },
  "roam_mode": "none",
  "schedule": {
    "enabled": false,
    "hours": {}
  },
  "site_id": "72771e6a-6f5e-4de4-a5b9-1266c4197811",
  "sle_excluded": false,
  "ssid": "string",
  "template_id": "c6d67e98-83ea-49f0-8812-e4abae2b68bc",
  "thumbnail": "http://example.com",
  "use_eapol_v1": false,
  "vlan_enabled": false,
  "vlan_id": 1,
  "vlan_ids": [
    1
  ],
  "vlan_pooling": false,
  "wlan_limit_down": 0,
  "wlan_limit_down_enabled": false,
  "wlan_limit_up": 0,
  "wlan_limit_up_enabled": false,
  "wxtag_ids": [
    "297f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "wxtunnel_id": "string",
  "wxtunnel_remote_id": "string"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWlans401ErrorException`](../../doc/models/api-v1-sites-wlans-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWlans403ErrorException`](../../doc/models/api-v1-sites-wlans-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWlans404ErrorException`](../../doc/models/api-v1-sites-wlans-404-error-exception.md) |


# Update Site Wlan

Update Site WLAN

```python
def update_site_wlan(self,
                    site_id,
                    wlan_id,
                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `wlan_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Wlan`](../../doc/models/wlan.md) | Body, Optional | Request Body |

## Response Type

[`Wlan`](../../doc/models/wlan.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

wlan_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Wlan(
    ssid='string',
    acct_interim_interval=0,
    acct_servers=[
        AcctServer(
            host='string',
            port=0,
            secret='string'
        )
    ],
    airwatch=WlanAirwatch(
        api_key='string',
        console_url='string',
        enabled=True,
        password='string',
        username='string'
    ),
    allow_ipv_6_ndp=True,
    allow_mdns=True,
    ap_ids=[
        'b069b358-4c97-5319-1f8c-7c5ca64d6ab1'
    ],
    app_limit=AppLimit(
        apps={},
        enabled=True,
        wxtag_ids={}
    ),
    app_qos=WlanAppQos(
        apps=Apps(
            skype_business_video=SkypeBusinessVideo(
                dscp=0,
                dst_subnet='string',
                src_subnet='string'
            ),
            skype_business_voice=SkypeBusinessVoice(
                dscp=0
            )
        ),
        enabled=True,
        others=[
            Other(
                dscp=0,
                dst_subnet='string',
                port_ranges='string',
                protocol='string',
                src_subnet='string'
            )
        ]
    ),
    apply_to=ApplyToEnum.SITE,
    arp_filter=True,
    auth=WlanAuth(
        mtype=Type38Enum.OPEN,
        eap_reauth=True,
        enable_mac_auth=True,
        key_idx=1,
        keys=[
            'string'
        ],
        multi_psk_only=True,
        owe='string',
        pairwise=[
            'string'
        ],
        private_wlan=True,
        psk='string123',
        wep_as_secondary_auth=True
    ),
    auth_server_selection=AuthServerSelectionEnum.ORDERED,
    auth_servers=[
        AuthServer(
            host='string',
            port=0,
            secret='string'
        )
    ],
    auth_servers_nas_id='string',
    auth_servers_nas_ip='string',
    auth_servers_retries=0,
    auth_servers_timeout=0,
    band='string',
    band_steer=True,
    band_steer_force_band_5=True,
    block_blacklist_clients=True,
    bonjour=WlanBonjour(
        additional_vlan_ids=[
            0
        ],
        services={
            "service_name2": Services(
                disable_local=True,
                radius_groups=[
                    'string'
                ],
                scope='string'
            )
        },
        enabled=True
    ),
    cisco_cwa=WlanCiscoCwa(
        allowed_hostnames=[
            'string'
        ],
        allowed_subnets=[
            'string'
        ],
        enabled=True
    ),
    client_limit_down=0,
    client_limit_down_enabled=True,
    client_limit_up=0,
    client_limit_up_enabled=True,
    coa_servers=[
        CoaServer(
            disable_event_timestamp_check=True,
            enabled=True,
            ip='192.168.1.1',
            port='3799',
            secret='string'
        )
    ],
    disable_11_ax=True,
    disable_uapsd=True,
    disable_wmm=True,
    dns_server_rewrite=DnsServerRewrite(
        enabled=True,
        radius_groups={}
    ),
    dtim=0,
    dynamic_psk=DynamicPsk(
        enabled=True
    ),
    dynamic_vlan=DynamicVlan1(
        default_vlan_id=1,
        enabled=True,
        local_vlan_ids=[
            1
        ],
        mtype=Type39Enum.STANDARD,
        vlans={}
    ),
    enable_wireless_bridging=True,
    enabled=True,
    hide_ssid=True,
    hostname_ie=True,
    hotspot_20=WlanHotspot20(
        enabled=True,
        operators=[
            'string'
        ],
        venue_name='string'
    ),
    interface=InterfaceEnum.ALL,
    isolation=True,
    legacy_overds=True,
    limit_bcast=True,
    limit_probe_response=True,
    max_idletime=60,
    no_static_dns=True,
    no_static_ip=True,
    portal=WlanPortal(
        amazon_client_id='string',
        amazon_client_secret='string',
        amazon_email_domains=[
            'string'
        ],
        amazon_enabled=True,
        auth=Auth2Enum.NONE,
        azure_client_id='string',
        azure_client_secret='string',
        azure_enabled=True,
        azure_tenant_id='string',
        bypass_when_cloud_down=True,
        email_enabled=True,
        enabled=True,
        expire=0,
        external_portal_url='string',
        facebook_client_id='string',
        facebook_client_secret='string',
        facebook_email_domains=[
            'string'
        ],
        facebook_enabled=True,
        forward=True,
        forward_url='string',
        google_email_domains=[
            'string'
        ],
        google_enabled=True,
        microsoft_client_id='string',
        microsoft_client_secret='string',
        microsoft_email_domains=[
            'string'
        ],
        microsoft_enabled=True,
        passphrase_enabled=True,
        password='string',
        portal_allowed_hostnames='string',
        portal_allowed_subnets='string',
        portal_api_secret='string',
        portal_denied_hostnames='string',
        portal_image='string',
        portal_sso_url='string',
        privacy=True,
        sms_enabled=True,
        sms_provider=SmsProviderEnum.MANUAL,
        sponsor_email_domains=[
            'string'
        ],
        sponsor_enabled=True,
        sponsor_link_validity_duration='60',
        sso_default_role='string',
        sso_idp_cert='string',
        sso_idp_sign_algo='string',
        sso_idp_sso_url='string',
        sso_issuer='string',
        thumbnail='string',
        twilio_auth_token='string',
        twilio_phone_number='string',
        twilio_sid='string'
    ),
    portal_allowed_hostnames=[
        'string'
    ],
    portal_allowed_subnets=[
        'string'
    ],
    portal_api_secret='string',
    portal_denied_hostnames=[
        'string'
    ],
    portal_image='http://example.com',
    portal_sso_url='string',
    portal_template_url='string',
    qos=Qos(
        mclass=ClassEnum.BEST_EFFORT,
        overwrite=True
    ),
    radsec=Radsec(
        enabled=True,
        server_name='string',
        servers=[
            Server(
                host='string',
                port=0
            )
        ]
    ),
    rateset={
        "24": WlanDatarates(
            ht='string',
            legacy=[
                'string'
            ],
            min_rssi=0,
            template='string',
            vht='string'
        ),
        "5": WlanDatarates(
            ht='string',
            legacy=[
                'string'
            ],
            min_rssi=0,
            template='string',
            vht='string'
        )
    },
    roam_mode=RoamModeEnum.ENUM_11R,
    schedule=Schedule(
        enabled=True,
        hours={}
    ),
    sle_excluded=True,
    thumbnail='http://example.com',
    use_eapol_v_1=True,
    vlan_enabled=True,
    vlan_id=1,
    vlan_ids=[
        1
    ],
    vlan_pooling=True,
    wlan_limit_down=0,
    wlan_limit_down_enabled=True,
    wlan_limit_up=0,
    wlan_limit_up_enabled=True,
    wxtag_ids=[
        'b069b358-4c97-5319-1f8c-7c5ca64d6ab1'
    ],
    wxtunnel_id='6f4bf402-45f9-2a56-6c8b-7f83d3bc98e9',
    wxtunnel_remote_id='string'
)

result = sites_wlans_controller.update_site_wlan(
    site_id,
    wlan_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "acct_interim_interval": 0,
  "acct_servers": [
    {
      "host": "string",
      "port": 1813,
      "secret": "string"
    }
  ],
  "airwatch": {
    "api_key": "string",
    "console_url": "string",
    "enabled": true,
    "password": "string",
    "username": "string"
  },
  "allow_ipv6_ndp": true,
  "allow_mdns": false,
  "ap_ids": [
    "097f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "app_limit": {
    "apps": {},
    "enabled": true,
    "wxtag_ids": {}
  },
  "app_qos": {
    "apps": {
      "skype-business-video": {
        "dscp": 0,
        "dst_subnet": "string",
        "src_subnet": "string"
      },
      "skype-business-voice": {
        "dscp": 0
      }
    },
    "enabled": true,
    "others": [
      {
        "dscp": 0,
        "dst_subnet": "string",
        "port_ranges": "string",
        "protocol": "string",
        "src_subnet": "string"
      }
    ]
  },
  "apply_to": "site",
  "arp_filter": false,
  "auth": {
    "eap_reauth": false,
    "enable_mac_auth": false,
    "key_idx": 1,
    "keys": [
      "string"
    ],
    "multi_psk_only": false,
    "owe": "string",
    "pairwise": [
      "wpa2-ccmp"
    ],
    "private_wlan": true,
    "psk": "stringst",
    "type": "open",
    "wep_as_secondary_auth": true
  },
  "auth_server_selection": "ordered",
  "auth_servers": [
    {
      "host": "string",
      "port": 1812,
      "secret": "string"
    }
  ],
  "auth_servers_nas_id": "string",
  "auth_servers_nas_ip": "string",
  "auth_servers_retries": 3,
  "auth_servers_timeout": 5,
  "band": "string",
  "band_steer": false,
  "band_steer_force_band5": false,
  "block_blacklist_clients": true,
  "bonjour": {
    "additional_vlan_ids": [
      0
    ],
    "enabled": false,
    "services": {
      "property1": {
        "disable_local": false,
        "radius_groups": [
          "string"
        ],
        "scope": "string"
      },
      "property2": {
        "disable_local": false,
        "radius_groups": [
          "string"
        ],
        "scope": "string"
      }
    }
  },
  "cisco_cwa": {
    "allowed_hostnames": [
      "string"
    ],
    "allowed_subnets": [
      "string"
    ],
    "enabled": true
  },
  "client_limit_down": 0,
  "client_limit_down_enabled": false,
  "client_limit_up": 0,
  "client_limit_up_enabled": false,
  "coa_servers": [
    {
      "disable_event_timestamp_check": true,
      "enabled": true,
      "ip": "192.168.0.1",
      "port": "string",
      "secret": "string"
    }
  ],
  "created_time": 0,
  "disable_11ax": false,
  "disable_ht_vht_rates": false,
  "disable_uapsd": false,
  "disable_wmm": false,
  "dns_server_rewrite": {
    "enabled": true,
    "radius_groups": {}
  },
  "dtim": 2,
  "dynamic_psk": {
    "default_psk": "stringst",
    "default_vlan_id": 0,
    "enabled": true,
    "source": "radius",
    "vlan_ids": [
      1
    ]
  },
  "dynamic_vlan": {
    "default_vlan_id": 999,
    "enabled": false,
    "local_vlan_ids": [
      1
    ],
    "type": "standard",
    "vlans": {
      "property1": "string",
      "property2": "string"
    }
  },
  "enable_wireless_bridging": true,
  "enabled": true,
  "for_site": true,
  "hide_ssid": false,
  "hostname_ie": false,
  "hotspot20": {
    "enabled": true,
    "operators": [
      "string"
    ],
    "venue_name": "string"
  },
  "id": "197f6eca-6276-4993-bfeb-53cbbbba6f08",
  "interface": "all",
  "isolation": false,
  "legacy_overds": true,
  "limit_bcast": false,
  "limit_probe_response": true,
  "max_idletime": 1800,
  "modified_time": 0,
  "msp_id": "c0cf23fc-d82f-4219-988c-82fb61d8c875",
  "mxtunnel": {},
  "mxtunnel_id": "6741baab-cbd6-45bd-9e5b-93e8eede3c80",
  "mxtunnel_name": [
    "default"
  ],
  "no_static_dns": false,
  "no_static_ip": false,
  "org_id": "a40f5d1f-d889-42e9-94ea-b9b33585fc6b",
  "portal": {
    "amazon_client_id": "string",
    "amazon_client_secret": "string",
    "amazon_email_domains": [
      "string"
    ],
    "amazon_enabled": true,
    "auth": "none",
    "azure_client_id": "string",
    "azure_client_secret": "string",
    "azure_enabled": true,
    "azure_tenant_id": "string",
    "broadnet_password": "string",
    "broadnet_sid": "string",
    "broadnet_user_id": "string",
    "bypass_when_cloud_down": false,
    "clickatell_api_key": "string",
    "email_enabled": true,
    "enabled": false,
    "expire": 1440,
    "external_portal_url": "string",
    "facebook_client_id": "string",
    "facebook_client_secret": "string",
    "facebook_email_domains": [
      "string"
    ],
    "facebook_enabled": true,
    "forward": false,
    "forward_url": "string",
    "google_client_id": "string",
    "google_client_secret": "string",
    "google_email_domains": [
      "string"
    ],
    "google_enabled": true,
    "gupshup_password": "string",
    "gupshup_userid": "string",
    "microsoft_client_id": "string",
    "microsoft_client_secret": "string",
    "microsoft_email_domains": [
      "string"
    ],
    "microsoft_enabled": true,
    "passphrase_enabled": true,
    "password": "string",
    "portal_allowed_hostnames": "string",
    "portal_allowed_subnets": "string",
    "portal_api_secret": "string",
    "portal_denied_hostnames": "string",
    "portal_image": "string",
    "portal_sso_url": "string",
    "predefined_sponsors_enabled": true,
    "privacy": true,
    "puzzel_password": "string",
    "puzzel_service_id": "string",
    "puzzel_username": "string",
    "smsMessageFormat": "string",
    "sms_enabled": true,
    "sms_provider": "manual",
    "sponsor_email_domains": [
      "string"
    ],
    "sponsor_enabled": true,
    "sponsor_link_validity_duration": "string",
    "sponsor_notify_all": false,
    "sponsors": {
      "property1": "string",
      "property2": "string"
    },
    "sso_default_role": "string",
    "sso_forced_role": "string",
    "sso_idp_cert": "string",
    "sso_idp_sign_algo": "string",
    "sso_idp_sso_url": "string",
    "sso_issuer": "string",
    "sso_nameid_format": "email",
    "thumbnail": "string",
    "twilio_auth_token": "string",
    "twilio_phone_number": "string",
    "twilio_sid": "string"
  },
  "portal_allowed_hostnames": [
    "string"
  ],
  "portal_allowed_subnets": [
    "string"
  ],
  "portal_api_secret": "string",
  "portal_denied_hostnames": [
    "string"
  ],
  "portal_image": "http://example.com",
  "portal_sso_url": "string",
  "portal_template_url": "string",
  "qos": {
    "class": "best_effort",
    "overwrite": false
  },
  "radsec": {
    "enabled": true,
    "idle_timeout": 0,
    "server_name": "string",
    "servers": [
      {
        "host": "string",
        "port": 0
      }
    ],
    "use_mxedge": true
  },
  "rateset": {
    "24": {
      "ht": "string",
      "legacy": [
        "string"
      ],
      "min_rssi": 0,
      "template": "string",
      "vht": "string"
    },
    "5": {
      "ht": "string",
      "legacy": [
        "string"
      ],
      "min_rssi": 0,
      "template": "string",
      "vht": "string"
    }
  },
  "roam_mode": "none",
  "schedule": {
    "enabled": false,
    "hours": {}
  },
  "site_id": "72771e6a-6f5e-4de4-a5b9-1266c4197811",
  "sle_excluded": false,
  "ssid": "string",
  "template_id": "c6d67e98-83ea-49f0-8812-e4abae2b68bc",
  "thumbnail": "http://example.com",
  "use_eapol_v1": false,
  "vlan_enabled": false,
  "vlan_id": 1,
  "vlan_ids": [
    1
  ],
  "vlan_pooling": false,
  "wlan_limit_down": 0,
  "wlan_limit_down_enabled": false,
  "wlan_limit_up": 0,
  "wlan_limit_up_enabled": false,
  "wxtag_ids": [
    "297f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "wxtunnel_id": "string",
  "wxtunnel_remote_id": "string"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWlans401ErrorException`](../../doc/models/api-v1-sites-wlans-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWlans403ErrorException`](../../doc/models/api-v1-sites-wlans-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWlans404ErrorException`](../../doc/models/api-v1-sites-wlans-404-error-exception.md) |


# Upload Site Wlan Portal Image

Wlan Portal Image Upload

```python
def upload_site_wlan_portal_image(self,
                                 site_id,
                                 wlan_id,
                                 file=None,
                                 json=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `wlan_id` | `uuid\|string` | Template, Required | - |
| `file` | `string` | Form, Optional | binary file |
| `json` | `string` | Form, Optional | JSON string describing your upload |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

wlan_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_wlans_controller.upload_site_wlan_portal_image(
    site_id,
    wlan_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWlansPortalImage401ErrorException`](../../doc/models/api-v1-sites-wlans-portal-image-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWlansPortalImage403ErrorException`](../../doc/models/api-v1-sites-wlans-portal-image-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWlansPortalImage404ErrorException`](../../doc/models/api-v1-sites-wlans-portal-image-404-error-exception.md) |


# Update Site Wlan Portal Template

Update a Portal Template

#### Sponsor Email Template

Sponsor Email Template supports following template variables:

| **Name** | **Description** |
| --- | --- |
| approve_url | Renders URL to approve the request; optionally &minutes=N query param can be appended to change the Authorization period of the guest, where N is a valid integer denoting number of minutes a guest remains authorized |
| deny_url | Renders URL to reject the request |
| guest_email | Renders Email ID of the guest |
| guest_name | Renders Name of the guest |
| field1 | Renders value of the Custom Field 1 |
| field2 | Renders value of the Custom Field 2 |
| company | Renders value of the Company field |
| sponsor_link_validity_duration | Renders validity time of the request (i.e. Approve/Deny URL) |
| auth_expire_minutes | Renders Wlan-level configured Guest Authorization Expiration time period (in minutes), If not configured then default (1 day in minutes) |

```python
def update_site_wlan_portal_template(self,
                                    site_id,
                                    wlan_id,
                                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `wlan_id` | `uuid\|string` | Template, Required | - |
| `body` | [`WlanPortalTemplate`](../../doc/models/wlan-portal-template.md) | Body, Optional | Request Body |

## Response Type

[`PortalTemplate`](../../doc/models/portal-template.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

wlan_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = WlanPortalTemplate(
    page_title='string',
    access_code_alternate_email='string',
    alignment='string',
    auth_button_amazon='string',
    auth_button_azure='string',
    auth_button_email='string',
    auth_button_facebook='string',
    auth_button_google='string',
    auth_button_microsoft='string',
    auth_button_passphrase='string',
    auth_button_sms='string',
    auth_button_sponsor='string',
    auth_label='string',
    back_link='string',
    color='string',
    color_dark='string',
    color_light='string',
    company=True,
    company_error='string',
    company_label='string',
    email=True,
    email_access_domain_error='string',
    email_cancel='string',
    email_code_error='string',
    email_error='string',
    email_field_label='string',
    email_label='string',
    email_message='string',
    email_submit='string',
    email_title='string',
    field_1=True,
    field_1_error='string',
    field_1_label='string',
    field_1_required=True,
    field_2=True,
    field_2_error='string',
    field_2_label='string',
    field_2_required=True,
    field_3=True,
    field_3_error='string',
    field_3_label='string',
    field_3_required=True,
    field_4=True,
    field_4_error='string',
    field_4_label='string',
    field_4_required=True,
    message='string',
    name=True,
    name_error='string',
    name_label='string',
    optout=True,
    optout_label='string',
    passphrase_cancel='string',
    passphrase_error='string',
    passphrase_label='string',
    passphrase_message='string',
    passphrase_submit='string',
    passphrase_title='string',
    powered_by=True,
    required_field_label='string',
    sign_in_label='string',
    sms_carrier_default='string',
    sms_carrier_error='string',
    sms_carrier_field_label='string',
    sms_code_cancel='string',
    sms_code_error='string',
    sms_code_field_label='string',
    sms_code_message='string',
    sms_code_submit='string',
    sms_code_title='string',
    sms_country_field_label='string',
    sms_country_format='string',
    sms_have_access_code='string',
    sms_message_format='string',
    sms_number_cancel='string',
    sms_number_error='string',
    sms_number_field_label='string',
    sms_number_format='string',
    sms_number_message='string',
    sms_number_submit='string',
    sms_number_title='string',
    sms_username_format='string',
    sms_validity_duration=0,
    sponsor_back_link='string',
    sponsor_cancel='string',
    sponsor_email='string',
    sponsor_email_error='string',
    sponsor_email_template='string',
    sponsor_info_approved='string',
    sponsor_info_denied='string',
    sponsor_info_pending='string',
    sponsor_name='string',
    sponsor_name_error='string',
    sponsor_note_pending='string',
    sponsor_status_approved='string',
    sponsor_status_denied='string',
    sponsor_status_pending='string',
    sponsor_submit='string',
    tos=True,
    tos_accept_label='string',
    tos_error='string',
    tos_link='string',
    tos_text='string'
)

result = sites_wlans_controller.update_site_wlan_portal_template(
    site_id,
    wlan_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "accessCodeAlternateEmail": "string",
  "alignment": "string",
  "authButtonAmazon": "string",
  "authButtonAzure": "string",
  "authButtonEmail": "string",
  "authButtonFacebook": "string",
  "authButtonGoogle": "string",
  "authButtonMicrosoft": "string",
  "authButtonPassphrase": "string",
  "authButtonSms": "string",
  "authButtonSponsor": "string",
  "authLabel": "string",
  "backLink": "string",
  "color": "string",
  "colorDark": "string",
  "colorLight": "string",
  "company": true,
  "companyError": "string",
  "companyLabel": "string",
  "created_time": 0,
  "email": true,
  "emailAccessDomainError": "string",
  "emailCancel": "string",
  "emailCodeError": "string",
  "emailError": "string",
  "emailFieldLabel": "string",
  "emailLabel": "string",
  "emailMessage": "string",
  "emailSubmit": "string",
  "emailTitle": "string",
  "field1": true,
  "field1Error": "string",
  "field1Label": "string",
  "field1Required": true,
  "field2": true,
  "field2Error": "string",
  "field2Label": "string",
  "field2Required": true,
  "field3": true,
  "field3Error": "string",
  "field3Label": "string",
  "field3Required": true,
  "field4": true,
  "field4Error": "string",
  "field4Label": "string",
  "field4Required": true,
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "message": "string",
  "modified_time": 0,
  "name": true,
  "nameError": "string",
  "nameLabel": "string",
  "optout": true,
  "optoutLabel": "string",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "pageTitle": "string",
  "passphraseCancel": "string",
  "passphraseError": "string",
  "passphraseLabel": "string",
  "passphraseMessage": "string",
  "passphraseSubmit": "string",
  "passphraseTitle": "string",
  "poweredBy": true,
  "requiredFieldLabel": "string",
  "signInLabel": "string",
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "smsCarrierDefault": "string",
  "smsCarrierError": "string",
  "smsCarrierFieldLabel": "string",
  "smsCodeCancel": "string",
  "smsCodeError": "string",
  "smsCodeFieldLabel": "string",
  "smsCodeMessage": "string",
  "smsCodeSubmit": "string",
  "smsCodeTitle": "string",
  "smsCountryFieldLabel": "string",
  "smsCountryFormat": "string",
  "smsHaveAccessCode": "string",
  "smsMessageFormat": "string",
  "smsNumberCancel": "string",
  "smsNumberError": "string",
  "smsNumberFieldLabel": "string",
  "smsNumberFormat": "string",
  "smsNumberMessage": "string",
  "smsNumberSubmit": "string",
  "smsNumberTitle": "string",
  "smsUsernameFormat": "string",
  "smsValidityDuration": 0,
  "sponsorBackLink": "string",
  "sponsorCancel": "string",
  "sponsorEmail": "string",
  "sponsorEmailError": "string",
  "sponsorEmailTemplate": "string",
  "sponsorInfoApproved": "string",
  "sponsorInfoDenied": "string",
  "sponsorInfoPending": "string",
  "sponsorName": "string",
  "sponsorNameError": "string",
  "sponsorNotePending": "string",
  "sponsorStatusApproved": "string",
  "sponsorStatusDenied": "string",
  "sponsorStatusPending": "string",
  "sponsorSubmit": "string",
  "tos": true,
  "tosAcceptLabel": "string",
  "tosError": "string",
  "tosLink": "string",
  "tosText": "string"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWlansPortalTemplate401ErrorException`](../../doc/models/api-v1-sites-wlans-portal-template-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWlansPortalTemplate403ErrorException`](../../doc/models/api-v1-sites-wlans-portal-template-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWlansPortalTemplate404ErrorException`](../../doc/models/api-v1-sites-wlans-portal-template-404-error-exception.md) |


# Test Site Wlan Telstra Setup

Allows validation of Telstra sms gateway credentials.

In case of success, a text message confirming successful setup should be received. In case of error, telstra error message are returned.

```python
def test_site_wlan_telstra_setup(self)
```

## Response Type

`object`

## Example Usage

```python
result = sites_wlans_controller.test_site_wlan_telstra_setup()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1UtilsTestTelstra401ErrorException`](../../doc/models/api-v1-utils-test-telstra-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1UtilsTestTelstra403ErrorException`](../../doc/models/api-v1-utils-test-telstra-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1UtilsTestTelstra404ErrorException`](../../doc/models/api-v1-utils-test-telstra-404-error-exception.md) |


# Test Site Wlan Twilio Setup

Allows validation of twilio setup
In case of success, a text message confirming successful setup should be received. In case of error, twilio error code and message are returned.

```python
def test_site_wlan_twilio_setup(self,
                               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ApiV1UtilsTestTwilioRequest`](../../doc/models/api-v1-utils-test-twilio-request.md) | Body, Optional | Request Body |

## Response Type

`object`

## Example Usage

```python
body = ApiV1UtilsTestTwilioRequest(
    mfrom='+185051234567',
    to='+19999999999',
    twilio_auth_token='2135be04736a1a0a314bce432d61721a',
    twilio_sid='AC5f4366878d193fb4865ab151739999eb'
)

result = sites_wlans_controller.test_site_wlan_twilio_setup(
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1UtilsTestTwilio401ErrorException`](../../doc/models/api-v1-utils-test-twilio-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1UtilsTestTwilio403ErrorException`](../../doc/models/api-v1-utils-test-twilio-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1UtilsTestTwilio404ErrorException`](../../doc/models/api-v1-utils-test-twilio-404-error-exception.md) |

