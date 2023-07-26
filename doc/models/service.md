
# Service

WIP

## Structure

`Service`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `addresses` | `List of string` | Optional | if `type`==`custom`, ip subnets |
| `app_caetgories` | `List of string` | Optional | list of application categories are available through /api/v1/const/app_categories |
| `apps` | `List of string` | Optional | when `type`==`app`, comes from `/api/v1/const/apps`<br>when `type`==`ssr_app`, comes from `/api/v1/const/ssr_apps`<br>when `type`==`srx_app`, comes from `/api/v1/const/srx_apps`<br>when `type`==`app_categories`, comes from `/api/v1/const/app_categories` |
| `created_time` | `int` | Optional | - |
| `description` | `string` | Optional | - |
| `dscp` | `int` | Optional | when `traffic_type`==`custom` |
| `failover_policy` | [`FailoverPolicyEnum`](../../doc/models/failover-policy-enum.md) | Optional | **Default**: `'revertable'` |
| `hostnames` | `List of string` | Optional | if `type`==`custom`, web filtering |
| `id` | `uuid\|string` | Optional | - |
| `max_jitter` | `int` | Optional | when `traffic_type`==`custom`, for uplink selection |
| `max_latency` | `string` | Optional | when `traffic_type`==`custom`, for uplink selection |
| `max_loss` | `int` | Optional | when `traffic_type`==`custom`, for uplink selection |
| `modified_time` | `int` | Optional | - |
| `name` | `string` | Optional | - |
| `org_id` | `uuid\|string` | Optional | - |
| `sle_enabled` | `bool` | Optional | whether to enable measure SLE<br>**Default**: `False` |
| `specs` | [`List of Spec1`](../../doc/models/spec-1.md) | Optional | when `type`==`addresses` or `type`==`hostnames`<br>if `type`==`custom`, specs is optional. If it doesn't exist, http and https is assumed.<br>**Constraints**: *Unique Items Required* |
| `traffic_class` | [`TrafficClassEnum`](../../doc/models/traffic-class-enum.md) | Optional | when `traffic_type`==`custom`<br>**Default**: `'best_effort'` |
| `traffic_type` | `string` | Optional | values from `/api/v1/consts/traffic_types`<br><br>* when `type`==`apps`, we'll choose traffic_type automatically<br>* when `type`==`addresses` or `type`==`hostnames`, you can provide your own settings (optional)<br>**Default**: `'data_best_effort'` |
| `mtype` | [`Type40Enum`](../../doc/models/type-40-enum.md) | Optional | **Default**: `'custom'` |
| `vpn_name` | [`VpnNameEnum`](../../doc/models/vpn-name-enum.md) | Optional | - |

## Example (as JSON)

```json
{
  "failover_policy": "revertable",
  "sle_enabled": false,
  "traffic_class": "best_effort",
  "traffic_type": "data_best_effort",
  "type": "custom",
  "addresses": [
    "addresses6",
    "addresses7"
  ],
  "app_caetgories": [
    "app_caetgories2"
  ],
  "apps": [
    "apps4",
    "apps5"
  ],
  "created_time": 118,
  "description": "description0"
}
```

