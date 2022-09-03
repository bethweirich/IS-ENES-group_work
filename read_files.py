#!/usr/bin/env python
# coding: utf-8
import glob
import os
import numpy as np

basepath = '/pool/data/CMIP6/data/ScenarioMIP/'
dirs = glob.glob(os.path.join(basepath, '*', '*', '*'))
models = {}
for path in dirs:
    split = os.path.split(path)
    pathname = split[-1]
    modelname = os.path.split(split[-2])[-1]
    if models.setdefault(modelname, []) != None:
        models[modelname].append(pathname)

all_scenarios = set()
for model, model_scenarios in models.items():
    all_scenarios = all_scenarios.union(set(model_scenarios))

counts = {}
for model, model_scenarios in models.items():
    for scenario_1 in all_scenarios:
        for scenario_2 in model_scenarios:
            if scenario_1 == scenario_2:
                if counts.setdefault(scenario_1, 0) != None:
                    counts[scenario_1] += 1

is_present = np.zeros((len(models), len(all_scenarios)))
md = []
for imodel, (model, model_scenarios) in enumerate(models.items()):
    md.append(model)
    for iscen, scenario in enumerate(all_scenarios):
        if scenario in model_scenarios:
            is_present[imodel, iscen] = 1


md = np.array(md)
idxs = np.nonzero(np.sum(is_present, 1) == 8)
modelnames = md[idxs]
filenames = []
for modelname in modelnames:
    for scenario in all_scenarios:
        if scenario != 'GISS-E2-1-G':
            filename = glob.glob(os.path.join('/pool/data/CMIP6/data/ScenarioMIP/*'
                                            , modelname, scenario,
                                              '*/day/tas/*/*/*.nc'))
            if filename:
                filenames.append(filename[0])
            else:
                print(modelname, scenario)

print(modelnames)
print(all_scenarios)





