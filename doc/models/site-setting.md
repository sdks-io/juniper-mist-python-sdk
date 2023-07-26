
# Site Setting

Site Settings

## Structure

`SiteSetting`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_config_cmds` | `List of string` | Optional | additional CLI commands to append to the generated switches config |
| `analytic` | [`Analytic`](../../doc/models/analytic.md) | Optional | - |
| `ap_matching` | [`ApMatching1`](../../doc/models/ap-matching-1.md) | Optional | - |
| `ap_port_config` | [`ApPortConfig1`](../../doc/models/ap-port-config-1.md) | Optional | - |
| `auto_placement` | [`AutoPlacement`](../../doc/models/auto-placement.md) | Optional | if we're able to determine its x/y/orientation, this will be populated |
| `auto_preemption` | [`AutoPreemption`](../../doc/models/auto-preemption.md) | Optional | schedule to preempt ap’s which are not connected to preferred peer |
| `auto_upgrade` | [`SiteAutoUpgrade`](../../doc/models/site-auto-upgrade.md) | Optional | Auto Upgrade Settings |
| `blacklist_url` | `string` | Optional | - |
| `ble_config` | [`ApBle`](../../doc/models/ap-ble.md) | Optional | BLE AP settings |
| `config_auto_revert` | `bool` | Optional | whether to enable ap auto config revert<br>**Default**: `False` |
| `created_time` | `float` | Optional | - |
| `device_updown_threshold` | `int` | Optional | sending AP_DISCONNECTED event in device-updowns only if AP_CONNECTED is not seen within the threshold, in minutes<br>**Default**: `0`<br>**Constraints**: `>= 0`, `<= 30` |
| `dns_servers` | `List of string` | Optional | list of NTP servers |
| `dns_suffix` | `List of string` | Optional | list of NTP servers |
| `enable_channel_144` | `bool` | Optional | whether to enable channel 144 (some older clients may not support it)<br>**Default**: `False` |
| `engagement` | [`SiteEngagement`](../../doc/models/site-engagement.md) | Optional | **Note**: if hours does not exist, it’s treated as everyday of the week, 00:00-23:59. Currently we don’t allow multiple ranges for the same day<br><br>**Note**: default values for `dwell_tags`: passerby (1,300) bounce (301, 14400) engaged (14401, 28800) stationed (28801, 42000)<br><br>**Note**: default values for `dwell_tag_names`: passerby = “Passerby”, bounce = “Visitor”, engaged = “Associates”, stationed = “Assets” |
| `evpn_options` | [`JunosEvpnOptions`](../../doc/models/junos-evpn-options.md) | Optional | EVPN Options |
| `flags` | `dict` | Optional | name/val pair objects for location engine to use |
| `for_site` | `bool` | Optional | - |
| `gateway_additional_config_cmds` | `List of string` | Optional | additional CLI commands to append to the generated config for gateways<br><br>**Note**: no check is done |
| `gateway_mgmt` | [`SiteGateway`](../../doc/models/site-gateway.md) | Optional | Gateway Site settings |
| `id` | `uuid\|string` | Optional | - |
| `led` | [`ApLed`](../../doc/models/ap-led.md) | Optional | LED AP settings |
| `modified_time` | `float` | Optional | - |
| `mxedge` | [`Mxedge1`](../../doc/models/mxedge-1.md) | Optional | site mist edges form a cluster of radsecproxy servers |
| `mxedge_mgmt` | [`MxedgeMgmt`](../../doc/models/mxedge-mgmt.md) | Optional | - |
| `mxtunnels` | [`SiteMxtunnel`](../../doc/models/site-mxtunnel.md) | Optional | Site MxTunnel |
| `networks` | [`dict`](../../doc/models/junos-networks.md) | Optional | the property key is the network name |
| `ntp_servers` | `List of string` | Optional | list of NTP servers |
| `occupancy` | [`SiteOccupancyAnalytics`](../../doc/models/site-occupancy-analytics.md) | Optional | Occupancy Analytics settings |
| `org_id` | `uuid\|string` | Optional | - |
| `ospf_areas` | [`dict`](../../doc/models/junos-ospf-areas.md) | Optional | the property key is the OSPF area |
| `persist_config_on_device` | `bool` | Optional | whether to store the config on AP<br>**Default**: `False` |
| `port_mirroring` | [`dict`](../../doc/models/junos-port-mirroring.md) | Optional | Property key is the port mirroring instance name<br>port_mirroring can be added under site/settings. It takes interface and ports as input for ingress, interface as input for egress and can take interface and port as output. |
| `port_usages` | [`PortUsages2`](../../doc/models/port-usages-2.md) | Optional | the property key is the port usage name |
| `proxy` | [`Proxy2`](../../doc/models/proxy-2.md) | Optional | Proxy Configuration for APs and Site Edges to talk to Mist |
| `radio_config` | [`ApRadio`](../../doc/models/ap-radio.md) | Optional | Radio AP settings |
| `radius_config` | [`JunosRadiusConfig`](../../doc/models/junos-radius-config.md) | Optional | Junos Radius config |
| `remote_syslog` | [`RemoteSyslog`](../../doc/models/remote-syslog.md) | Optional | - |
| `report_gatt` | `bool` | Optional | whether AP should periodically connect to BLE devices and report GATT device info (device name, manufacturer name, serial number, battery %, temperature, humidity)<br>**Default**: `False` |
| `rogue` | [`SiteRogue`](../../doc/models/site-rogue.md) | Optional | Rogue site settings |
| `rtsa` | [`Rtsa`](../../doc/models/rtsa.md) | Optional | managed mobility |
| `simple_alert` | [`SimpleAlert`](../../doc/models/simple-alert.md) | Optional | Set of heuristic rules will be enabled when marvis subscription is not available.<br>It triggers when, in a Z minute window, there are more than Y distinct client encountring over X failures |
| `site_id` | `uuid\|string` | Optional | - |
| `skyatp` | [`Skyatp`](../../doc/models/skyatp.md) | Optional | - |
| `srx_app` | [`SrxApp`](../../doc/models/srx-app.md) | Optional | - |
| `ssh_keys` | `List of string` | Optional | when limit_ssh_access = true in Org Setting, list of SSH public keys provided by Mist Support to install onto APs (see Org:Setting) |
| `ssr` | [`SiteSsr`](../../doc/models/site-ssr.md) | Optional | - |
| `status_portal` | [`StatusPortal`](../../doc/models/status-portal.md) | Optional | - |
| `switch_matching` | [`SwitchMatching`](../../doc/models/switch-matching.md) | Optional | - |
| `switch_mgmt` | [`SiteSwitch`](../../doc/models/site-switch.md) | Optional | Switch site settings |
| `track_anonymous_devices` | `bool` | Optional | whether to track anonymous BLE assets (requires ‘track_asset’ enabled)<br>**Default**: `False` |
| `tunterm_monitoring` | [`List of SiteTuntermMonitoring`](../../doc/models/site-tunterm-monitoring.md) | Optional | - |
| `tunterm_monitoring_disabled` | `bool` | Optional | - |
| `vars` | `dict` | Optional | - |
| `vna` | [`Vna`](../../doc/models/vna.md) | Optional | - |
| `vrf_instances` | [`dict`](../../doc/models/junos-vrf-instance.md) | Optional | the property key is the network name |
| `vrrp_groups` | [`dict`](../../doc/models/junos-vrrp-group.md) | Optional | the property key is the vrrp group |
| `vs_instances` | [`dict`](../../doc/models/vs-instances.md) | Optional | virtual-switch (for EX92xx and QFX5130)<br>all the networks not included here will be placed in default `evpn_vs` virtual-switch RI<br>Property key is the instance name |
| `wan_vna` | [`WanVna`](../../doc/models/wan-vna.md) | Optional | - |
| `watched_station_url` | `string` | Optional | - |
| `whitelist_url` | `string` | Optional | - |
| `wids` | [`SiteWids`](../../doc/models/site-wids.md) | Optional | WIDS site settings |
| `wifi` | [`SiteWifi`](../../doc/models/site-wifi.md) | Optional | Wi-Fi site settings |
| `wired_vna` | [`WiredVna`](../../doc/models/wired-vna.md) | Optional | - |
| `zone_occupancy_alert` | [`SiteZoneOccupancyAlert`](../../doc/models/site-zone-occupancy-alert.md) | Optional | Zone Occupancy alert site settings |

## Example (as JSON)

```json
{
  "config_auto_revert": false,
  "device_updown_threshold": 0,
  "enable_channel_144": false,
  "persist_config_on_device": false,
  "report_gatt": false,
  "track_anonymous_devices": false,
  "additional_config_cmds": [
    "additional_config_cmds6"
  ],
  "analytic": {
    "enabled": false
  },
  "ap_matching": {
    "enabled": false,
    "rules": [
      {
        "match_model": "match_model2",
        "name": "name0",
        "port_config": {
          "key0": {
            "additional_vlan_ids": [
              77
            ],
            "authentication_protocol": "pap",
            "disabled": false,
            "dynamic_vlan": {
              "default_vlan_id": 166,
              "enabled": false,
              "type": "type8",
              "vlans": {
                "key0": "vlans7",
                "key1": "vlans8",
                "key2": "vlans9"
              }
            },
            "enable_mac_auth": false
          }
        }
      },
      {
        "match_model": "match_model1",
        "name": "name9",
        "port_config": {
          "key0": {
            "additional_vlan_ids": [
              78,
              79
            ],
            "authentication_protocol": "eap-peap",
            "disabled": true,
            "dynamic_vlan": {
              "default_vlan_id": 165,
              "enabled": true,
              "type": "type9",
              "vlans": {
                "key0": "vlans6",
                "key1": "vlans7"
              }
            },
            "enable_mac_auth": true
          },
          "key1": {
            "additional_vlan_ids": [
              79,
              80,
              81
            ],
            "authentication_protocol": "eap-md5",
            "disabled": false,
            "dynamic_vlan": {
              "default_vlan_id": 164,
              "enabled": false,
              "type": "type0",
              "vlans": {
                "key0": "vlans5"
              }
            },
            "enable_mac_auth": false
          }
        }
      },
      {
        "match_model": "match_model0",
        "name": "name8",
        "port_config": {
          "key0": {
            "additional_vlan_ids": [
              79,
              80,
              81
            ],
            "authentication_protocol": "eap-md5",
            "disabled": false,
            "dynamic_vlan": {
              "default_vlan_id": 164,
              "enabled": false,
              "type": "type0",
              "vlans": {
                "key0": "vlans5"
              }
            },
            "enable_mac_auth": false
          },
          "key1": {
            "additional_vlan_ids": [
              80
            ],
            "authentication_protocol": "pap",
            "disabled": true,
            "dynamic_vlan": {
              "default_vlan_id": 163,
              "enabled": true,
              "type": "type1",
              "vlans": {
                "key0": "vlans4",
                "key1": "vlans5",
                "key2": "vlans6"
              }
            },
            "enable_mac_auth": true
          },
          "key2": {
            "additional_vlan_ids": [
              81,
              82
            ],
            "authentication_protocol": "eap-peap",
            "disabled": false,
            "dynamic_vlan": {
              "default_vlan_id": 162,
              "enabled": false,
              "type": "type2",
              "vlans": {
                "key0": "vlans3",
                "key1": "vlans4"
              }
            },
            "enable_mac_auth": false
          }
        }
      }
    ]
  },
  "ap_port_config": {
    "model_specific": {
      "key0": {
        "additional_vlan_ids": [
          191
        ],
        "authentication_protocol": "pap",
        "disabled": false,
        "dynamic_vlan": {
          "default_vlan_id": 8,
          "enabled": false,
          "type": "type8",
          "vlans": {
            "key0": "vlans3",
            "key1": "vlans4"
          }
        },
        "enable_mac_auth": false
      },
      "key1": {
        "additional_vlan_ids": [
          192,
          193
        ],
        "authentication_protocol": "eap-peap",
        "disabled": true,
        "dynamic_vlan": {
          "default_vlan_id": 9,
          "enabled": true,
          "type": "type9",
          "vlans": {
            "key0": "vlans4",
            "key1": "vlans5",
            "key2": "vlans6"
          }
        },
        "enable_mac_auth": true
      },
      "key2": {
        "additional_vlan_ids": [
          193,
          194,
          195
        ],
        "authentication_protocol": "eap-md5",
        "disabled": false,
        "dynamic_vlan": {
          "default_vlan_id": 10,
          "enabled": false,
          "type": "type0",
          "vlans": {
            "key0": "vlans5"
          }
        },
        "enable_mac_auth": false
      }
    }
  },
  "auto_placement": {
    "orientation": 98.14,
    "x": 15.0,
    "y": 146.28
  }
}
```

