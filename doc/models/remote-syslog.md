
# Remote Syslog

## Structure

`RemoteSyslog`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `archive` | [`Archive`](../../doc/models/archive.md) | Optional | - |
| `console` | [`Console`](../../doc/models/console.md) | Optional | - |
| `enabled` | `bool` | Optional | **Default**: `False` |
| `files` | [`List of typing.BinaryIO`](../../doc/models/file.md) | Optional | - |
| `network` | `string` | Optional | if source_address is configured, will use the vlan firstly otherwise use source_ip |
| `send_to_all_servers` | `bool` | Optional | **Default**: `True` |
| `servers` | [`List of Server1`](../../doc/models/server-1.md) | Optional | - |
| `time_format` | [`TimeFormatEnum`](../../doc/models/time-format-enum.md) | Optional | - |
| `users` | [`List of User1`](../../doc/models/user-1.md) | Optional | - |

## Example (as JSON)

```json
{
  "enabled": false,
  "send_to_all_servers": true,
  "archive": {
    "files": 122,
    "size": "size8"
  },
  "console": {
    "contents": [
      {
        "facility": "any",
        "severity": "notice"
      },
      {
        "facility": "authorization",
        "severity": "error"
      },
      {
        "facility": "conflict-log",
        "severity": "any"
      }
    ]
  },
  "files": [
    {
      "archive": {
        "files": 191,
        "size": "size1"
      },
      "contents": [
        {
          "facility": "dfc",
          "severity": "alert"
        },
        {
          "facility": "kernel",
          "severity": "emergency"
        }
      ],
      "explicit_priority": true,
      "file": "file7",
      "match": "match3"
    },
    {
      "archive": {
        "files": 190,
        "size": "size0"
      },
      "contents": [
        {
          "facility": "daemon",
          "severity": "any"
        }
      ],
      "explicit_priority": false,
      "file": "file8",
      "match": "match2"
    }
  ],
  "network": "network4"
}
```

