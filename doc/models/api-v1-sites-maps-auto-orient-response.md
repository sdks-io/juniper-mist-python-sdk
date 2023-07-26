
# Api V1 Sites Maps Auto Orient Response

## Structure

`ApiV1SitesMapsAutoOrientResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `state` | [`State2Enum`](../../doc/models/state-2-enum.md) | Optional | The state of auto orient for a given map derived from an Enum |
| `time_queued` | `float` | Optional | Time when auto orient process was last queued for this map |

## Example (as JSON)

```json
{
  "state": "Oriented",
  "time_queued": 46.6
}
```

