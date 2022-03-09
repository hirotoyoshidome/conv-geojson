import json
import geojson
from geojson import Polygon, Feature


path = "./saitama.geojson"
out_path = "./out/"

_type = None
_name = None
_crs = None

with open(path, "r") as fil:
    data = json.load(fil)
    _type = data["type"]
    _name = data["name"]
    _crs = data["crs"]
    features = data["features"]
    for _features in features:
        out = out_path + "{0}-{1}-{2}.geojson".format(
            _features["properties"]["N03_001"],
            _features["properties"]["N03_003"]
            if _features["properties"]["N03_003"] is not None
            else "",
            _features["properties"]["N03_004"],
        )
        with open(out, "w") as ofil:
            geojson.dump(
                {
                    "type": _type,
                    "name": _name,
                    "crs": _crs,
                    "features": [_features],
                },
                ofil,
                ensure_ascii=False,
                indent=2,
            )
