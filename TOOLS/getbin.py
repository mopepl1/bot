import csv
import pycountry


def country_code_to_emoji(code):
    """Convert a country code to its corresponding emoji flag."""
    try:
        return ''.join(chr(127397 + ord(c)) for c in code.upper())
    except Exception as e:
        print(f"Error converting country code to emoji: {e}")
        return "N/A"


def get_bin_info_from_csv(fbin, csv_file='FILES/bin_new.csv'):
    """Retrieve BIN information from a CSV file."""
    try:
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == fbin: 
                    return {
                        "bin": row[0],            # BIN
                        "brand": row[1],          # Brand
                        "type": row[2],           # Type (DEBIT, CREDIT, etc.)
                        "level": row[3],          # Level (PLATINUM, etc.)
                        "bank": row[4],           # Bank name
                        "country_code": row[7],   # Country code (BD)
                        "flag": row[8],           # Country code alpha-3 (BGD)
                        "country_name": row[9]    # Country name (BANGLADESH)
                    }
    except FileNotFoundError:
        print(f"CSV file '{csv_file}' not found.")
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return {}


async def get_bin_details(cc):
    """
    Get detailed information for a given card number using its BIN (first 6 digits).
    """
    fbin = cc[:6]
    currency = "N/A"  # Default currency value

    try:
        # Fetch BIN information from the CSV
        bin_info = get_bin_info_from_csv(fbin)

        # If no data is found, return defaults
        if not bin_info:
            return "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"

        # Extract fields from the BIN info
        brand = bin_info.get("brand", "N/A").upper()
        card_type = bin_info.get("type", "N/A").upper()
        level = bin_info.get("level", "N/A").upper()
        bank = bin_info.get("bank", "N/A").upper()
        country_code = bin_info.get("country_code", "N/A").upper()
        flag = country_code_to_emoji(country_code)
        country_name = bin_info.get("country_name", "N/A").upper()

        # Use pycountry to enrich country and currency details
        if country_code != "N/A":
            country = pycountry.countries.get(alpha_2=country_code)
            if country:
                country_name = country.name.upper()
                currency_obj = pycountry.currencies.get(numeric=country.numeric)
                if currency_obj:
                    currency = currency_obj.alpha_3

        # Fallback for country name if still missing
        if country_name == "N/A":
            country_name = country_code

        # Return detailed BIN information
        return brand, card_type, level, bank, country_name, flag, currency

    except Exception as e:
        print(f"Error processing BIN details: {e}")
        return "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"
