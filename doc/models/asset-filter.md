
# Asset Filter

Asset Filter

## Structure

`AssetFilter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ap_mac` | `string` | Optional | - |
| `beam` | `int` | Optional | - |
| `created_time` | `float` | Optional | - |
| `disasbled` | `bool` | Optional | whether the asset filter is disabled |
| `eddystone_uid_namespace` | `string` | Optional | eddystone uid namespace used to filter assets |
| `eddystone_url` | `string` | Optional | eddystone url used to filter assets |
| `for_site` | `bool` | Optional | - |
| `ibeacon_major` | `int` | Optional | ibeacon major value used to filter assets |
| `ibeacon_uuid` | `uuid\|string` | Optional | ibeacon uuid used to filter assets |
| `id` | `uuid\|string` | Optional | - |
| `mfg_company_id` | `int` | Optional | ble manufacturing-specific company-id used to filter assets |
| `modified_time` | `float` | Optional | - |
| `name` | `string` | Required | - |
| `org_id` | `uuid\|string` | Optional | - |
| `rssi` | `int` | Optional | - |
| `service_uuid` | `uuid\|string` | Optional | ble service data uuid used to filter assets |
| `site_id` | `uuid\|string` | Optional | - |

## Example (as JSON)

```json
{
  "eddystone_uid_namespace": "2818e3868dec25629ede",
  "eddystone_url": "https://www.abc.com",
  "ibeacon_major": 13,
  "ibeacon_uuid": "f3f17139-704a-f03a-2786-0400279e37c3",
  "mfg_company_id": 935,
  "name": "Visitor Tags",
  "service_uuid": "0000fe6a-0000-1000-8000-0030459b3cfb",
  "ap_mac": "ap_mac2",
  "beam": 168,
  "created_time": 198.3,
  "disasbled": false
}
```

