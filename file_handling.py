# file handling

def read_file(filename):
    """Simple file reader that reads a file as raw bytes and returns the data."""
    with open(filename, "rb") as file:
        data = file.read()

    return data

# analysers

def calculate_frequency(data):
    """Returns how frequently each byte occurs."""
    frequency = {}

    for byte in data:
        if byte in frequency:
            frequency[byte] += 1
        else:
            frequency[byte] = 1

    return frequency


def calculate_average(data):
    """Returns the average byte value."""
    if len(data) == 0:
        return 0

    return sum(data) / len(data)

def calculate_variation(data):
    """Returns the average difference between consecutive bytes."""
    if len(data) < 2:
        return 0

    total_difference = 0

    for i in range(len(data) - 1):
        difference = abs(data[i + 1] - data[i])
        total_difference += difference

    return total_difference / (len(data) - 1)

def find_dominant_bytes(frequency):
    """Find the most frequently occurring byte values."""
    # TODO
    return 0

def analyse_file(data):
    """Returns a dictionary of calculated frequency, average, variation and dominant byte(s) in file uploaded."""
    analysis = {
        "frequency": calculate_frequency(data),
        "average": calculate_average(data),
        "variation": calculate_variation(data)
    }

    analysis["dominant_bytes"] = find_dominant_bytes(analysis["frequency"])

    return analysis