# NCAR CGD Ocean Section Catalogs

[Deployed Website](https://ncar.github.io/oce-catalogs/) | [Quick Demo Notebook](https://github.com/NCAR/oce-catalogs/blob/main/demo.ipynb)

### `reference-datasets.yml`

A collection of reference datasets containing both observations and model output.

This is an [intake-xarray catalog](https://intake-xarray.readthedocs.io). Here's an example:
```python
catalog = intake.open_catalog("/glade/campaign/cgd/oce/catalogs/reference-datasets.yml")
rapid = catalog["transports-rapid"].to_dask()  # returns Xarray dataset
```
