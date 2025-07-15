# A program to extract data from a vehicle black box
# Lehlogonolo Tshehla
# 13 April 2025

def get_data_block(raw_string):
    """
    Extracts the telemetry block between START and END markers.
    """
    x = raw_string.find("START") +6
    y = raw_string.find("END") -1
    
    data = raw_string[x:y]
    
    return data

def rpm(data_block):
    """
    Extracts and returns the engine RPM as an integer.
    """
    x = data_block.find(":")+1
    y = data_block.find("|")
    
    rotate = data_block[x:y]
    return rotate

def speed(data_block):
    """
    Extracts and returns the vehicle speed as a float.
    """
    x = data_block.find("|")+1
    y = data_block.find("lat")-1
    
    velocity = data_block[x:y]
    return velocity    

def coordinates(data_block):
    """
    Extracts and returns latitude and longitude from the telemetry block as a tuple.
    """
    lat_s = data_block.find("lat")+4
    lat_e = data_block.find("long")-1
    
    long_s = data_block.find("long")+5
    long_e = data_block.find("name")-1
    
    x = data_block[lat_s:lat_e]
    y = data_block[long_s:long_e]
    location = "(" + x + "," + " " + y + ")"
    return location


def driver_name(data_block):
    """
    Extracts and returns the driver's name in title case.
    """
    x = data_block.find("name")+5
    
    person = data_block[x:]
    return person

def main():
    # Vehicle Telemetry
    string = input("Enter the raw data:\n")
    print("Vehicle Black Box Information:")
    raw_data = get_data_block(string)
    rotate = rpm(raw_data)
    print("Engine RPM:",rotate)
    velocity = speed(raw_data)
    print(f"Vehicle speed: {velocity}km/h")
    location = coordinates(raw_data)
    print("Coordinates:",location)
    person = driver_name(raw_data)
    print("Driver's name:",person)

if __name__ == "__main__":
    main()
