
# Api V1 Sites Location Coverage Response

## Structure

`ApiV1SitesLocationCoverageResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `beams_means` | `List of float` | Required | list of [x, y, mean]s, x/y are in meters (UI would need to use map.ppm to calulate the pixel location from top-left). |
| `end` | `int` | Required | - |
| `gridsize` | `float` | Required | the size of grid, in meter |
| `result_def` | `List of string` | Required | list of names annotating the fields in results |
| `results` | `List of float` | Required | list of results, see result_def. |
| `start` | `int` | Required | - |

## Example (as JSON)

```json
{
  "beams_means": [
    [
      243.82
    ]
  ],
  "end": 254,
  "gridsize": 37.12,
  "result_def": [
    "result_def0",
    "result_def1",
    "result_def2"
  ],
  "results": [
    [
      65.73
    ]
  ],
  "start": 212
}
```

