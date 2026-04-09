#!/usr/bin/python3
"""
Task 0: Simple Templating Program
Generates personalized invitation files from a template and a list of attendees.
"""

import os


def generate_invitations(template, attendees):
    """
    Generates invitation files based on a template and a list of attendee dictionaries.

    Args:
        template (str): The invitation template containing placeholders.
        attendees (list): A list of dictionaries with attendee data.

    Behavior:
        - Validates input types.
        - Handles empty template or empty attendee list.
        - Replaces missing values with "N/A".
        - Creates output files named output_X.txt.
    """

    # -------------------------------
    # 1. Validate input types
    # -------------------------------
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # -------------------------------
    # 2. Handle empty template
    # -------------------------------
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # -------------------------------
    # 3. Handle empty attendees list
    # -------------------------------
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # -------------------------------
    # 4. Process each attendee
    # -------------------------------
    for index, attendee in enumerate(attendees, start=1):
        # Replace missing values with "N/A"
        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_date = attendee.get("event_date") or "N/A"
        event_location = attendee.get("event_location") or "N/A"

        # Create personalized invitation
        personalized = template.replace("{name}", name)
        personalized = personalized.replace("{event_title}", event_title)
        personalized = personalized.replace("{event_date}", event_date)
        personalized = personalized.replace("{event_location}", event_location)

        # -------------------------------
        # 5. Write output file
        # -------------------------------
        filename = f"output_{index}.txt"

        # If file exists, overwrite (allowed unless instructions say otherwise)
        try:
            with open(filename, "w") as f:
                f.write(personalized)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
            continue

    print("Invitation files generated successfully.")
