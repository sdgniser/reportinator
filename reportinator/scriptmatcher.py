import os
import sys
import reportinator.config
import importlib
sys.path.append(reportinator.config.script.location)

def main(module, section):
    module = module.lower()
    try:
        return importlib.import_module(module).main(section)
    except:
        try:
            return importlib.import_module("reportinator." + module).main(section)
        except:
            return importlib.import_module("reportinator.default").main(section)
