import random
from datetime import datetime

FIELDS = [
    "timestamp", "sensor_id", "temperature", "humidity", "pressure",
    "iaq", "iaq_accuracy", "static_iaq", "co2_equivalent", "breath_voc_equivalent",
    "bmeGas1", "bmeGas2", "bmeGas3", "bmeGas4"
]

SENSOR_ID = "TEST_SENSOR_001"

def generate_row():
    return [
        datetime.utcnow().isoformat(),
        SENSOR_ID,
        round(random.uniform(20.0, 35.0), 2),
        round(random.uniform(30.0, 70.0), 2),
        round(random.uniform(1000.0, 1025.0), 2),
        round(random.uniform(0, 500), 2),
        random.randint(0, 3),
        round(random.uniform(0, 500), 2),
        round(random.uniform(400, 600), 2),
        round(random.uniform(0.2, 1.5), 2),
        round(random.uniform(100, 200), 2),
        round(random.uniform(100, 200), 2),
        round(random.uniform(100, 200), 2),
        round(random.uniform(100, 200), 2)
    ]

def generate_csv(rows=1):
    output = ["","<html><body>", ",".join(FIELDS)]
    for _ in range(rows):
        output.append(",".join(map(str, generate_row())))
    output.append("</body></html>")
    return "\n".join(output)

if __name__ == "__main__":
    with open("samples/sample_data_1.html", "w") as f:
        f.write(generate_csv(rows=5))

    with open("samples/sample_data_2.csv", "w") as f:
        f.write(",".join(FIELDS) + "\n")
        for _ in range(5):
            f.write(",".join(map(str, generate_row())) + "\n")
