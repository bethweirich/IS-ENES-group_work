import xarray as xr

filename = '/pool/data/CMIP6/data/ScenarioMIP/NASA-GISS/GISS-E2-1-G/ssp119/r1i1p3f1/day/tas/gn/v20200115/tas_day_GISS-E2-1-G_ssp119_r1i1p3f1_gn_20150101-21001231.nc'

filename = '/pool/data/CMIP6/data/ScenarioMIP/CAS/FGOALS-g3/ssp585/r1i1p1f1/day/tas/gn/v20190819/tas_day_FGOALS-g3_ssp585_r1i1p1f1_gn_20660101-20661231.nc'

filename = '/pool/data/CMIP6/data/ScenarioMIP/CAS/FGOALS-g3/ssp585/r1i1p1f1/day/tas/gn/v20190819/tas_day_FGOALS-g3_ssp585_r1i1p1f1_gn_20660101-20661231.nc'

ds = xr.open_dataset(filename).load()
min_lon = 19.373147
max_lon = 28.247637
min_lat = 34.800885
max_lat = 41.748865

mask_lon = (ds.lon >= min_lon) & (ds.lon <= max_lon)
mask_lat = (ds.lat >= min_lat) & (ds.lat <= max_lat)

cropped_ds = ds.where(mask_lon & mask_lat, drop=True)





