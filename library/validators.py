# Link on GitHub: https://github.com/viacheslav-bandylo/111124-projects/blob/main/library/validators.py

from rest_framework import serializers



def validate_title_length(value):
    if len(value) < 10:
        raise serializers.ValidationError("Title of the Book must be at least 10 characters long.")

