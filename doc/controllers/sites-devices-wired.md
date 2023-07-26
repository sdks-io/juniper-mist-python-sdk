# Sites Devices-Wired

```python
sites_devices_wired_controller = client.sites_devices_wired
```

## Class Name

`SitesDevicesWiredController`

## Methods

* [Ports Bounce From Switch](../../doc/controllers/sites-devices-wired.md#ports-bounce-from-switch)
* [Cable Test From Switch](../../doc/controllers/sites-devices-wired.md#cable-test-from-switch)
* [Clear Bpdu Erros From Ports on Switch](../../doc/controllers/sites-devices-wired.md#clear-bpdu-erros-from-ports-on-switch)
* [Clear All Learned Macs From Port on Switch](../../doc/controllers/sites-devices-wired.md#clear-all-learned-macs-from-port-on-switch)
* [Delete Site Local Switch Port Config](../../doc/controllers/sites-devices-wired.md#delete-site-local-switch-port-config)
* [Update Site Local Switch Port Config](../../doc/controllers/sites-devices-wired.md#update-site-local-switch-port-config)
* [Poll Site Switch Stats](../../doc/controllers/sites-devices-wired.md#poll-site-switch-stats)
* [Get Site Switches Metrics](../../doc/controllers/sites-devices-wired.md#get-site-switches-metrics)


# Ports Bounce From Switch

Port Bounce can be performed from the Switch.The output will be available through websocket. As there can be multiple command issued against the same AP at the same time and the output all goes through the same websocket stream, session is introduced for demux.

#### Subscribe to Device Command outputs

`WS /api-ws/v1/stream`

```json
{
    "subscribe": "/sites/{site_id}/devices/{device_id}/cmd"
}
```

##### Example output from ws stream

```json
{
    "event": "data",
    "channel": "/sites/4ac1dcf4-9d8b-7211-65c4-057819f0862b/devices/00000000-0000-0000-1000-5c5b350e0060/cmd",
    "data": {
        "session": "session_id",
        "raw": "Port bounce complete."
    }
}
```

```python
def ports_bounce_from_switch(self,
                            site_id,
                            device_id,
                            body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesDevicesBouncePortRequest`](../../doc/models/api-v1-sites-devices-bounce-port-request.md) | Body, Optional | Request Body |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ApiV1SitesDevicesBouncePortRequest(
    ports=[
        'ge-0/0/0',
        'ge-0/0/1'
    ]
)

result = sites_devices_wired_controller.ports_bounce_from_switch(
    site_id,
    device_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesBouncePort401ErrorException`](../../doc/models/api-v1-sites-devices-bounce-port-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesBouncePort403ErrorException`](../../doc/models/api-v1-sites-devices-bounce-port-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesBouncePort404ErrorException`](../../doc/models/api-v1-sites-devices-bounce-port-404-error-exception.md) |


# Cable Test From Switch

TDR can be performed from the Switch. The output will be available through websocket. As there can be multiple command issued against the same Switch at the same time and the output all goes through the same websocket stream, session is introduced for demux.

#### Subscribe to Device Command outputs

`WS /api-ws/v1/stream`

```json
{
    "subscribe": "/sites/{site_id}/devices/{device_id}/cmd"
}
```

##### Example output from ws stream

```json
{
    "event": "data",
    "channel": "/sites/4ac1dcf4-9d8b-7211-65c4-057819f0862b/devices/00000000-0000-0000-1000-5c5b350e0060/cmd",
    "data": {
        "session": "session_id",
        "raw": "Interface TDR detail:\nTest status : Test successfully executed  ge-0/0/0\n"
    }
}
```

```python
def cable_test_from_switch(self,
                          site_id,
                          device_id,
                          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesDevicesCableTestRequest`](../../doc/models/api-v1-sites-devices-cable-test-request.md) | Body, Optional | - |

## Response Type

[`Session1`](../../doc/models/session-1.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ApiV1SitesDevicesCableTestRequest(
    port='ge-0/0/0'
)

result = sites_devices_wired_controller.cable_test_from_switch(
    site_id,
    device_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "session": "session_id"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesCableTest401ErrorException`](../../doc/models/api-v1-sites-devices-cable-test-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesCableTest403ErrorException`](../../doc/models/api-v1-sites-devices-cable-test-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesCableTest404ErrorException`](../../doc/models/api-v1-sites-devices-cable-test-404-error-exception.md) |


# Clear Bpdu Erros From Ports on Switch

Clear bridge protocol data unit (BPDU) error condition caused by the detection of a possible bridging loop from Spanning Tree Protocol (STP) operation that renders the port unoperational.

```python
def clear_bpdu_erros_from_ports_on_switch(self,
                                         site_id,
                                         device_id,
                                         body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesDevicesClearBpduErrorRequest`](../../doc/models/api-v1-sites-devices-clear-bpdu-error-request.md) | Body, Optional | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_devices_wired_controller.clear_bpdu_erros_from_ports_on_switch(
    site_id,
    device_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Port not specified | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesClearBpduError401ErrorException`](../../doc/models/api-v1-sites-devices-clear-bpdu-error-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesClearBpduError403ErrorException`](../../doc/models/api-v1-sites-devices-clear-bpdu-error-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesClearBpduError404ErrorException`](../../doc/models/api-v1-sites-devices-clear-bpdu-error-404-error-exception.md) |


# Clear All Learned Macs From Port on Switch

Clear all learned MAC addresses, including persistent MAC addresses, on a port.

```python
def clear_all_learned_macs_from_port_on_switch(self,
                                              site_id,
                                              device_id,
                                              body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesDevicesClearMacsRequest`](../../doc/models/api-v1-sites-devices-clear-macs-request.md) | Body, Optional | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ApiV1SitesDevicesClearMacsRequest(
    ports=[
        'ge-0/0/0.0'
    ]
)

result = sites_devices_wired_controller.clear_all_learned_macs_from_port_on_switch(
    site_id,
    device_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesClearMacs401ErrorException`](../../doc/models/api-v1-sites-devices-clear-macs-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesClearMacs403ErrorException`](../../doc/models/api-v1-sites-devices-clear-macs-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesClearMacs404ErrorException`](../../doc/models/api-v1-sites-devices-clear-macs-404-error-exception.md) |


# Delete Site Local Switch Port Config

Sometimes HelpDesk Admin needs to change port configs

```python
def delete_site_local_switch_port_config(self,
                                        site_id,
                                        device_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_devices_wired_controller.delete_site_local_switch_port_config(
    site_id,
    device_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesLocalPortConfig401ErrorException`](../../doc/models/api-v1-sites-devices-local-port-config-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesLocalPortConfig403ErrorException`](../../doc/models/api-v1-sites-devices-local-port-config-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesLocalPortConfig404ErrorException`](../../doc/models/api-v1-sites-devices-local-port-config-404-error-exception.md) |


# Update Site Local Switch Port Config

Sometimes HelpDesk Admin needs to change port configs

```python
def update_site_local_switch_port_config(self,
                                        site_id,
                                        device_id,
                                        body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `body` | [`JunosPortConfig`](../../doc/models/junos-port-config.md) | Body, Optional | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = JunosPortConfig(
    usage='string',
    ae_disable_lacp=True,
    ae_idx=0,
    aggregated=False,
    description='string',
    disable_autoneg=True,
    duplex=DuplexEnum.AUTO,
    dynamic_usage='string',
    esilag=True,
    poe_disabled=True,
    speed=SpeedEnum.AUTO
)

result = sites_devices_wired_controller.update_site_local_switch_port_config(
    site_id,
    device_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesLocalPortConfig401ErrorException`](../../doc/models/api-v1-sites-devices-local-port-config-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesLocalPortConfig403ErrorException`](../../doc/models/api-v1-sites-devices-local-port-config-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesLocalPortConfig404ErrorException`](../../doc/models/api-v1-sites-devices-local-port-config-404-error-exception.md) |


# Poll Site Switch Stats

This API can be used to poll statistics from the Switch proactively once. After it is called, the statistics will be pushed back to the cloud within the statistics interval.

```python
def poll_site_switch_stats(self,
                          site_id,
                          device_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_devices_wired_controller.poll_site_switch_stats(
    site_id,
    device_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesPollStats401ErrorException`](../../doc/models/api-v1-sites-devices-poll-stats-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesPollStats403ErrorException`](../../doc/models/api-v1-sites-devices-poll-stats-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesPollStats404ErrorException`](../../doc/models/api-v1-sites-devices-poll-stats-404-error-exception.md) |


# Get Site Switches Metrics

Get version compliance metrics for managed or monitored switches

```python
def get_site_switches_metrics(self,
                             site_id,
                             mtype=None,
                             scope=None,
                             switch_mac=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `mtype` | [`Type64Enum`](../../doc/models/type-64-enum.md) | Query, Optional | - |
| `scope` | [`Scope17Enum`](../../doc/models/scope-17-enum.md) | Query, Optional | - |
| `switch_mac` | `string` | Query, Optional | switch mac, used only with metric `type`==`active_ports_summary` |

## Response Type

[`ApiV1SitesStatsSwitchesMetricsResponse`](../../doc/models/api-v1-sites-stats-switches-metrics-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_devices_wired_controller.get_site_switches_metrics(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "active_ports_summary": {
    "details": {
      "active_port_count": 4,
      "total_port_count": 4
    },
    "score": 100,
    "total_switch_count": 2
  },
  "config_success": {
    "details": {
      "config_success_count": 2
    },
    "score": 100,
    "total_switch_count": 2
  },
  "version_compliance": {
    "details": {
      "major_versions": [
        {
          "major_count": 1,
          "major_version": "21.4R3.5",
          "model": "EX2300-C-12P",
          "system_names": []
        },
        {
          "major_count": 1,
          "major_version": "6.0.4-11",
          "model": "SSR120",
          "system_names": []
        }
      ]
    },
    "score": 100,
    "total_switch_count": 2
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsSwitchesMetrics401ErrorException`](../../doc/models/api-v1-sites-stats-switches-metrics-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsSwitchesMetrics403ErrorException`](../../doc/models/api-v1-sites-stats-switches-metrics-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsSwitchesMetrics404ErrorException`](../../doc/models/api-v1-sites-stats-switches-metrics-404-error-exception.md) |

