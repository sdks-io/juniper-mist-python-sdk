
# Junos Acl Policies

- for GBP-based policy, all src_tags and dst_tags have to be gbp-based
- for ACL-based policy, `network` is required in either the source or destination so that we know where to attach the policy to

## Structure

`JunosAclPolicies`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `actions` | [`List of Action`](../../doc/models/action.md) | Optional | - for GBP-based policy, all src_tags and dst_tags have to be gbp-based<br>- for ACL-based policy, `network` is required in either the source or destination so that we know where to attach the policy to |
| `name` | `string` | Optional | - |
| `src_tags` | `List of string` | Optional | - for GBP-based policy, all src_tags and dst_tags have to be gbp-based<br>- for ACL-based policy, `network` is required in either the source or destination so that we know where to attach the policy to |

## Example (as JSON)

```json
{
  "name": "guest access",
  "actions": [
    {
      "action": "deny",
      "dst_tag": "dst_tag1"
    },
    {
      "action": "allow",
      "dst_tag": "dst_tag2"
    },
    {
      "action": "deny",
      "dst_tag": "dst_tag3"
    }
  ],
  "src_tags": [
    "src_tags1",
    "src_tags2"
  ]
}
```

