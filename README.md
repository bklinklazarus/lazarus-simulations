# Lazarus Simulations

Scripts to simulate sensor behavior by generating synthetic HTML-embedded CSV files and raw CSVs for testing the ingestion pipeline.

## Includes:
- Python script to generate data (`generate_sensor_data.py`)
- HTML-wrapped and raw CSV sample files

## Usage

```bash
python3 generator/generate_sensor_data.py
```
This will regenerate both sample files inside the `samples/` directory.

---

Let me know if you want to extend it to simulate multiple sensors or time series gaps!
