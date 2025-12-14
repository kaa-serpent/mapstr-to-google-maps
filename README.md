# Mapstr to Google Maps Converter

A small Python utility to **convert a Mapstr export file** (JSON with geographic features) into a **CSV file you can import into Google My Maps**.

The script extracts place names and coordinates from your Mapstr JSON export and writes them to a simple CSV file using a semicolon (`;`) delimiter. This format is compatible with **Google My Maps** and other mapping platforms that accept CSV imports.

---

## Overview

**Input**

* A Mapstr JSON export containing geographic features

**Output**

* A CSV file with three columns:

  * **Name** — location name
  * **Latitude** — latitude coordinate
  * **Longitude** — longitude coordinate

The CSV uses a semicolon (`;`) as the delimiter to ensure compatibility with Google My Maps.

---

## Requirements

* Python 3.x
* Standard Python modules: `json` and `csv` (included with Python)

---

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/kaa-serpent/mapstr-to-google-maps.git
   cd mapstr-to-google-maps
   ```

2. Verify that Python 3 is installed:

   ```sh
   python3 --version
   ```

---

## Usage

1. Export your places from Mapstr as a JSON file.
2. Place the JSON file in the repository directory.
3. Run the conversion script:

   ```sh
   python3 converterMapSTRToCsvGoogleMaps.py input.json output.csv
   ```

   Replace:

   * `input.json` with the path to your Mapstr export file
   * `output.csv` with the desired output filename

The script will generate a CSV file where each row represents one place from your Mapstr export.

---

## Importing the CSV into Google My Maps

1. Go to **Google My Maps**: [https://www.google.com/mymaps](https://www.google.com/mymaps)
2. Create a new custom map.
3. Click **Import** in the new layer.
4. Upload the generated CSV file.
5. When prompted, select:

   * **Latitude** column for latitude
   * **Longitude** column for longitude

Your places will appear as points on the map.

---

## Example

Given a Mapstr export JSON file with multiple features, the script will produce a CSV like:

```csv
Name;Latitude;Longitude
Cafe Example;48.8566;2.3522
Park Example;48.8584;2.2945
```

This output can be loaded directly into Google My Maps.

---

## Notes

The script expects each feature in the JSON to contain:

* A `properties.name` field
* A `geometry.coordinates` array in the form `[longitude, latitude]`

If your export file does not follow this structure, the script may fail.

---

## License

This project is licensed under the **MIT License** — free to use, modify, and share.

---

## Contact

If you have questions or want to contribute, feel free to open issues or pull requests on the GitHub repository.
