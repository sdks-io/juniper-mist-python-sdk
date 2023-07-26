# Sites Setting

```python
sites_setting_controller = client.sites_setting
```

## Class Name

`SitesSettingController`

## Methods

* [Get Site Setting](../../doc/controllers/sites-setting.md#get-site-setting)
* [Update Site Settings](../../doc/controllers/sites-setting.md#update-site-settings)
* [Delete Site Wireless Clients Blocklist](../../doc/controllers/sites-setting.md#delete-site-wireless-clients-blocklist)
* [Create Site Wireless Clients Blocklist](../../doc/controllers/sites-setting.md#create-site-wireless-clients-blocklist)
* [Delete Site Watched Stations](../../doc/controllers/sites-setting.md#delete-site-watched-stations)
* [Create Site Watched Stations](../../doc/controllers/sites-setting.md#create-site-watched-stations)
* [Delete Site Wireless Clients Allowlist](../../doc/controllers/sites-setting.md#delete-site-wireless-clients-allowlist)
* [Create Site Wireless Clients Allowlist](../../doc/controllers/sites-setting.md#create-site-wireless-clients-allowlist)


# Get Site Setting

Get Site Settings

```python
def get_site_setting(self,
                    site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`SiteSetting`](../../doc/models/site-setting.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_setting_controller.get_site_setting(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "additional_config_cmds": [
    "string"
  ],
  "analytic": {
    "enabled": false
  },
  "auto_upgrade": {
    "custom_versions": {
      "property1": "string",
      "property2": "string"
    },
    "day_of_week": "any",
    "enabled": false,
    "time_of_day": "string",
    "version": "stable"
  },
  "bgp_groups": {
    "property1": {
      "type": "external"
    },
    "property2": {
      "type": "external"
    }
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
  "config_auto_revert": false,
  "created_time": 0,
  "device_updown_threshold": 0,
  "dns_servers": [
    "string"
  ],
  "dns_suffix": [
    "string"
  ],
  "enable_channel_144": false,
  "engagement": {
    "dwell_tag_names": {
      "bounce": "string",
      "engaged": "string",
      "passerby": "string",
      "stationed": "string"
    },
    "dwell_tags": {
      "bounce": "string",
      "engaged": "string",
      "passerby": "string",
      "stationed": "string"
    },
    "hours": {
      "fri": "string",
      "mon": "string",
      "sta": "string",
      "sun": "string",
      "thu": "string",
      "tue": "string",
      "wed": "string"
    },
    "max_dwell": 43200,
    "min_dwell": 0
  },
  "evpn_options": {
    "overlay": {
      "as": 0
    },
    "underlay": {
      "as_base": 0,
      "subnet": "string"
    }
  },
  "flags": {
    "property1": "string",
    "property2": "string"
  },
  "for_site": true,
  "gateway_mgmt": {
    "app_usage": true,
    "config_revert_timer": 10
  },
  "id": "458f6ec2-6276-4993-bfeb-53abbbba6f08",
  "led": {
    "brightness": 0,
    "enabled": true
  },
  "modified_time": 0,
  "mxtunnels": {
    "property1": {
      "ap_subnets": [
        "string"
      ],
      "clusters": [
        {
          "name": "string",
          "tunterm_hosts": [
            "string"
          ]
        }
      ],
      "created_time": 0,
      "for_site": true,
      "hello_interval": 60,
      "hello_retries": 7,
      "hosts": [
        "string"
      ],
      "id": "457f6ec3-6276-4993-bfeb-53cbbbba6f08",
      "modified_time": 0,
      "mtu": 0,
      "org_id": "a40f5d1f-d889-42e9-94ea-b9b33585fc6b",
      "protocol": "udp",
      "radsec": {
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
        "enabled": true,
        "use_mxedge": true
      },
      "site_id": "72771e6a-6f5e-4de4-a5b9-1266c4197811",
      "vlan_ids": [
        0
      ]
    },
    "property2": {
      "ap_subnets": [
        "string"
      ],
      "clusters": [
        {
          "name": "string",
          "tunterm_hosts": [
            "string"
          ]
        }
      ],
      "created_time": 0,
      "for_site": true,
      "hello_interval": 60,
      "hello_retries": 7,
      "hosts": [
        "string"
      ],
      "id": "456f6ec4-6276-4993-bfeb-53cbbbba6f08",
      "modified_time": 0,
      "mtu": 0,
      "org_id": "a40f5d1f-d889-42e9-94ea-b9b33585fc6b",
      "protocol": "udp",
      "radsec": {
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
        "enabled": true,
        "use_mxedge": true
      },
      "site_id": "72771e6a-6f5e-4de4-a5b9-1266c4197811",
      "vlan_ids": [
        0
      ]
    }
  },
  "networks": {
    "property1": {
      "dns": [
        "string"
      ],
      "dns_suffix": [
        "string"
      ],
      "gateway": "string",
      "ospf_interface_type": "string",
      "subnet": "string",
      "vlan_id": 0,
      "zone": "string"
    },
    "property2": {
      "dns": [
        "string"
      ],
      "dns_suffix": [
        "string"
      ],
      "gateway": "string",
      "ospf_interface_type": "string",
      "subnet": "string",
      "vlan_id": 0,
      "zone": "string"
    }
  },
  "ntp_servers": [
    "string"
  ],
  "occupancy": {
    "assets_enabled": false,
    "clients_enabled": true,
    "min_duration": 3000,
    "sdkclients_enabled": false,
    "unconnected_clients_enabled": false
  },
  "org_id": "a40f5d1f-d889-42e9-94ea-b9b33585fc6b",
  "ospf_areas": {
    "property1": {
      "networks": {
        "property1": {
          "auth_keys": {
            "property1": "string",
            "property2": "string"
          },
          "auth_password": "string",
          "auth_type": "none",
          "interface_type": "nbma",
          "passive": false
        },
        "property2": {
          "auth_keys": {
            "property1": "string",
            "property2": "string"
          },
          "auth_password": "string",
          "auth_type": "none",
          "interface_type": "nbma",
          "passive": false
        }
      },
      "type": "default"
    },
    "property2": {
      "networks": {
        "property1": {
          "auth_keys": {
            "property1": "string",
            "property2": "string"
          },
          "auth_password": "string",
          "auth_type": "none",
          "interface_type": "nbma",
          "passive": false
        },
        "property2": {
          "auth_keys": {
            "property1": "string",
            "property2": "string"
          },
          "auth_password": "string",
          "auth_type": "none",
          "interface_type": "nbma",
          "passive": false
        }
      },
      "type": "default"
    }
  },
  "persist_config_on_device": false,
  "port_usages": {
    "dynamic": {
      "mode": "dynamic",
      "rules": [
        {
          "equals": "string",
          "expression": "string",
          "src": "lldp_chassis_id",
          "usage": "string"
        }
      ]
    },
    "property1": {
      "all_networks": false,
      "bypass_auth_when_server_down": true,
      "description": "string",
      "disable_autoneg": false,
      "disabled": false,
      "duplex": "auto",
      "dynamic_vlan": {
        "default_network": 0,
        "enabled": true,
        "networks": {
          "property1": 0,
          "property2": 0
        },
        "type": "standard"
      },
      "enable_mac_auth": true,
      "enable_qos": true,
      "guest_network": "string",
      "mac_limit": 0,
      "mode": "access",
      "mtu": 0,
      "networks": [
        "string"
      ],
      "persist_mac": false,
      "poe_disabled": false,
      "port_auth": "string",
      "port_network": "string",
      "speed": "string",
      "storm_control": {
        "no_broadcast": false,
        "no_multicast": false,
        "no_registered_multicast": false,
        "no_unknown_unicast": false,
        "percentage": 80
      },
      "stp_edge": true,
      "voip_network": "string"
    },
    "property2": {
      "all_networks": false,
      "bypass_auth_when_server_down": true,
      "description": "string",
      "disable_autoneg": false,
      "disabled": false,
      "duplex": "auto",
      "dynamic_vlan": {
        "default_network": 0,
        "enabled": true,
        "networks": {
          "property1": 0,
          "property2": 0
        },
        "type": "standard"
      },
      "enable_mac_auth": true,
      "enable_qos": true,
      "guest_network": "string",
      "mac_limit": 0,
      "mode": "access",
      "mtu": 0,
      "networks": [
        "string"
      ],
      "persist_mac": false,
      "poe_disabled": false,
      "port_auth": "string",
      "port_network": "string",
      "speed": "string",
      "storm_control": {
        "no_broadcast": false,
        "no_multicast": false,
        "no_registered_multicast": false,
        "no_unknown_unicast": false,
        "percentage": 80
      },
      "stp_edge": true,
      "voip_network": "string"
    }
  },
  "proxy": {
    "url": "string"
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
  "remote_syslog": {
    "enabled": true,
    "send_to_all_servers": true,
    "servers": [
      {
        "facility": "any",
        "host": "string",
        "port": 0,
        "protocol": "udp",
        "severity": "alert",
        "tag": "string"
      }
    ]
  },
  "report_gatt": false,
  "rogue": {
    "enabled": true,
    "honeypot_enabled": true,
    "min_duration": 10,
    "min_rssi": -80,
    "whitelisted_bssids": [
      "string"
    ],
    "whitelisted_ssids": [
      "string"
    ]
  },
  "rtsa": {
    "app_waking": false,
    "disable_dead_reckoning": true,
    "disable_pressure_sensor": true,
    "enabled": true,
    "track_asset": true
  },
  "site_id": "72771e6a-6f5e-4de4-a5b9-1266c4197811",
  "skyatp": {
    "enabled": true,
    "send_ip_mac_mapping": true
  },
  "ssh_keys": [
    "string"
  ],
  "status_portal": {
    "enabled": true,
    "hostnames": [
      "string"
    ]
  },
  "switch_matching": {
    "enable": true,
    "rules": [
      {
        "additional_config_cmds": [
          "string"
        ],
        "name": "string",
        "port_config": {
          "property1": {
            "ae_disable_lacp": true,
            "ae_idx": 0,
            "aggregated": false,
            "description": "string",
            "esilag": true,
            "usage": "string"
          },
          "property2": {
            "ae_disable_lacp": true,
            "ae_idx": 0,
            "aggregated": false,
            "description": "string",
            "esilag": true,
            "usage": "string"
          }
        },
        "property1": "string",
        "property2": "string"
      }
    ]
  },
  "switch_mgmt": {
    "config_revert_timer": 10,
    "root_password": "string"
  },
  "track_anonymous_devices": false,
  "vars": {
    "property1": "string",
    "property2": "string"
  },
  "vrf_instances": {
    "property1": {
      "extra_routes": {
        "property1": {
          "via": "192.168.0.1"
        },
        "property2": {
          "via": "192.168.0.1"
        }
      },
      "networks": [
        "string"
      ]
    },
    "property2": {
      "extra_routes": {
        "property1": {
          "via": "192.168.0.1"
        },
        "property2": {
          "via": "192.168.0.1"
        }
      },
      "networks": [
        "string"
      ]
    }
  },
  "vrrp_groups": {
    "property1": {
      "auth_key": "string",
      "auth_password": "string",
      "auth_type": "md5",
      "networks": {
        "property1": {
          "ip": "string"
        },
        "property2": {
          "ip": "string"
        }
      }
    },
    "property2": {
      "auth_key": "string",
      "auth_password": "string",
      "auth_type": "md5",
      "networks": {
        "property1": {
          "ip": "string"
        },
        "property2": {
          "ip": "string"
        }
      }
    }
  },
  "wids": {
    "repeated_auth_failures": {
      "duration": 0,
      "threshold": 0
    }
  },
  "wifi": {
    "cisco_enabled": true,
    "disable_11k": false,
    "disable_radios_when_power_constrained": true,
    "enable_arp_spoof_check": false,
    "enable_channel_144": false,
    "enable_shared_radio_scanning": true,
    "enable_vna": false,
    "enabled": true,
    "locate_connected": false,
    "locate_unconnected": false,
    "mesh_allow_dfs": false,
    "mesh_enabled": false,
    "proxy_arp": "default"
  },
  "zone_occupancy_alert": {
    "email_notifiers": [
      "string"
    ],
    "enabled": false,
    "threshold": 5
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSetting401ErrorException`](../../doc/models/api-v1-sites-setting-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSetting403ErrorException`](../../doc/models/api-v1-sites-setting-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSetting404ErrorException`](../../doc/models/api-v1-sites-setting-404-error-exception.md) |


# Update Site Settings

Update Site Settings

```python
def update_site_settings(self,
                        site_id,
                        body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`SiteSetting`](../../doc/models/site-setting.md) | Body, Optional | Request Body |

## Response Type

[`SiteSetting`](../../doc/models/site-setting.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = SiteSetting(
    additional_config_cmds=[
        'string'
    ],
    analytic=Analytic(
        enabled=False
    ),
    ap_matching=ApMatching1(
        enabled=True,
        rules=[
            Rules5(
                match_model='string',
                name='string',
                port_config={
                    "property1": ApPortConfig(
                        disabled=True,
                        dynamic_vlan=DynamicVlan(
                            default_vlan_id=0,
                            enabled=True,
                            mtype='string',
                            vlans={
                                "property1": 'string',
                                "property2": 'string'
                            }
                        ),
                        enable_mac_auth=True,
                        forwarding=ForwardingEnum.ALL,
                        mx_tunnel_id='5f5cac07-0805-46ea-aafd-5c5729042729',
                        mxtunnel_name='string',
                        port_auth=PortAuthEnum.NONE,
                        port_vlan_id=0,
                        radius_config=JunosRadiusConfig(
                            acct_interim_interval=0,
                            acct_servers=[
                                AcctServer(
                                    host='string',
                                    port=1813,
                                    secret='string'
                                )
                            ],
                            auth_servers=[
                                AuthServer(
                                    host='string',
                                    port=1812,
                                    secret='string'
                                )
                            ],
                            auth_servers_retries=3,
                            auth_servers_timeout=5,
                            coa_enabled=False,
                            coa_port=3799,
                            network='string',
                            source_ip='string'
                        ),
                        radsec=Radsec(
                            enabled=True,
                            idle_timeout=0,
                            server_name='string',
                            servers=[
                                Server(
                                    host='string',
                                    port=0
                                )
                            ],
                            use_mxedge=True
                        ),
                        vlan_id=0,
                        vland_ids=[
                            0
                        ],
                        wxtunnel_id='string',
                        wxtunnel_remote_id='string'
                    ),
                    "property2": ApPortConfig(
                        disabled=True,
                        dynamic_vlan=DynamicVlan(
                            default_vlan_id=0,
                            enabled=True,
                            mtype='string',
                            vlans={
                                "property1": 'string',
                                "property2": 'string'
                            }
                        ),
                        enable_mac_auth=True,
                        forwarding=ForwardingEnum.ALL,
                        mx_tunnel_id='5f5cac07-0805-46ea-aafd-5c5729042729',
                        mxtunnel_name='string',
                        port_auth=PortAuthEnum.NONE,
                        port_vlan_id=0,
                        radius_config=JunosRadiusConfig(
                            acct_interim_interval=0,
                            acct_servers=[
                                AcctServer(
                                    host='string',
                                    port=1813,
                                    secret='string'
                                )
                            ],
                            auth_servers=[
                                AuthServer(
                                    host='string',
                                    port=1812,
                                    secret='string'
                                )
                            ],
                            auth_servers_retries=3,
                            auth_servers_timeout=5,
                            coa_enabled=False,
                            coa_port=3799,
                            network='string',
                            source_ip='string'
                        ),
                        radsec=Radsec(
                            enabled=True,
                            idle_timeout=0,
                            server_name='string',
                            servers=[
                                Server(
                                    host='string',
                                    port=0
                                )
                            ],
                            use_mxedge=True
                        ),
                        vlan_id=0,
                        vland_ids=[
                            0
                        ],
                        wxtunnel_id='string',
                        wxtunnel_remote_id='string'
                    )
                }
            )
        ]
    ),
    ap_port_config=ApPortConfig1(
        model_specific={
            "property1": ApPortConfig(),
            "property2": ApPortConfig()
        }
    ),
    auto_upgrade=SiteAutoUpgrade(
        custom_versions={
            "property1": 'string',
            "property2": 'string'
        },
        day_of_week=DayOfWeekEnum.ANY,
        enabled=False,
        time_of_day='string',
        version=Version2Enum.STABLE
    ),
    blacklist_url='string',
    ble_config=ApBle(
        beacon_enabled=True,
        beacon_rate=0,
        beacon_rate_mode=BeaconRateModeEnum.DEFAULT,
        beam_disabled=[
            0
        ],
        eddystone_uid_adv_power=-100,
        eddystone_uid_beams='string',
        eddystone_uid_enabled=True,
        eddystone_uid_freq_msec=0,
        eddystone_uid_instance='string',
        eddystone_uid_namespace='string',
        eddystone_url_adv_power=0,
        eddystone_url_beams='string',
        eddystone_url_enabled=True,
        eddystone_url_freq_msec=0,
        eddystone_url_url='string',
        ibeacon_adv_power=-100,
        ibeacon_beams='string',
        ibeacon_enabled=False,
        ibeacon_freq_msec=0,
        ibeacon_major=0,
        ibeacon_minor=0,
        ibeacon_uuid='1f89bc00-d0af-481b-82fe-a6629259a39f',
        power=9,
        power_mode='string'
    ),
    config_auto_revert=False,
    created_time=0,
    device_updown_threshold=0,
    dns_servers=[
        'string'
    ],
    dns_suffix=[
        'string'
    ],
    enable_channel_144=False,
    engagement=SiteEngagement(
        dwell_tag_names=DwellTagNames(
            bounce='string',
            engaged='string',
            passerby='string',
            stationed='string'
        ),
        dwell_tags=DwellTags(
            bounce='string',
            engaged='string',
            passerby='string',
            stationed='string'
        ),
        hours=Hours(
            fri='string',
            mon='string',
            sta='string',
            sun='string',
            thu='string',
            tue='string',
            wed='string'
        ),
        max_dwell=43200,
        min_dwell=0
    ),
    evpn_options=JunosEvpnOptions(
        overlay=Overlay(
            mas=65000
        ),
        underlay=Underlay(
            as_base=65001,
            routed_id_prefix='/24',
            subnet='10.255.240.0/20'
        )
    ),
    flags={
        "property1": 'string',
        "property2": 'string'
    },
    for_site=True,
    gateway_mgmt=SiteGateway(
        app_probing=AppProbing1(
            apps=[
                'string'
            ],
            custom_apps=[
                CustomApp(
                    app_type='string',
                    hostname=[
                        'string'
                    ],
                    name='string',
                    protocol=Protocol5Enum.HTTP
                )
            ],
            enabled=True
        ),
        app_usage=True,
        config_revert_timer=10,
        security_log_source_address='string',
        security_log_source_interface='string'
    ),
    id='498f6eca-6276-4993-dfeb-53cbbbba6f08',
    led=ApLed(
        brightness=0,
        enabled=True
    ),
    modified_time=0,
    mxedge_mgmt=MxedgeMgmt(
        mist_password='string',
        root_password='string'
    ),
    mxtunnels=SiteMxtunnel(
        ap_subnets=[
            'string'
        ],
        clusters=[
            Cluster(
                name='string',
                tunterm_hosts=[
                    'string'
                ]
            )
        ],
        created_time=0,
        for_site=True,
        hello_interval=60,
        hello_retries=7,
        hosts=[
            'string'
        ],
        id='499f6eca-6276-4993-efeb-53cbbbba6f08',
        modified_time=0,
        mtu=0,
        org_id='a40f5d1f-d889-42e9-94ea-b9b33585fc6b',
        protocol=Protocol3Enum.UDP,
        radsec=Radsec1(
            acct_servers=[
                AcctServer(
                    host='string',
                    port=1813,
                    secret='string'
                )
            ],
            auth_servers=[
                AuthServer(
                    host='string',
                    port=1812,
                    secret='string'
                )
            ],
            enabled=True,
            use_mxedge=True
        ),
        site_id='72771e6a-6f5e-4de4-a5b9-1266c4197811',
        vlan_ids=[
            jsonpickle.decode('0')
        ]
    ),
    networks={
        "property1": JunosNetworks(
            vlan_id=0,
            dns=[
                'string'
            ],
            dns_suffix=[
                'string'
            ],
            gateway='string',
            ospf_interface_type='string',
            subnet='string',
            zone='string'
        ),
        "property2": JunosNetworks(
            vlan_id=0,
            dns=[
                'string'
            ],
            dns_suffix=[
                'string'
            ],
            gateway='string',
            ospf_interface_type='string',
            subnet='string',
            zone='string'
        )
    },
    ntp_servers=[
        'string'
    ],
    occupancy=SiteOccupancyAnalytics(
        assets_enabled=False,
        clients_enabled=True,
        min_duration=3000,
        sdkclients_enabled=False,
        unconnected_clients_enabled=False
    ),
    org_id='a40f5d1f-d889-42e9-94ea-b9b33585fc6b',
    ospf_areas={
        "property1": JunosOspfAreas(
            networks={
                "property1": Networks1(
                    auth_keys={
                        "property1": 'string',
                        "property2": 'string'
                    },
                    auth_password='string',
                    auth_type=AuthTypeEnum.NONE,
                    interface_type=InterfaceTypeEnum.NBMA,
                    passive=False
                ),
                "property2": Networks1(
                    auth_keys={
                        "property1": 'string',
                        "property2": 'string'
                    },
                    auth_password='string',
                    auth_type=AuthTypeEnum.NONE,
                    interface_type=InterfaceTypeEnum.NBMA,
                    passive=False
                )
            },
            mtype=Type25Enum.DEFAULT
        ),
        "property2": JunosOspfAreas(
            networks={
                "property1": Networks1(
                    auth_keys={
                        "property1": 'string',
                        "property2": 'string'
                    },
                    auth_password='string',
                    auth_type=AuthTypeEnum.NONE,
                    interface_type=InterfaceTypeEnum.NBMA,
                    passive=False
                ),
                "property2": Networks1(
                    auth_keys={
                        "property1": 'string',
                        "property2": 'string'
                    },
                    auth_password='string',
                    auth_type=AuthTypeEnum.NONE,
                    interface_type=InterfaceTypeEnum.NBMA,
                    passive=False
                )
            },
            mtype=Type25Enum.DEFAULT
        )
    },
    persist_config_on_device=False,
    port_usages=PortUsages2(
        dynamic=JunosPortUsagesDynamic(
            mode='dynamic',
            reset_default_when=ResetDefaultWhenEnum.LINK_DOWN,
            rules=[
                Rules2(
                    src=SrcEnum.LLDP_CHASSIS_ID,
                    equals='string',
                    expression='string',
                    usage='string'
                )
            ]
        )
    ),
    proxy=Proxy2(
        url='string'
    ),
    radio_config=ApRadio(
        ant_gain_24=0,
        ant_gain_5=0,
        band_24=ApRadioBand(
            allow_rrm_disable=True,
            ant_gain=0,
            antenna_mode=AntennaModeEnum.DEFAULT,
            bandwidth=BandwidthEnum.ENUM_20,
            channel=0,
            channels=[
                0
            ],
            disabled=True,
            power=0,
            power_max=0,
            power_min=0,
            preamble=PreambleEnum.SHORT,
            usage=UsageEnum.ENUM_24
        ),
        band_24_usage=Band24UsageEnum.ENUM_24,
        band_5=ApRadioBand(
            allow_rrm_disable=True,
            ant_gain=0,
            antenna_mode=AntennaModeEnum.DEFAULT,
            bandwidth=BandwidthEnum.ENUM_20,
            channel=0,
            channels=[
                0
            ],
            disabled=True,
            power=0,
            power_max=0,
            power_min=0,
            preamble=PreambleEnum.SHORT,
            usage=UsageEnum.ENUM_24
        ),
        band_5_on_24_radio=ApRadioBand(
            allow_rrm_disable=True,
            ant_gain=0,
            antenna_mode=AntennaModeEnum.DEFAULT,
            bandwidth=BandwidthEnum.ENUM_20,
            channel=0,
            channels=[
                0
            ],
            disabled=True,
            power=0,
            power_max=0,
            power_min=0,
            preamble=PreambleEnum.SHORT,
            usage=UsageEnum.ENUM_24
        ),
        scanning_enabled=True
    ),
    radius_config=JunosRadiusConfig(
        acct_interim_interval=0,
        acct_servers=[
            AcctServer(
                host='string',
                port=1813,
                secret='string'
            )
        ],
        auth_servers=[
            AuthServer(
                host='string',
                port=1812,
                secret='string'
            )
        ],
        auth_servers_retries=3,
        auth_servers_timeout=5,
        coa_enabled=False,
        coa_port=3799,
        network='string',
        source_ip='string'
    ),
    remote_syslog=RemoteSyslog(
        enabled=True,
        send_to_all_servers=True,
        servers=[
            Server1(
                facility=FacilityEnum.AUTHORIZATION,
                host='string',
                port=0,
                protocol=Protocol4Enum.UDP,
                severity=Severity1Enum.ANY,
                tag='string'
            )
        ]
    ),
    report_gatt=False,
    rogue=SiteRogue(
        enabled=True,
        honeypot_enabled=True,
        min_duration=10,
        min_rssi=-80,
        whitelisted_bssids=[
            'string'
        ],
        whitelisted_ssids=[
            'string'
        ]
    ),
    rtsa=Rtsa(
        app_waking=False,
        disable_dead_reckoning=True,
        disable_pressure_sensor=True,
        enabled=True,
        track_asset=True
    ),
    site_id='72771e6a-6f5e-4de4-a5b9-1266c4197811',
    skyatp=Skyatp(
        enabled=True,
        send_ip_mac_mapping=True
    ),
    srx_app=SrxApp(
        enabled=False
    ),
    ssh_keys=[
        'string'
    ],
    status_portal=StatusPortal(
        enabled=True,
        hostnames=[
            'string'
        ]
    ),
    switch_matching=SwitchMatching(
        rules=[
            Rules6(
                name='string',
                port_config={
                    "property1": PortConfig1(
                        usage='string'
                    ),
                    "property2": PortConfig1(
                        usage='string'
                    )
                }
            )
        ]
    ),
    switch_mgmt=SiteSwitch(
        config_revert_timer=10,
        mxedge_proxy_host='string',
        mxedge_proxy_port=2222,
        root_password='string',
        use_mxedge_proxy=True
    ),
    track_anonymous_devices=False,
    tunterm_monitoring=[
        SiteTuntermMonitoring(
            host='string',
            port=0,
            protocol=Protocol2Enum.ARP,
            timeout=300
        )
    ],
    vars={
        "property1": 'string',
        "property2": 'string'
    },
    vna=Vna(
        enabled=False
    ),
    vrf_instances={
        "property1": JunosVrfInstance(
            extra_routes={
                "property1": ExtraRoutes3(
                    via='192.168.0.1'
                ),
                "property2": ExtraRoutes3(
                    via='192.168.0.1'
                )
            },
            networks=[
                'string'
            ]
        ),
        "property2": JunosVrfInstance(
            extra_routes={
                "property1": ExtraRoutes3(
                    via='192.168.0.1'
                ),
                "property2": ExtraRoutes3(
                    via='192.168.0.1'
                )
            },
            networks=[
                'string'
            ]
        )
    },
    vrrp_groups={
        "property1": JunosVrrpGroup(
            auth_key='string',
            auth_password='string',
            auth_type=AuthType1Enum.MD5,
            networks={
                "property1": Networks2(
                    ip='string'
                ),
                "property2": Networks2(
                    ip='string'
                )
            }
        ),
        "property2": JunosVrrpGroup(
            auth_key='string',
            auth_password='string',
            auth_type=AuthType1Enum.MD5,
            networks={
                "property1": Networks2(
                    ip='string'
                ),
                "property2": Networks2(
                    ip='string'
                )
            }
        )
    },
    wan_vna=WanVna(
        enabled=False
    ),
    watched_station_url='string',
    whitelist_url='string',
    wids=SiteWids(
        repeated_auth_failures=RepeatedAuthFailures(
            duration=0,
            threshold=0
        )
    ),
    wifi=SiteWifi(
        cisco_enabled=True,
        disable_11_k=False,
        disable_radios_when_power_constrained=True,
        enable_arp_spoof_check=False,
        enable_channel_144=False,
        enable_shared_radio_scanning=True,
        enable_vna=False,
        enabled=True,
        locate_connected=False,
        locate_unconnected=False,
        mesh_allow_dfs=False,
        mesh_enabled=False,
        proxy_arp=ProxyArpEnum.DEFAULT
    ),
    wired_vna=WiredVna(
        enabled=False
    ),
    zone_occupancy_alert=SiteZoneOccupancyAlert(
        email_notifiers=[
            'string'
        ],
        enabled=False,
        threshold=5
    )
)

result = sites_setting_controller.update_site_settings(
    site_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "additional_config_cmds": [
    "string"
  ],
  "analytic": {
    "enabled": false
  },
  "auto_upgrade": {
    "custom_versions": {
      "property1": "string",
      "property2": "string"
    },
    "day_of_week": "any",
    "enabled": false,
    "time_of_day": "string",
    "version": "stable"
  },
  "bgp_groups": {
    "property1": {
      "type": "external"
    },
    "property2": {
      "type": "external"
    }
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
  "config_auto_revert": false,
  "created_time": 0,
  "device_updown_threshold": 0,
  "dns_servers": [
    "string"
  ],
  "dns_suffix": [
    "string"
  ],
  "enable_channel_144": false,
  "engagement": {
    "dwell_tag_names": {
      "bounce": "string",
      "engaged": "string",
      "passerby": "string",
      "stationed": "string"
    },
    "dwell_tags": {
      "bounce": "string",
      "engaged": "string",
      "passerby": "string",
      "stationed": "string"
    },
    "hours": {
      "fri": "string",
      "mon": "string",
      "sta": "string",
      "sun": "string",
      "thu": "string",
      "tue": "string",
      "wed": "string"
    },
    "max_dwell": 43200,
    "min_dwell": 0
  },
  "evpn_options": {
    "overlay": {
      "as": 0
    },
    "underlay": {
      "as_base": 0,
      "subnet": "string"
    }
  },
  "flags": {
    "property1": "string",
    "property2": "string"
  },
  "for_site": true,
  "gateway_mgmt": {
    "app_usage": true,
    "config_revert_timer": 10
  },
  "id": "458f6ec2-6276-4993-bfeb-53abbbba6f08",
  "led": {
    "brightness": 0,
    "enabled": true
  },
  "modified_time": 0,
  "mxtunnels": {
    "property1": {
      "ap_subnets": [
        "string"
      ],
      "clusters": [
        {
          "name": "string",
          "tunterm_hosts": [
            "string"
          ]
        }
      ],
      "created_time": 0,
      "for_site": true,
      "hello_interval": 60,
      "hello_retries": 7,
      "hosts": [
        "string"
      ],
      "id": "457f6ec3-6276-4993-bfeb-53cbbbba6f08",
      "modified_time": 0,
      "mtu": 0,
      "org_id": "a40f5d1f-d889-42e9-94ea-b9b33585fc6b",
      "protocol": "udp",
      "radsec": {
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
        "enabled": true,
        "use_mxedge": true
      },
      "site_id": "72771e6a-6f5e-4de4-a5b9-1266c4197811",
      "vlan_ids": [
        0
      ]
    },
    "property2": {
      "ap_subnets": [
        "string"
      ],
      "clusters": [
        {
          "name": "string",
          "tunterm_hosts": [
            "string"
          ]
        }
      ],
      "created_time": 0,
      "for_site": true,
      "hello_interval": 60,
      "hello_retries": 7,
      "hosts": [
        "string"
      ],
      "id": "456f6ec4-6276-4993-bfeb-53cbbbba6f08",
      "modified_time": 0,
      "mtu": 0,
      "org_id": "a40f5d1f-d889-42e9-94ea-b9b33585fc6b",
      "protocol": "udp",
      "radsec": {
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
        "enabled": true,
        "use_mxedge": true
      },
      "site_id": "72771e6a-6f5e-4de4-a5b9-1266c4197811",
      "vlan_ids": [
        0
      ]
    }
  },
  "networks": {
    "property1": {
      "dns": [
        "string"
      ],
      "dns_suffix": [
        "string"
      ],
      "gateway": "string",
      "ospf_interface_type": "string",
      "subnet": "string",
      "vlan_id": 0,
      "zone": "string"
    },
    "property2": {
      "dns": [
        "string"
      ],
      "dns_suffix": [
        "string"
      ],
      "gateway": "string",
      "ospf_interface_type": "string",
      "subnet": "string",
      "vlan_id": 0,
      "zone": "string"
    }
  },
  "ntp_servers": [
    "string"
  ],
  "occupancy": {
    "assets_enabled": false,
    "clients_enabled": true,
    "min_duration": 3000,
    "sdkclients_enabled": false,
    "unconnected_clients_enabled": false
  },
  "org_id": "a40f5d1f-d889-42e9-94ea-b9b33585fc6b",
  "ospf_areas": {
    "property1": {
      "networks": {
        "property1": {
          "auth_keys": {
            "property1": "string",
            "property2": "string"
          },
          "auth_password": "string",
          "auth_type": "none",
          "interface_type": "nbma",
          "passive": false
        },
        "property2": {
          "auth_keys": {
            "property1": "string",
            "property2": "string"
          },
          "auth_password": "string",
          "auth_type": "none",
          "interface_type": "nbma",
          "passive": false
        }
      },
      "type": "default"
    },
    "property2": {
      "networks": {
        "property1": {
          "auth_keys": {
            "property1": "string",
            "property2": "string"
          },
          "auth_password": "string",
          "auth_type": "none",
          "interface_type": "nbma",
          "passive": false
        },
        "property2": {
          "auth_keys": {
            "property1": "string",
            "property2": "string"
          },
          "auth_password": "string",
          "auth_type": "none",
          "interface_type": "nbma",
          "passive": false
        }
      },
      "type": "default"
    }
  },
  "persist_config_on_device": false,
  "port_usages": {
    "dynamic": {
      "mode": "dynamic",
      "rules": [
        {
          "equals": "string",
          "expression": "string",
          "src": "lldp_chassis_id",
          "usage": "string"
        }
      ]
    },
    "property1": {
      "all_networks": false,
      "bypass_auth_when_server_down": true,
      "description": "string",
      "disable_autoneg": false,
      "disabled": false,
      "duplex": "auto",
      "dynamic_vlan": {
        "default_network": 0,
        "enabled": true,
        "networks": {
          "property1": 0,
          "property2": 0
        },
        "type": "standard"
      },
      "enable_mac_auth": true,
      "enable_qos": true,
      "guest_network": "string",
      "mac_limit": 0,
      "mode": "access",
      "mtu": 0,
      "networks": [
        "string"
      ],
      "persist_mac": false,
      "poe_disabled": false,
      "port_auth": "string",
      "port_network": "string",
      "speed": "string",
      "storm_control": {
        "no_broadcast": false,
        "no_multicast": false,
        "no_registered_multicast": false,
        "no_unknown_unicast": false,
        "percentage": 80
      },
      "stp_edge": true,
      "voip_network": "string"
    },
    "property2": {
      "all_networks": false,
      "bypass_auth_when_server_down": true,
      "description": "string",
      "disable_autoneg": false,
      "disabled": false,
      "duplex": "auto",
      "dynamic_vlan": {
        "default_network": 0,
        "enabled": true,
        "networks": {
          "property1": 0,
          "property2": 0
        },
        "type": "standard"
      },
      "enable_mac_auth": true,
      "enable_qos": true,
      "guest_network": "string",
      "mac_limit": 0,
      "mode": "access",
      "mtu": 0,
      "networks": [
        "string"
      ],
      "persist_mac": false,
      "poe_disabled": false,
      "port_auth": "string",
      "port_network": "string",
      "speed": "string",
      "storm_control": {
        "no_broadcast": false,
        "no_multicast": false,
        "no_registered_multicast": false,
        "no_unknown_unicast": false,
        "percentage": 80
      },
      "stp_edge": true,
      "voip_network": "string"
    }
  },
  "proxy": {
    "url": "string"
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
  "remote_syslog": {
    "enabled": true,
    "send_to_all_servers": true,
    "servers": [
      {
        "facility": "any",
        "host": "string",
        "port": 0,
        "protocol": "udp",
        "severity": "alert",
        "tag": "string"
      }
    ]
  },
  "report_gatt": false,
  "rogue": {
    "enabled": true,
    "honeypot_enabled": true,
    "min_duration": 10,
    "min_rssi": -80,
    "whitelisted_bssids": [
      "string"
    ],
    "whitelisted_ssids": [
      "string"
    ]
  },
  "rtsa": {
    "app_waking": false,
    "disable_dead_reckoning": true,
    "disable_pressure_sensor": true,
    "enabled": true,
    "track_asset": true
  },
  "site_id": "72771e6a-6f5e-4de4-a5b9-1266c4197811",
  "skyatp": {
    "enabled": true,
    "send_ip_mac_mapping": true
  },
  "ssh_keys": [
    "string"
  ],
  "status_portal": {
    "enabled": true,
    "hostnames": [
      "string"
    ]
  },
  "switch_matching": {
    "enable": true,
    "rules": [
      {
        "additional_config_cmds": [
          "string"
        ],
        "name": "string",
        "port_config": {
          "property1": {
            "ae_disable_lacp": true,
            "ae_idx": 0,
            "aggregated": false,
            "description": "string",
            "esilag": true,
            "usage": "string"
          },
          "property2": {
            "ae_disable_lacp": true,
            "ae_idx": 0,
            "aggregated": false,
            "description": "string",
            "esilag": true,
            "usage": "string"
          }
        },
        "property1": "string",
        "property2": "string"
      }
    ]
  },
  "switch_mgmt": {
    "config_revert_timer": 10,
    "root_password": "string"
  },
  "track_anonymous_devices": false,
  "vars": {
    "property1": "string",
    "property2": "string"
  },
  "vrf_instances": {
    "property1": {
      "extra_routes": {
        "property1": {
          "via": "192.168.0.1"
        },
        "property2": {
          "via": "192.168.0.1"
        }
      },
      "networks": [
        "string"
      ]
    },
    "property2": {
      "extra_routes": {
        "property1": {
          "via": "192.168.0.1"
        },
        "property2": {
          "via": "192.168.0.1"
        }
      },
      "networks": [
        "string"
      ]
    }
  },
  "vrrp_groups": {
    "property1": {
      "auth_key": "string",
      "auth_password": "string",
      "auth_type": "md5",
      "networks": {
        "property1": {
          "ip": "string"
        },
        "property2": {
          "ip": "string"
        }
      }
    },
    "property2": {
      "auth_key": "string",
      "auth_password": "string",
      "auth_type": "md5",
      "networks": {
        "property1": {
          "ip": "string"
        },
        "property2": {
          "ip": "string"
        }
      }
    }
  },
  "wids": {
    "repeated_auth_failures": {
      "duration": 0,
      "threshold": 0
    }
  },
  "wifi": {
    "cisco_enabled": true,
    "disable_11k": false,
    "disable_radios_when_power_constrained": true,
    "enable_arp_spoof_check": false,
    "enable_channel_144": false,
    "enable_shared_radio_scanning": true,
    "enable_vna": false,
    "enabled": true,
    "locate_connected": false,
    "locate_unconnected": false,
    "mesh_allow_dfs": false,
    "mesh_enabled": false,
    "proxy_arp": "default"
  },
  "zone_occupancy_alert": {
    "email_notifiers": [
      "string"
    ],
    "enabled": false,
    "threshold": 5
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSetting401ErrorException`](../../doc/models/api-v1-sites-setting-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSetting403ErrorException`](../../doc/models/api-v1-sites-setting-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSetting404ErrorException`](../../doc/models/api-v1-sites-setting-404-error-exception.md) |


# Delete Site Wireless Clients Blocklist

Delete Site Blacklist Station Clients

```python
def delete_site_wireless_clients_blocklist(self,
                                          site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_setting_controller.delete_site_wireless_clients_blocklist(site_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSettingBlacklist401ErrorException`](../../doc/models/api-v1-sites-setting-blacklist-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSettingBlacklist403ErrorException`](../../doc/models/api-v1-sites-setting-blacklist-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSettingBlacklist404ErrorException`](../../doc/models/api-v1-sites-setting-blacklist-404-error-exception.md) |


# Create Site Wireless Clients Blocklist

This endpoint is to provide list of client macs for annotation blacklist.

Retrieve the current clients list `blacklist_url` under Site:Setting

```python
def create_site_wireless_clients_blocklist(self,
                                          site_id,
                                          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ModelObjectMacsArrayString`](../../doc/models/model-object-macs-array-string.md) | Body, Optional | Request Body |

## Response Type

[`MacsArray`](../../doc/models/macs-array.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ModelObjectMacsArrayString(
    macs=[
        '18-65-90-de-f4-c6',
        '84-89-ad-5d-69-0d'
    ]
)

result = sites_setting_controller.create_site_wireless_clients_blocklist(
    site_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "macs": [
    "18-65-90-de-f4-c6",
    "84-89-ad-5d-69-0d"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSettingBlacklist401ErrorException`](../../doc/models/api-v1-sites-setting-blacklist-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSettingBlacklist403ErrorException`](../../doc/models/api-v1-sites-setting-blacklist-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSettingBlacklist404ErrorException`](../../doc/models/api-v1-sites-setting-blacklist-404-error-exception.md) |


# Delete Site Watched Stations

Delete Site Watched Station Clients

```python
def delete_site_watched_stations(self,
                                site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_setting_controller.delete_site_watched_stations(site_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSettingWatchedStation401ErrorException`](../../doc/models/api-v1-sites-setting-watched-station-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSettingWatchedStation403ErrorException`](../../doc/models/api-v1-sites-setting-watched-station-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSettingWatchedStation404ErrorException`](../../doc/models/api-v1-sites-setting-watched-station-404-error-exception.md) |


# Create Site Watched Stations

This endpoint is to provide list of client macs for annotation as  watched station.

Retrieve the current clients list from  `watched_station_url` under Site:Setting

```python
def create_site_watched_stations(self,
                                site_id,
                                body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ModelObjectMacsArrayString`](../../doc/models/model-object-macs-array-string.md) | Body, Optional | Request Body |

## Response Type

[`MacsArray`](../../doc/models/macs-array.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ModelObjectMacsArrayString(
    macs=[
        '18-65-90-de-f4-c6',
        '84-89-ad-5d-69-0d'
    ]
)

result = sites_setting_controller.create_site_watched_stations(
    site_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "macs": [
    "18-65-90-de-f4-c6",
    "84-89-ad-5d-69-0d"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSettingWatchedStation401ErrorException`](../../doc/models/api-v1-sites-setting-watched-station-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSettingWatchedStation403ErrorException`](../../doc/models/api-v1-sites-setting-watched-station-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSettingWatchedStation404ErrorException`](../../doc/models/api-v1-sites-setting-watched-station-404-error-exception.md) |


# Delete Site Wireless Clients Allowlist

Delete Site Whitelist Station Clients

```python
def delete_site_wireless_clients_allowlist(self,
                                          site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_setting_controller.delete_site_wireless_clients_allowlist(site_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSettingWhitelist401ErrorException`](../../doc/models/api-v1-sites-setting-whitelist-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSettingWhitelist403ErrorException`](../../doc/models/api-v1-sites-setting-whitelist-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSettingWhitelist404ErrorException`](../../doc/models/api-v1-sites-setting-whitelist-404-error-exception.md) |


# Create Site Wireless Clients Allowlist

This endpoint is to provide list of client macs for annotation as whitelist.

Retrieve the current clients list from `whitelist_url` under Site:Setting

```python
def create_site_wireless_clients_allowlist(self,
                                          site_id,
                                          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ModelObjectMacsArrayString`](../../doc/models/model-object-macs-array-string.md) | Body, Optional | Request Body |

## Response Type

[`MacsArray`](../../doc/models/macs-array.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ModelObjectMacsArrayString(
    macs=[
        '18-65-90-de-f4-c6',
        '84-89-ad-5d-69-0d'
    ]
)

result = sites_setting_controller.create_site_wireless_clients_allowlist(
    site_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "macs": [
    "18-65-90-de-f4-c6",
    "84-89-ad-5d-69-0d"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSettingWhitelist401ErrorException`](../../doc/models/api-v1-sites-setting-whitelist-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSettingWhitelist403ErrorException`](../../doc/models/api-v1-sites-setting-whitelist-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSettingWhitelist404ErrorException`](../../doc/models/api-v1-sites-setting-whitelist-404-error-exception.md) |

