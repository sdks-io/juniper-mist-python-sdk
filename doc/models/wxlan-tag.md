
# Wxlan Tag

WxLAN Tag

* type:
  ** client: created manually (e.g. on wireless client table, when they spot a device of interest, they can create an wxlan tag for it
  ** resource: created automatically when we discover a network resource
  ** subnet: create automatically when a subnet is discovered

* match:
  ** wlan_id, ap_id: values are a list of Wlan / Device ids
  ** client_mac: values are a list of MAC addresses

* radius_group: this is a smart tag that matches RADIUS-Filter-ID, Airespace-ACL-Name (VendorID=14179, VendorType=6) / Aruba-User-Role (VendorID=14823, VendorType=1)

* radius_username: this matches the ATTR-User-Name(1)

* radius_class: thie matches the ATTR-Class(25)

* radius_attr: the values are [ “6=1”, “26=10.2.3.4” ], this support other RADIUS attributes where we know the type

* radius_vendor: the values are [ “14179.10=1”, “14178.16=1.2.3.4” ], this matches vendor attributes and will be dynamically evaluated

## Structure

`WxlanTag`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_time` | `float` | Optional | - |
| `for_site` | `bool` | Optional | - |
| `id` | `uuid\|string` | Optional | - |
| `last_ips` | `List of string` | Optional | - |
| `mac` | `string` | Optional | - |
| `match` | [`Match1Enum`](../../doc/models/match-1-enum.md) | Optional | - |
| `modified_time` | `float` | Optional | - |
| `name` | `string` | Required | The name |
| `op` | [`Op1Enum`](../../doc/models/op-1-enum.md) | Optional | **Default**: `'in'` |
| `org_id` | `uuid\|string` | Optional | - |
| `resource_mac` | `string` | Optional | - |
| `services` | `List of string` | Optional | - |
| `site_id` | `uuid\|string` | Optional | - |
| `specs` | [`List of Spec2`](../../doc/models/spec-2.md) | Optional | - |
| `subnet` | `string` | Optional | - |
| `mtype` | [`Type43Enum`](../../doc/models/type-43-enum.md) | Required | - |
| `values` | `List of string` | Optional | list of values to match |

## Example (as JSON)

```json
{
  "name": "name0",
  "op": "in",
  "type": "match",
  "created_time": 198.3,
  "for_site": false,
  "id": "00001770-0000-0000-0000-000000000000",
  "last_ips": [
    "last_ips2"
  ],
  "mac": "mac4"
}
```

