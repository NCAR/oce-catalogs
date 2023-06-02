import intake
import pytest

cat = intake.open_catalog("reference-datasets.yml")

@pytest.mark.parametrize("key", tuple(cat.keys()))
def test_open_catalog_entry(key):
    cat[key].to_dask()
