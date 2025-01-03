# mapstr to google maps Converter
convert mapstr export into a csv you can import in google maps

## Overview

This script is a Python utility designed to convert a JSON file containing GeoJSON-like from the application mapstr into a CSV file. The output CSV includes only three columns: Name, Latitude, and Longitude, ensuring compatibility with tools like Google MyMaps.

## How It Works

Input: A JSON file with geographic features. Each feature is expected to have:

A name field in its properties.

Coordinates in the geometry section, with longitude and latitude values.

Processing: The script reads the JSON file, extracts the relevant information from each feature, and writes it to a CSV file with ; as the delimiter.

Output: A CSV file containing:

Name: The name of the location.

Latitude: The latitude coordinate of the location.

Longitude: The longitude coordinate of the location.
