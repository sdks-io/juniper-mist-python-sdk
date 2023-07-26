# Webhook Samples

```python
webhook_samples_controller = client.webhook_samples
```

## Class Name

`WebhookSamplesController`

## Methods

* [Alarms](../../doc/controllers/webhook-samples.md#alarms)
* [Asset Raw](../../doc/controllers/webhook-samples.md#asset-raw)
* [Audits](../../doc/controllers/webhook-samples.md#audits)
* [Client Join](../../doc/controllers/webhook-samples.md#client-join)
* [Client Sessions](../../doc/controllers/webhook-samples.md#client-sessions)
* [Device Events](../../doc/controllers/webhook-samples.md#device-events)
* [Device up Down](../../doc/controllers/webhook-samples.md#device-up-down)
* [Discovered-Raw-Rssi](../../doc/controllers/webhook-samples.md#discovered-raw-rssi)
* [Location](../../doc/controllers/webhook-samples.md#location)
* [Occupancy Alerts](../../doc/controllers/webhook-samples.md#occupancy-alerts)
* [Ping](../../doc/controllers/webhook-samples.md#ping)
* [Sdkclient Scan Data](../../doc/controllers/webhook-samples.md#sdkclient-scan-data)
* [Zone](../../doc/controllers/webhook-samples.md#zone)


# Alarms

Webhook sample for `alarm` topic

**Note**: The server host will be your own server FQDN where the Mist Cloud is sending the webhook messages

```python
def alarms(self,
          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`WebhookAlarms`](../../doc/models/webhook-alarms.md) | Body, Optional | **N.B.**: Fields like `aps`, `bssids`, `ssids` are event specific. They are relevant to this event type ( rogue-ap-detected). For a different event type, different fields may be sent. These don’t contain all affected entities and are representative samples of entities (capped at 10). For marvis action related events, we expose `details` to include more event specific details.<br><br>Events specific fields for other alarm event type can be found with API https://api.mist.com/api/v1/const/alarm_defs, under “fields” array of /alarm_defs response object. |

## Response Type

`object`

## Example Usage

```python
body = WebhookAlarms(
    events=[
        Event(
            None,
            None,
            None,
            None,
            None,
            None
        )
    ],
    topic='alarms'
)

result = webhook_samples_controller.alarms(
    body
)
print(result)
```


# Asset Raw

Webhook sample for `asset_raw` topic

**Note**: The server host will be your own server FQDN where the Mist Cloud is sending the webhook messages

**will be deprecated after 03/31/2024**

```python
def asset_raw(self,
             body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`WebhookAssetRaw`](../../doc/models/webhook-asset-raw.md) | Body, Optional | - |

## Response Type

`object`

## Example Usage

```python
body = WebhookAssetRaw(
    events=[
        Event1(
            asset_id='b4695157-0d1d-4da0-8f9e-5c53149389e4',
            beam=0,
            device_id='3bafab7b-4400-4bcf-8e6e-09f954699940',
            mac='string',
            map_id='09d2b626-2e4e-45ef-a3c4-e6aeb6c83db1',
            mfg_company_id=0,
            mfg_data='string',
            rssi=0,
            site_id='72771e6a-6f5e-4de4-a5b9-1266c4197811',
            timestamp=0,
            ibeacon_major=0,
            ibeacon_minor=0,
            ibeacon_uuid='1f89bc00-d0af-481b-82fe-a6629259a39f'
        )
    ],
    topic='asset-raw'
)

result = webhook_samples_controller.asset_raw(
    body
)
print(result)
```


# Audits

Webhook sample for `audit` topic

**Note**: The server host will be your own server FQDN where the Mist Cloud is sending the webhook messages

```python
def audits(self,
          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`WebhookAudits`](../../doc/models/webhook-audits.md) | Body, Optional | - |

## Response Type

`object`

## Example Usage

```python
body = WebhookAudits(
    events=[
        Event2(
            admin_name='string',
            device_id='3bafab7b-4400-4bcf-8e6e-09f954699940',
            id='488f6eca-6276-4993-bfeb-d3cbbbba6f08',
            message='string',
            org_id='a40f5d1f-d889-42e9-94ea-b9b33585fc6b',
            site_id='72771e6a-6f5e-4de4-a5b9-1266c4197811',
            src_ip='string',
            timestamp=0
        )
    ],
    topic='audits'
)

result = webhook_samples_controller.audits(
    body
)
print(result)
```


# Client Join

Webhook sample for `client_join` topic

**Note**: The server host will be your own server FQDN where the Mist Cloud is sending the webhook messages

```python
def client_join(self,
               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`WebhookClientJoin`](../../doc/models/webhook-client-join.md) | Body, Optional | - |

## Response Type

`object`

## Example Usage

```python
body = WebhookClientJoin(
    events=[
        Event3(
            ap='string',
            ap_name='string',
            band='string',
            bssid='string',
            connect=0,
            connect_float=0,
            mac='string',
            org_id='a40f5d1f-d889-42e9-94ea-b9b33585fc6b',
            rssi=0,
            site_id='72771e6a-6f5e-4de4-a5b9-1266c4197811',
            site_name='string',
            ssid='string',
            timestamp=0,
            version=0,
            wlan_id='5028e92b-fc59-4056-91d1-ea4b4ca1617a'
        )
    ],
    topic='client-join'
)

result = webhook_samples_controller.client_join(
    body
)
print(result)
```


# Client Sessions

Webhook sample for `client_sessions` topic

**Note**: The server host will be your own server FQDN where the Mist Cloud is sending the webhook messages

```python
def client_sessions(self,
                   body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`WebhookClientSessions`](../../doc/models/webhook-client-sessions.md) | Body, Optional | - |

## Response Type

`object`

## Example Usage

```python
body = WebhookClientSessions(
    events=[
        Event4(
            ap='string',
            ap_name='string',
            band='string',
            bssid='string',
            client_family='string',
            client_manufacture='string',
            client_model='string',
            client_os='string',
            connect=0,
            connect_float=0,
            disconnect=0,
            disconnect_float=0,
            duration=0,
            mac='string',
            next_ap='string',
            org_id='a40f5d1f-d889-42e9-94ea-b9b33585fc6b',
            rssi=0,
            site_id='72771e6a-6f5e-4de4-a5b9-1266c4197811',
            site_name='string',
            ssid='string',
            termination_reason=0,
            timestamp=0,
            version=0,
            wlan_id='5028e92b-fc59-4056-91d1-ea4b4ca1617a'
        )
    ],
    topic='client-sessions'
)

result = webhook_samples_controller.client_sessions(
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |


# Device Events

Webhook sample for `device_events` topic

**Note**: The server host will be your own server FQDN where the Mist Cloud is sending the webhook messages

```python
def device_events(self,
                 body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`WebhookDeviceEvents`](../../doc/models/webhook-device-events.md) | Body, Optional | - |

## Response Type

`object`

## Example Usage

```python
body = WebhookDeviceEvents(
    events=[
        Event5(
            device_name='string',
            device_type=DeviceType1Enum.AP,
            ev_type=EvTypeEnum.NOTICE,
            mac='string',
            org_id='a40f5d1f-d889-42e9-94ea-b9b33585fc6b',
            timestamp=0,
            mtype='string',
            ap='string',
            ap_name='string',
            audit_id='78c04fa6-cfb4-46a0-9aa5-3681ba4f3897',
            reason='string',
            site_id='72771e6a-6f5e-4de4-a5b9-1266c4197811',
            site_name='string',
            text='string'
        )
    ],
    topic='device-events'
)

result = webhook_samples_controller.device_events(
    body
)
print(result)
```


# Device up Down

Webhook sample for `device_updowns` topic

**Note**: The server host will be your own server FQDN where the Mist Cloud is sending the webhook messages

```python
def device_up_down(self,
                  body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`WebhookDeviceUpdowns`](../../doc/models/webhook-device-updowns.md) | Body, Optional | - |

## Response Type

`object`

## Example Usage

```python
body = WebhookDeviceUpdowns(
    events=[
        Event6(
            ap='string',
            ap_name='string',
            org_id='a40f5d1f-d889-42e9-94ea-b9b33585fc6b',
            site_id='72771e6a-6f5e-4de4-a5b9-1266c4197811',
            site_name='string',
            timestamp=0,
            mtype='string',
            for_site=True
        )
    ],
    topic='device-updowns'
)

result = webhook_samples_controller.device_up_down(
    body
)
print(result)
```


# Discovered-Raw-Rssi

Webhook sample for `discovered-raw-rssi` topic

**Note**: The server host will be your own server FQDN where the Mist Cloud is sending the webhook messages

```python
def discovered_raw_rssi(self,
                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`WebhookDiscoveredRawRssi`](../../doc/models/webhook-discovered-raw-rssi.md) | Body, Optional | - |

## Response Type

`object`

## Example Usage

```python
body = WebhookDiscoveredRawRssi(
    topic='string',
    events=[
        Event7(
            beam=0,
            device_id='3bafab7b-4400-4bcf-8e6e-09f954699940',
            mac='string',
            map_id='09d2b626-2e4e-45ef-a3c4-e6aeb6c83db1',
            org_id='a40f5d1f-d889-42e9-94ea-b9b33585fc6b',
            rssi=0,
            site_id='72771e6a-6f5e-4de4-a5b9-1266c4197811',
            ap_loc=[
                0
            ],
            ibeacon_major=0,
            ibeacon_minor=0,
            ibeacon_uuid='1f89bc00-d0af-481b-82fe-a6629259a39f',
            is_asset=True,
            mfg_company_id='string',
            mfg_data='string',
            service_packets=[
                ServicePacket1(
                    service_data='string',
                    service_uuid='7138cc00-c611-4dec-a05e-5c4b1cae13c0'
                )
            ],
            timestamp=0
        )
    ]
)

result = webhook_samples_controller.discovered_raw_rssi(
    body
)
print(result)
```


# Location

Webhook sample for `location` topic

**Note**: The server host will be your own server FQDN where the Mist Cloud is sending the webhook messages

```python
def location(self,
            body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`WebhookLocation`](../../doc/models/webhook-location.md) | Body, Optional | - |

## Response Type

`object`

## Example Usage

```python
body = WebhookLocation(
    events=[
        Event8(
            id='487f6eca-6276-4993-bfeb-e3cbbbba6f08',
            map_id='09d2b626-2e4e-45ef-a3c4-e6aeb6c83db1',
            site_id='72771e6a-6f5e-4de4-a5b9-1266c4197811',
            timestamp=0,
            mtype='string',
            x=0,
            y=0,
            battery_voltage=0,
            eddystone_uid_instance='string',
            eddystone_uid_namespace='string',
            eddystone_url_url='string',
            ibeacon_major=0,
            ibeacon_minor=0,
            ibeacon_uuid='1f89bc00-d0af-481b-82fe-a6629259a39f',
            mac='string',
            mfg_company_id=0,
            mfg_data='string',
            name='string'
        )
    ],
    topic='location'
)

result = webhook_samples_controller.location(
    body
)
print(result)
```


# Occupancy Alerts

Webhook sample for `occupancy_alerts` topic

**Note**: The server host will be your own server FQDN where the Mist Cloud is sending the webhook messages

```python
def occupancy_alerts(self,
                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`WebhookOccupancyAlerts`](../../doc/models/webhook-occupancy-alerts.md) | Body, Optional | - |

## Response Type

`object`

## Example Usage

```python
body = WebhookOccupancyAlerts(
    events=[
        Event9(
            None,
            None
        )
    ],
    topic='occupancy-alerts'
)

result = webhook_samples_controller.occupancy_alerts(
    body
)
print(result)
```


# Ping

Webhook sample for `ping` topic

**Note**: The server host will be your own server FQDN where the Mist Cloud is sending the webhook messages

```python
def ping(self,
        body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`WebhookPing`](../../doc/models/webhook-ping.md) | Body, Optional | - |

## Response Type

`object`

## Example Usage

```python
body = WebhookPing(
    events=[
        Event10(
            id='487f6eca-6276-4993-bfeb-f3cbbbba6f08',
            name='string',
            site_id='72771e6a-6f5e-4de4-a5b9-1266c4197811',
            timestamp=0
        )
    ],
    topic='ping'
)

result = webhook_samples_controller.ping(
    body
)
print(result)
```


# Sdkclient Scan Data

Webhook sample for `sdkclient_scan_data` topic

**Note**: The server host will be your own server FQDN where the Mist Cloud is sending the webhook messages

```python
def sdkclient_scan_data(self,
                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`WebhookSdkclientScanData`](../../doc/models/webhook-sdkclient-scan-data.md) | Body, Optional | - |

## Response Type

`object`

## Example Usage

```python
body = WebhookSdkclientScanData(
    events=[
        Event11(
            connection_ap='5c5b352f587e',
            connection_band='2.4',
            connection_bssid='5c5b352b51b4',
            connection_channel=11,
            connection_rssi=-87,
            last_seen=1592333828,
            mac='70ef0071535f',
            site_id='d761985e-49b1-4506-88e9-e0368a05c301',
            scan_data=[
                ScanDatum(
                    ap='5c5b352f587e',
                    band=Band12Enum.ENUM_24,
                    bssid='5c5b352b51b4',
                    channel=11,
                    rssi=-87,
                    ssid='mist-wifi',
                    timestamp=1592333828
                ),
                ScanDatum(
                    ap='5c5b352f587e',
                    band=Band12Enum.ENUM_5,
                    bssid='5c5b352b51b8',
                    channel=36,
                    rssi=-75,
                    ssid='mist-wifi',
                    timestamp=1592333828
                )
            ]
        )
    ],
    topic='sdkclient-scan-data'
)

result = webhook_samples_controller.sdkclient_scan_data(
    body
)
print(result)
```


# Zone

Webhook sample for `zone` topic

**Note**: The server host will be your own server FQDN where the Mist Cloud is sending the webhook messages

```python
def zone(self,
        body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`WebhookZone`](../../doc/models/webhook-zone.md) | Body, Optional | - |

## Response Type

`object`

## Example Usage

```python
body = WebhookZone(
    events=[
        Event12(
            id='485f6eca-6276-4993-bfeb-54cbbbba6f08',
            map_id='09d2b626-2e4e-45ef-a3c4-e6aeb6c83db1',
            site_id='72771e6a-6f5e-4de4-a5b9-1266c4197811',
            timestamp=0,
            trigger=TriggerEnum.ENTER,
            mtype='string',
            zone_id='4495020a-236f-46e0-9453-e3f9cc6476f4',
            asset_id='b4695157-0d1d-4da0-8f9e-5c53149389e4',
            mac='string',
            name='string'
        )
    ],
    topic='zone'
)

result = webhook_samples_controller.zone(
    body
)
print(result)
```

