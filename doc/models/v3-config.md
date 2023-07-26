
# V3 Config

## Structure

`V3Config`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notify` | [`List of Notify`](../../doc/models/notify.md) | Optional | - |
| `notify_filter` | [`List of NotifyFilter`](../../doc/models/notify-filter.md) | Optional | - |
| `target_address` | [`List of TargetAddress`](../../doc/models/target-address.md) | Optional | - |
| `target_parameters` | [`List of TargetParameter`](../../doc/models/target-parameter.md) | Optional | - |
| `usm` | [`Usm`](../../doc/models/usm.md) | Optional | - |
| `vacm` | [`Vacm`](../../doc/models/vacm.md) | Optional | - |

## Example (as JSON)

```json
{
  "notify": [
    {
      "name": "name0",
      "tag": "tag4",
      "type": "trap"
    },
    {
      "name": "name1",
      "tag": "tag5",
      "type": "inform"
    }
  ],
  "notify_filter": [
    {
      "contents": [
        {
          "include": true,
          "oid": "oid7"
        }
      ],
      "profile_name": "profile_name3"
    }
  ],
  "target_address": [
    {
      "address": "address7",
      "address_mask": "address_mask9",
      "port": 243,
      "tag_list": "tag_list7",
      "target_address_name": "target_address_name5"
    },
    {
      "address": "address8",
      "address_mask": "address_mask0",
      "port": 244,
      "tag_list": "tag_list6",
      "target_address_name": "target_address_name6"
    }
  ],
  "target_parameters": [
    {
      "message_processing_model": "v1",
      "name": "name1",
      "notify_filter": "notify_filter3",
      "security_level": "privacy",
      "security_model": "v2c"
    },
    {
      "message_processing_model": "v3",
      "name": "name2",
      "notify_filter": "notify_filter4",
      "security_level": "none",
      "security_model": "usm"
    }
  ],
  "usm": {
    "engine-id": "engine-id8",
    "engine_type": "remote_engine",
    "users": [
      {
        "authentication_password": "authentication_password3",
        "authentication_type": "authentication-none",
        "encryption_password": "encryption_password7",
        "encryption_type": "privacy-des",
        "name": "name9"
      }
    ]
  }
}
```

