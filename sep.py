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
    for fea in features:
        out = out_path + "{0}-{1}-{2}.geojson".format(
            fea["properties"]["N03_001"],
            fea["properties"]["N03_003"],
            fea["properties"]["N03_004"],
        )
        # poly = Polygon()
        # f = Feature(geometry=poly, properties={"country": "Spain"})
        # d = geojson.dumps(f, sort_keys=True)
        _features = fea["geometry"]["coordinates"]
        with open(out, "w") as of:
            geojson.dump(
                {
                    "type": _type,
                    "name": _name,
                    "crs": _crs,
                    "features": _features,
                },
                of,
                ensure_ascii=False,
            )
