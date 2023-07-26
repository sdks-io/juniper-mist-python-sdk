# Sites Pcaps

```python
sites_pcaps_controller = client.sites_pcaps
```

## Class Name

`SitesPcapsController`

## Methods

* [List Site Packet Captures](../../doc/controllers/sites-pcaps.md#list-site-packet-captures)
* [Stop Site Packet Capture](../../doc/controllers/sites-pcaps.md#stop-site-packet-capture)
* [Get Site Capturing Status](../../doc/controllers/sites-pcaps.md#get-site-capturing-status)
* [Start Site Packet Capture](../../doc/controllers/sites-pcaps.md#start-site-packet-capture)
* [Update Site Packet Capture](../../doc/controllers/sites-pcaps.md#update-site-packet-capture)


# List Site Packet Captures

Get List of Site Packet Captures

```python
def list_site_packet_captures(self,
                             site_id,
                             page=1,
                             limit=100,
                             start=0,
                             end=0,
                             duration='1d',
                             client_mac=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |
| `client_mac` | `string` | Query, Optional | optional client mac filter |

## Response Type

[`PcapsSearch`](../../doc/models/pcaps-search.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

page = 1

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_pcaps_controller.list_site_packet_captures(
    site_id,
    page,
    limit,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "end": 1461089816,
  "limit": 100,
  "next": "/api/v1/sites/67970e46-4e12-11e6-9188-0242ac110007/insights/marvis?start=1461099816&token=AAAAFgAIAAAAAFj6ohEAAAhzZXZlcml0eQB%2F%2F%2F%2F1&limit=100&end=1461089816",
  "results": [
    {
      "ap_macs": [
        "5c5b35000010"
      ],
      "timestamp": 1461869041,
      "type": "new_assoc",
      "url": "https://..."
    }
  ],
  "start": 1461099816
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesPcaps401ErrorException`](../../doc/models/api-v1-sites-pcaps-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesPcaps403ErrorException`](../../doc/models/api-v1-sites-pcaps-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesPcaps404ErrorException`](../../doc/models/api-v1-sites-pcaps-404-error-exception.md) |


# Stop Site Packet Capture

Stop current capture

```python
def stop_site_packet_capture(self,
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

result = sites_pcaps_controller.stop_site_packet_capture(site_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesPcapsCapture401ErrorException`](../../doc/models/api-v1-sites-pcaps-capture-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesPcapsCapture403ErrorException`](../../doc/models/api-v1-sites-pcaps-capture-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesPcapsCapture404ErrorException`](../../doc/models/api-v1-sites-pcaps-capture-404-error-exception.md) |


# Get Site Capturing Status

Get Capturing status

```python
def get_site_capturing_status(self,
                             site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`PcapStatus`](../../doc/models/pcap-status.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_pcaps_controller.get_site_capturing_status(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "aps": [
    "5c5b350e001c",
    "5c5b350e001b"
  ],
  "client_mac": "60a10a773412",
  "duration": 300,
  "failed": [],
  "id": "a9a84e13-a714-b1eb-152f-a434416217d5",
  "includes_mcast": false,
  "max_pkt_len": 128,
  "num_packets": 1000,
  "ok": [
    "5c5b350e001c",
    "5c5b350e001b"
  ],
  "started_time": 1435080709,
  "type": "client"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesPcapsCapture401ErrorException`](../../doc/models/api-v1-sites-pcaps-capture-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesPcapsCapture403ErrorException`](../../doc/models/api-v1-sites-pcaps-capture-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesPcapsCapture404ErrorException`](../../doc/models/api-v1-sites-pcaps-capture-404-error-exception.md) |


# Start Site Packet Capture

Initiate a Packet Capture

The output will be available through websocket. As there can be multiple command issued against the same AP at the same time and the output all goes through the same websocket stream, session is introduced for demux.

#### Subscribe to Device Command outputs

`WS /api-ws/v1/stream`

```json
{
    subscribe: "/sites/{site_id}/pcaps"
}
```

#### Response (Wireless/RadioTap)

```json
{
    "event": "data"
    "channel": "/sites/:site_id/pcaps"
    "data": {
         "capture_id": "6b1be4fb-b239-44d9-9d3b-cb1ff3af1721",
     "lost_messages": 0
         "pcap_dict": {
             "channel_frequency": 2412,
             "channel": "1",
             "datarate": "1.0 Mbps",
             "rssi": -75, 
             "dst": "78:bd:bc:ca:0b:0a",
             "src": "18:b8:1f:4c:91:c0",
             "bssid": "18:b8:1f:4c:91:c0",
             "frame_type": "Management", 
             "frame_subtype": "Probe Response", 
         "proto": "802.11", 
             "ap_mac": "d4:20:b0:81:99:2e", 
             "direction": "tx", 
             "timestamp": 1652246543, 
             "length": 416.0,
             "interface": "radiotap",
             "info": "1652246544.467733 1683216786us tsft 1.0 Mb/s 2412 MHz 11g -75dBm signal -82dBm noise antenna 0 Probe Response (ATTKmsWiVS) [1.0* 2.0* 5.5* 11.0* 18.0 24.0 36.0 54.0 Mbit] CH: 2, PRIVACY\\n",
         }, 
        "pcap_raw": "1MOyoQIABAAAAAAAAAAAAP//AAABAAAAEEh7Yh5VBwCgAQAAoAEAAAAAKwBvCADAAQAAAIw7reCS2VNkAAAAABACbAmABLWuAAEAEBgAAwACAABQADoBeL28ygsKGLgfTJHAGLgfTJHAcIZ2WDlBJQAAAGQAERUACkFUVEttc1dpVlMBCIKEi5YkMEhsAwECBwZVUyABCx4gAQAjAhkAKgEEMgQMEhhgMBQBAAAPrAQBAAAPrAQBAAAPrAIMAAsFAQAbAABGBTIIAQAALRqtCR////8AAAAAAAAAAAAAAAAAAAAAAAAAAD0WAggVAAAAAAAAAAAAAAAAAAAAAAAAAH8IBAAIAAAAAEDdkwBQ8gQQSgABEBBEAAECEDsAAQMQRwAQn2481frn3KT+uGod2ERx+RAhAAtBcnJpcywgSW5jLhAjAApCR1cyMTAtNzAwECQACkJHVzIxMC03MDAQQgAKQkdXMjEwLTcwMBBUAAgABgBQ8gQAARARAA5BcnJpcyBXaXJlbGVzcxAIAAIgCBA8AAEBEEkABgA3KgABIN0JABAYAgEQHAAA3RgAUPICAQGEAAOkAAAnpAAAQkNeAGIyLwAzjakr"
}
```

#### vResponse (Wired)

```json
{
    "event": "data"
    "channel": "/sites/67970e46-4e12-11e6-9188-0242ac110007/pcaps"
    "data": {
        "capture_id": "f039b1b4-a23e-48b2-906a-0da40524de73", 
        "pcap_dict": {
             "dst_mac": "68:ec:c5:09:2e:87",
             "src_mac": "8c:3b:ad:e0:47:40", 
             "vlan": 1, 
             "src_ip": "34.224.147.117", 
             "dst_ip": "192.168.1.55",
             "dst_port": 51635, 
             "src_port": 443,
             "proto": "TCP", 
             "ap_mac": "d4:20:b0:81:99:2e",
             "direction": "tx", 
             "timestamp": 1652247615, 
             "length": 159.0, 
             "interface": "wired",
             "info": "1652247616.007409 IP ec2-34-224-147-117.compute-1.amazonaws.com.https > ip-192-168-1-55.ec2.internal.51635: Flags [P.], seq 2192123968:2192124057, ack 4035166782, win 12, options [nop,nop,TS val 597467050 ecr 740580660], length 89\\n",
             }, 
        "pcap_raw": "1MOyoQIABAAAAAAAAAAAAP//AAABAAAAQEx7YhMzAACfAAAAnwAAAGjsxQkuh4w7reBHQIEAAAEIAEUAAI1bLEAAKAZ/CiLgk3XAqAE3AbvJs4KpKEDwg8I+gBgADFf9AAABAQgKI5yfqiwkXTQXAwMAVKY5JopoKQrVEn0/3ld4YntctGEH/rTZuwtCvzSncFw71QJveJi9uxHs57KC8w9Apph3YvXJrmWg7M37+o+YV0KH/xmr626s5Bkhb3QhKOu+NoNEmA=="

    }
}
```

#### Stop Response (Wired/Wireless)

```json
{
    "event": "data"
    "channel": "/sites/67970e46-4e12-11e6-9188-0242ac110007/pcaps"
    "data": {
      "capture_id": "a2f7374d-6a70-41fd-8a3f-71e42573baaf", 
      "lost_messages": 0,
      "pcap_dict": null
    }
}
```

```python
def start_site_packet_capture(self,
                             site_id,
                             body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Capture`](../../doc/models/capture.md) | Body, Optional | Request Body |

## Response Type

[`PcapStart`](../../doc/models/pcap-start.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Capture(
    client_mac='60a10a773412',
    duration=600,
    includes_mcast=False,
    max_pkt_len=128,
    num_packets=100,
    mtype=envrr
)

result = sites_pcaps_controller.start_site_packet_capture(
    site_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "ap_count": 3,
  "aps": [],
  "duration": 600,
  "enabled": true,
  "expiry": 1614886726.5411825,
  "format": "stream",
  "id": "a9a84e13-a714-b1eb-152f-a434416217d5",
  "include_mcast": false,
  "invalid_aps": {},
  "max_pkt_len": 68,
  "num_packets": 100,
  "org_id": "a9346fba-f920-e99a-cc51-2e8dcc57fa3c",
  "raw": true,
  "site_id": "67970e46-4e12-11e6-9188-0242ac110007",
  "ssid": "",
  "timestamp": 1614886126.5411825,
  "type": "radiotap"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesPcapsCapture401ErrorException`](../../doc/models/api-v1-sites-pcaps-capture-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesPcapsCapture403ErrorException`](../../doc/models/api-v1-sites-pcaps-capture-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesPcapsCapture404ErrorException`](../../doc/models/api-v1-sites-pcaps-capture-404-error-exception.md) |


# Update Site Packet Capture

Update or add notes to a completed packet capture

```python
def update_site_packet_capture(self,
                              site_id,
                              pcap_id,
                              body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `pcap_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesPcapsRequest`](../../doc/models/api-v1-sites-pcaps-request.md) | Body, Optional | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

pcap_id = '00002548-0000-0000-0000-000000000000'

body = ApiV1SitesPcapsRequest(
    notes='wired pcap test'
)

result = sites_pcaps_controller.update_site_packet_capture(
    site_id,
    pcap_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesPcaps401ErrorException`](../../doc/models/api-v1-sites-pcaps-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesPcaps403ErrorException`](../../doc/models/api-v1-sites-pcaps-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesPcaps404ErrorException`](../../doc/models/api-v1-sites-pcaps-404-error-exception.md) |

