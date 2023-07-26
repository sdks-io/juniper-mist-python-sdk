
# Junos Snmp Config

## Structure

`JunosSnmpConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_list` | [`List of ClientList`](../../doc/models/client-list.md) | Optional | - |
| `contact` | `string` | Optional | - |
| `description` | `string` | Optional | - |
| `enabled` | `bool` | Optional | **Default**: `True` |
| `engine_id` | [`EngineIdEnum`](../../doc/models/engine-id-enum.md) | Optional | - |
| `location` | `string` | Optional | - |
| `name` | `string` | Optional | - |
| `network` | `string` | Optional | **Default**: `'default'` |
| `trap_groups` | [`List of TrapGroup`](../../doc/models/trap-group.md) | Optional | - |
| `v_2_c_config` | [`List of V2cConfig`](../../doc/models/v2-c-config.md) | Optional | - |
| `v_3_config` | [`V3Config`](../../doc/models/v3-config.md) | Optional | - |
| `views` | [`Views`](../../doc/models/views.md) | Optional | - |

## Example (as JSON)

```json
{
  "contact": "cns@juniper.net",
  "description": "Juniper QFX Series Switch - 1K_5LA",
  "enabled": true,
  "location": "Las Vegas, NV",
  "name": "TGH-1K-QFX10K",
  "network": "default",
  "client_list": [
    {
      "client_list_name": "client_list_name7",
      "clients": [
        "clients9"
      ]
    }
  ],
  "engine_id": "use-default-ip-address"
}
```

