
# Api V1 Sites Mxedges Support Response

## Structure

`ApiV1SitesMxedgesSupportResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_time` | `int` | Optional | - |
| `for_site` | `bool` | Optional | - |
| `id` | `string` | Optional | - |
| `magic` | `string` | Optional | - |
| `model` | `string` | Optional | - |
| `modified_time` | `int` | Optional | - |
| `mxagent_registered` | `bool` | Optional | - |
| `mxcluster_id` | `uuid\|string` | Optional | - |
| `name` | `string` | Optional | - |
| `org_id` | `string` | Optional | - |
| `services` | `List of string` | Optional | - |
| `site_id` | `string` | Optional | - |
| `status` | `string` | Optional | - |
| `tunterm_ip_config` | [`TuntermIpConfig1`](../../doc/models/tunterm-ip-config-1.md) | Optional | - |
| `tunterm_port_config` | [`TuntermPortConfig2`](../../doc/models/tunterm-port-config-2.md) | Optional | - |
| `tunterm_registered` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "created_time": 118,
  "for_site": false,
  "id": "id0",
  "magic": "magic0",
  "model": "model2"
}
```

