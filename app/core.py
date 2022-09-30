from google.cloud import vision
from google.oauth2 import service_account
from app.config import SERVICE_ACCOUNT_INFO
import re

def text_detection_google_vision(content:bytes):
    # credentials = service_account.Credentials.from_service_account_file("sturdy-quarter-361804-599639eb7da1.json")
    credentials = service_account.Credentials.from_service_account_info(SERVICE_ACCOUNT_INFO)
    client = vision.ImageAnnotatorClient(credentials=credentials)
    image = vision.Image(content=content)
    response = client.text_detection(
        image=image,
        image_context={"language_hints": ["id"]} # specify the language to avoid non latin characters
    )
    return response

def get_text_plate(response):
    """Get text of plate and chasis number,"""

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    else:
        def clean_the_text(text):
            """Remove non alphanumeric chars."""
            # substitute non alphanumeric to a space
            non_alphanum_pattern = re.compile(r"[^a-zA-Z0-9\s]+")
            cleaned_text = non_alphanum_pattern.sub(" ", text)
            # clean double or more whitespace
            more_whitespace_pattern = re.compile(r"\s{2,}")
            cleaned_text = more_whitespace_pattern.sub(" ", cleaned_text)
            return cleaned_text

        def get_plate_number(text):
            """Get text of plate number"""
            pattern = re.compile(r"^([A-Z]{1,2})\s?(\d{1,4})\s?([A-Z]{1,3})$", flags=re.MULTILINE)
            plate_number = pattern.search(text)
            if plate_number is not None:
                return (
                    plate_number.group(0), 
                    plate_number.group(1), 
                    plate_number.group(2), 
                    plate_number.group(3)
                )
            else:
                return None

        # Get first response text description 
        main_text = response.text_annotations[0].description 
        cleaned_text = clean_the_text(main_text)
        plate_number = get_plate_number(cleaned_text)

        result_dictionary = {}
        if plate_number is not None:
            result_dictionary['plate_number'] = plate_number[0]
            result_dictionary['region_cod'] = plate_number[1]
            result_dictionary['reg_number'] = plate_number[2]
            result_dictionary['letter_series'] = plate_number[3]
        else:
            result_dictionary['plate_number'] = "not found"
            result_dictionary['region_code'] = "not found"
            result_dictionary['reg_number'] = "not found"
            result_dictionary['letter_series'] = "not found"
        
        return result_dictionary

def get_text_stnk(response):
    """Get text of plate and chasis number,"""

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    else:
        def clean_the_text(text):
            """Remove non alphanumeric chars."""
            # substitute non alphanumeric to a space
            non_alphanum_pattern = re.compile(r"[^a-zA-Z0-9\s]+")
            cleaned_text = non_alphanum_pattern.sub(" ", text)
            # clean double or more whitespace
            more_whitespace_pattern = re.compile(r"\s{2,}")
            cleaned_text = more_whitespace_pattern.sub(" ", cleaned_text)
            return cleaned_text

        def get_plate_number(text):
            """Get text of plate number"""
            pattern = re.compile(r"^([A-Z]{1,2})\s?(\d{1,4})\s?([A-Z]{1,3})$", flags=re.MULTILINE)
            plate_number = pattern.search(text)
            if plate_number is not None:
                return (
                    plate_number.group(0), 
                    plate_number.group(1), 
                    plate_number.group(2), 
                    plate_number.group(3)
                )
            else:
                return None

        def get_chasis_number(text):
            """Get text of chasis number"""
            pattern = re.compile(r"[\w\d]{10,12}([\d]{5})")
            chasis_number = pattern.search(text)
            if chasis_number is not None:
                return chasis_number.group(0), chasis_number.group(1)
            else:
                return None

        # Get first response text description 
        main_text = response.text_annotations[0].description 
        cleaned_text = clean_the_text(main_text)
        plate_number = get_plate_number(cleaned_text)
        chasis_number = get_chasis_number(cleaned_text)

        result_dictionary = {}
        if plate_number is not None:
            result_dictionary["plate_number"] = plate_number[0]
            result_dictionary["region_code"] = plate_number[1]
            result_dictionary["reg_number"] = plate_number[2]
            result_dictionary["letter_series"] = plate_number[3]
        else:
            result_dictionary["plate_number"] = "not found"
            result_dictionary["region_code"] = "not found"
            result_dictionary["reg_number"] = "not found"
            result_dictionary["letter_series"] = "not found"
        
        if chasis_number is not None:
            result_dictionary["chasis_number"] = chasis_number[0]
            result_dictionary["last_five"] = chasis_number[1]
        else:
            result_dictionary["chasis_number"] = "not found"
            result_dictionary["last_five"] = "not found"

        return result_dictionary

def get_text_ktp(response):
    """Get text of id number."""

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    else:
        def clean_the_text(text):
            """Remove non alphanumeric chars."""
            # substitute non alphanumeric to a space
            non_alphanum_pattern = re.compile(r"[^a-zA-Z0-9\s]+")
            cleaned_text = non_alphanum_pattern.sub(" ", text)
            # clean double or more whitespace
            more_whitespace_pattern = re.compile(r"\s{2,}")
            cleaned_text = more_whitespace_pattern.sub(" ", cleaned_text)
            return cleaned_text

        def get_id_number(text):
            """Get text of id number or Indonesian NIK"""
            pattern = re.compile(r"\d{16}")
            id_number = pattern.search(text)
            if id_number is not None:
                return id_number.group(0)
            else:
                return None

        # Get first response text description 
        main_text = response.text_annotations[0].description 
        cleaned_text = clean_the_text(main_text)
        id_number = get_id_number(cleaned_text)

        result_dictionary = {}
        if id_number is not None:
            result_dictionary["id_number"] = id_number
        else:
            result_dictionary["id_number"] = "not found"        

        return result_dictionary

if __name__ == "__main__":
    print("OK")