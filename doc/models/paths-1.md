
# Paths 1

## Structure

`Paths1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bfd_profile` | [`BfdProfileEnum`](../../doc/models/bfd-profile-enum.md) | Optional | **Default**: `'broadband'`<br>**Constraints**: *Minimum Length*: `1` |
| `ip` | `string` | Optional | if different from the wan port<br>**Constraints**: *Minimum Length*: `1` |

## Example (as JSON)

```json
{
  "bfd_profile": "broadband",
  "ip": "ip4"
}
```

