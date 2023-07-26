
# Map

Map

## Structure

`Map`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_time` | `float` | Optional | - |
| `flags` | `object` | Optional | name/val pair objects for location engine to use |
| `for_site` | `bool` | Optional | - |
| `height` | `float` | Optional | when type=image, height of the image map |
| `height_m` | `float` | Optional | - |
| `id` | `uuid\|string` | Optional | - |
| `latlng_br` | [`LatlngBr`](../../doc/models/latlng-br.md) | Optional | when type=google, latitude / longitude of the bottom-right corner |
| `latlng_tl` | [`LatlngTl`](../../doc/models/latlng-tl.md) | Optional | when type=google, latitude / longitude of the top-left corner |
| `locked` | `bool` | Optional | whether this map is considered locked down<br>**Default**: `False` |
| `modified_time` | `float` | Optional | - |
| `name` | `string` | Optional | The name of the map |
| `occupancy_limit` | `int` | Optional | - |
| `org_id` | `uuid\|string` | Optional | - |
| `orientation` | `float` | Optional | orientation of the map, 0 means up is north, 90 means up is west<br>**Default**: `0` |
| `origin_x` | `float` | Optional | the user-annotated x origin, pixels |
| `origin_y` | `float` | Optional | the user-annotated y origin, pixels |
| `ppm` | `float` | Optional | when type=image, pixels per meter |
| `site_id` | `uuid\|string` | Optional | - |
| `sitesurvey_path` | [`List of SitesurveyPath`](../../doc/models/sitesurvey-path.md) | Optional | sitesurvey_path<br>**Constraints**: *Minimum Items*: `0` |
| `thumbnail_url` | `string` | Optional | when type=image, the url for the thumbnail image / preview |
| `mtype` | [`Type30Enum`](../../doc/models/type-30-enum.md) | Optional | **Default**: `'image'` |
| `url` | `string` | Optional | when type=image, the url |
| `use_auto_orientation` | `bool` | Optional | whether this map uses autooreintation values or ignores them<br>**Default**: `False` |
| `use_auto_placement` | `bool` | Optional | whether this map uses autoplacement values or ignores them<br>**Default**: `False` |
| `view` | [`ViewEnum`](../../doc/models/view-enum.md) | Optional | when type=google |
| `wall_path` | [`WallPath`](../../doc/models/wall-path.md) | Optional | a JSON blob for wall definition (same format as wayfinding_path) |
| `wayfinding` | [`Wayfinding`](../../doc/models/wayfinding.md) | Optional | properties related to wayfinding |
| `wayfinding_path` | [`WayfindingPath`](../../doc/models/wayfinding-path.md) | Optional | a JSON blob for wayfinding (using Dijkstra’s algorithm) |
| `width` | `float` | Optional | when type=image, width of the image map |
| `width_m` | `float` | Optional | - |

## Example (as JSON)

```json
{
  "locked": false,
  "orientation": 0,
  "type": "image",
  "use_auto_orientation": false,
  "use_auto_placement": false,
  "created_time": 198.3,
  "flags": {
    "key1": "val1",
    "key2": "val2"
  },
  "for_site": false,
  "height": 18.96,
  "height_m": 245.68
}
```

