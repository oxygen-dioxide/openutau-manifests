import yaml
import py_linq
from typing import List

data = yaml.safe_load(open("manifestdata.yaml", encoding="utf8").read())
resamplers = data["resamplers"]
expressions = data["expressions"]
for resampler in data["resamplers"]:
    name:str = resampler["name"]
    supportedFlags:List[str] = resampler["supportedFlags"]
    manifest = {
        "expressions": py_linq.Enumerable(supportedFlags)\
            .to_dictionary(lambda key:key, lambda key:expressions[key])
    }
    yaml.dump(manifest,open(name+".yaml","w", encoding="utf8"))
    