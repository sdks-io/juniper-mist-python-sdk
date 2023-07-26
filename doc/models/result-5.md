
# Result 5

## Structure

`Result5`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Optional | - |
| `name` | `string` | Optional | org name |
| `num_aps` | `int` | Optional | - |
| `num_gateways` | `int` | Optional | - |
| `num_sites` | `int` | Optional | - |
| `num_switches` | `int` | Optional | - |
| `num_unassigned_aps` | `int` | Optional | - |
| `org_id` | `uuid\|string` | Optional | org id |
| `sub_ana_entitled` | `int` | Optional | - |
| `sub_ana_required` | `int` | Optional | - |
| `sub_ast_entitled` | `int` | Optional | - |
| `sub_ast_required` | `int` | Optional | - |
| `sub_eng_entitled` | `int` | Optional | - |
| `sub_eng_required` | `int` | Optional | - |
| `sub_ex_12_required` | `int` | Optional | - |
| `sub_insufficient` | `bool` | Optional | if this org has sufficient subscription |
| `sub_man_entitled` | `int` | Optional | - |
| `sub_man_required` | `int` | Optional | - |
| `sub_me_entitled` | `int` | Optional | - |
| `sub_vna_entitled` | `int` | Optional | - |
| `sub_vna_required` | `int` | Optional | - |
| `timestamp` | `float` | Optional | - |
| `trial_enabled` | `bool` | Optional | if this org is under trial period |
| `usage_types` | `List of string` | Optional | a list of types that enabled by usage |

## Example (as JSON)

```json
{
  "msp_id": "0000156c-0000-0000-0000-000000000000",
  "name": "name0",
  "num_aps": 230,
  "num_gateways": 22,
  "num_sites": 216
}
```

