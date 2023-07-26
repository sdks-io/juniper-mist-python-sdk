# Sites Service Policies

```python
sites_service_policies_controller = client.sites_service_policies
```

## Class Name

`SitesServicePoliciesController`

## Methods

* [List Site Device Profiles Derived](../../doc/controllers/sites-service-policies.md#list-site-device-profiles-derived)
* [List Site Service Policies Derived](../../doc/controllers/sites-service-policies.md#list-site-service-policies-derived)


# List Site Device Profiles Derived

Retrieves the list of Device Profiles available for the Site

```python
def list_site_device_profiles_derived(self,
                                     site_id,
                                     resolve=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `resolve` | `bool` | Query, Optional | whether resolve the site variables<br>**Default**: `False` |

## Response Type

[`List of Deviceprofile`](../../doc/models/deviceprofile.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

resolve = False

result = sites_service_policies_controller.list_site_device_profiles_derived(
    site_id,
    resolve
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "aeroscout": {
      "enabled": false,
      "host": "string",
      "locate_connected": true
    },
    "ble_config": {
      "beacon_enabled": true,
      "beacon_rate": 0,
      "beacon_rate_mode": "default",
      "beam_disabled": [
        0
      ],
      "eddystone_uid_adv_power": -100,
      "eddystone_uid_beams": "string",
      "eddystone_uid_enabled": true,
      "eddystone_uid_freq_msec": 0,
      "eddystone_uid_instance": "string",
      "eddystone_uid_namespace": "string",
      "eddystone_url_adv_power": 0,
      "eddystone_url_beams": "string",
      "eddystone_url_enabled": true,
      "eddystone_url_freq_msec": 0,
      "eddystone_url_url": "string",
      "ibeacon_adv_power": -100,
      "ibeacon_beams": "string",
      "ibeacon_enabled": false,
      "ibeacon_freq_msec": 0,
      "ibeacon_major": 0,
      "ibeacon_minor": 0,
      "ibeacon_uuid": "1f89bc00-d0af-481b-82fe-a6629259a39f",
      "power": 9,
      "power_mode": "string"
    },
    "created_time": 0,
    "disable_eth1": false,
    "disable_eth2": false,
    "disable_eth3": false,
    "disable_module": false,
    "for_site": true,
    "height": 0,
    "id": "471f6eca-6276-4993-bfeb-53cbbbba6f38",
    "iot_config": {
      "A1": {
        "enabled": false,
        "name": "string",
        "output": true,
        "pullup": "internal"
      },
      "A2": {
        "enabled": false,
        "name": "string",
        "output": true,
        "pullup": "internal"
      },
      "A3": {
        "enabled": false,
        "name": "string",
        "output": true,
        "pullup": "internal"
      },
      "A4": {
        "enabled": false,
        "name": "string",
        "output": true,
        "pullup": "internal"
      },
      "DI1": {
        "enabled": false,
        "name": "string",
        "pullup": "internal"
      },
      "DI2": {
        "enabled": false,
        "name": "string",
        "pullup": "internal"
      },
      "DO": {
        "enabled": false,
        "name": "string",
        "output": true,
        "pullup": "internal",
        "value": 0
      }
    },
    "ip_config": {
      "dns": [
        "string"
      ],
      "dns_suffix": [
        "string"
      ],
      "gateway": "192.168.0.1",
      "gateway6": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
      "ip": "192.168.0.1",
      "ip6": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
      "mtu": 0,
      "netmask": "192.168.0.1",
      "netmask6": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
      "type": "static",
      "type6": "static",
      "vlan_id": 1
    },
    "led": {
      "brightness": 0,
      "enabled": true
    },
    "map_id": "09d2b626-2e4e-45ef-a3c4-e6aeb6c83db1",
    "mesh": {
      "enabled": false,
      "group": 0,
      "role": "base"
    },
    "modified_time": 0,
    "name": "string",
    "notes": "string",
    "ntp_servers": [
      "string"
    ],
    "org_id": "a40f5d1f-d889-42e9-94ea-b9b33585fc6b",
    "orientation": 0,
    "orientation_overwrite": true,
    "poe_passthrough": false,
    "port_config": {
      "property1": {
        "disabled": true,
        "dynamic_vlan": {
          "default_vlan_id": 0,
          "enabled": true,
          "type": "string",
          "vlans": {
            "property1": "string",
            "property2": "string"
          }
        },
        "enable_mac_auth": true,
        "forwarding": "all",
        "mx_tunnel_id": "5f5cac07-0805-46ea-aafd-5c5729042729",
        "mxtunnel_name": "string",
        "port_auth": "none",
        "port_vlan_id": 0,
        "radius_config": {
          "acct_interim_interval": 0,
          "acct_servers": [
            {
              "host": "string",
              "port": 1813,
              "secret": "string"
            }
          ],
          "auth_servers": [
            {
              "host": "string",
              "port": 1812,
              "secret": "string"
            }
          ],
          "auth_servers_retries": 3,
          "auth_servers_timeout": 5
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
        "vlan_id": 0,
        "vland_ids": [
          0
        ],
        "wxtunnel_id": "string",
        "wxtunnel_remote_id": "string"
      },
      "property2": {
        "disabled": true,
        "dynamic_vlan": {
          "default_vlan_id": 0,
          "enabled": true,
          "type": "string",
          "vlans": {
            "property1": "string",
            "property2": "string"
          }
        },
        "enable_mac_auth": true,
        "forwarding": "all",
        "mx_tunnel_id": "5f5cac07-0805-46ea-aafd-5c5729042729",
        "mxtunnel_name": "string",
        "port_auth": "none",
        "port_vlan_id": 0,
        "radius_config": {
          "acct_interim_interval": 0,
          "acct_servers": [
            {
              "host": "string",
              "port": 1813,
              "secret": "string"
            }
          ],
          "auth_servers": [
            {
              "host": "string",
              "port": 1812,
              "secret": "string"
            }
          ],
          "auth_servers_retries": 3,
          "auth_servers_timeout": 5
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
        "vlan_id": 0,
        "vland_ids": [
          0
        ],
        "wxtunnel_id": "string",
        "wxtunnel_remote_id": "string"
      }
    },
    "pwr_config": {
      "base": 0
    },
    "radio_config": {
      "ant_gain_24": 0,
      "ant_gain_5": 0,
      "band_24": {
        "allow_rrm_disable": true,
        "ant_gain": 0,
        "antenna_mode": "default",
        "bandwidth": 20,
        "channel": 0,
        "channels": [
          0
        ],
        "disabled": true,
        "power": 0,
        "power_max": 0,
        "power_min": 0,
        "preamble": "short",
        "usage": "24"
      },
      "band_24_usage": "24",
      "band_5": {
        "allow_rrm_disable": true,
        "ant_gain": 0,
        "antenna_mode": "default",
        "bandwidth": 20,
        "channel": 0,
        "channels": [
          0
        ],
        "disabled": true,
        "power": 0,
        "power_max": 0,
        "power_min": 0,
        "preamble": "short",
        "usage": "24"
      },
      "band_5_on_24_radio": {
        "allow_rrm_disable": true,
        "ant_gain": 0,
        "antenna_mode": "default",
        "bandwidth": 20,
        "channel": 0,
        "channels": [
          0
        ],
        "disabled": true,
        "power": 0,
        "power_max": 0,
        "power_min": 0,
        "preamble": "short",
        "usage": "24"
      },
      "scanning_enabled": true
    },
    "site_id": "72771e6a-6f5e-4de4-a5b9-1266c4197811",
    "switch_config": {
      "enabled": false,
      "eth0": {
        "enable_vlan": true,
        "port_vlan_id": 0,
        "vlan_ids": [
          0
        ]
      },
      "eth1": {
        "enable_vlan": true,
        "port_vlan_id": 0,
        "vlan_ids": [
          0
        ]
      },
      "eth2": {
        "enable_vlan": true,
        "port_vlan_id": 0,
        "vlan_ids": [
          0
        ]
      },
      "eth3": {
        "enable_vlan": true,
        "port_vlan_id": 0,
        "vlan_ids": [
          0
        ]
      },
      "module": {
        "enable_vlan": true,
        "port_vlan_id": 0,
        "vlan_ids": [
          0
        ]
      },
      "wds": {
        "enable_vlan": true,
        "port_vlan_id": 0,
        "vlan_ids": [
          0
        ]
      }
    },
    "usb_config": {
      "cacert": "string",
      "channel": 0,
      "enabled": true,
      "host": "string",
      "port": 0,
      "type": "imagotag",
      "verify_cert": true
    },
    "vars": {},
    "x": 0,
    "y": 0
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDeviceprofilesDerived401ErrorException`](../../doc/models/api-v1-sites-deviceprofiles-derived-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDeviceprofilesDerived403ErrorException`](../../doc/models/api-v1-sites-deviceprofiles-derived-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDeviceprofilesDerived404ErrorException`](../../doc/models/api-v1-sites-deviceprofiles-derived-404-error-exception.md) |


# List Site Service Policies Derived

Retrieves the list of Service Policies available for the Site

```python
def list_site_service_policies_derived(self,
                                      site_id,
                                      resolve=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `resolve` | `bool` | Query, Optional | whether resolve the site variables<br>**Default**: `False` |

## Response Type

[`List of ServicePolicy`](../../doc/models/service-policy.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

resolve = False

result = sites_service_policies_controller.list_site_service_policies_derived(
    site_id,
    resolve
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesServicepoliciesDerived401ErrorException`](../../doc/models/api-v1-sites-servicepolicies-derived-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesServicepoliciesDerived403ErrorException`](../../doc/models/api-v1-sites-servicepolicies-derived-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesServicepoliciesDerived404ErrorException`](../../doc/models/api-v1-sites-servicepolicies-derived-404-error-exception.md) |

